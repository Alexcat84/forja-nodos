#!/usr/bin/env bash
# ARNES DEL EXTRACTOR de forja-nodos: dos asientos por vuelta, EXTRACTOR y
# AUDITOR. Se corre UNA vez, idealmente dentro de tmux:
#
#     bash orquestador_forja.sh
#
# ES PRIMO DEL orquestador.sh DE My-idea, Y LAS MECANICAS SE HEREDAN PORQUE YA
# ESTAN PROBADAS ALLI, cada una con la averia que la parió:
#
#   - deteccion de fallo instantaneo con espera y reintento del MISMO turno
#   - testigo de turno mudo (el turno corre, cobra, y no escribe su fichero)
#   - rol inicial por medicion, no por costumbre
#   - parada por docs/loop/PARA_ALEXIS.md
#
# LO QUE ESTE ARNES NO TRAE, y se dice para que nadie lo busque: EL CRITERIO DE
# EXTRACCION. docs/loop/EXTRACTOR.md y docs/loop/AUDITOR_FORJA.md estan en
# BORRADOR EN ESPERA DE LA COSECHA (docs/COSECHA_2026-09.md), y sus secciones de
# criterio estan vacias a proposito. Esto es fontaneria: mueve turnos, no decide
# nada sobre nodos.
#
# SE DETIENE SOLO SI: existe docs/loop/PARA_ALEXIS.md, no hay prompt siguiente,
# se alcanza MAX_VUELTAS, o una invocacion falla MAX_INTENTOS veces seguidas por
# una de las dos especies que el arnes vigila (instantanea o turno mudo).
#
# EL ESTADO VIVE EN EL REPO: cada vuelta sobrevive a caidas porque todo se
# commitea y se pushea.
set -uo pipefail
cd "$(dirname "$0")"

MAX_VUELTAS="${MAX_VUELTAS:-20}"
MODELO_EXTRACTOR="${MODELO_EXTRACTOR:-claude-opus-5}"
MODELO_AUDITOR="${MODELO_AUDITOR:-claude-opus-5}"
# El bucle vive en su propia rama. El merge a main es SIEMPRE decision de
# Alexis, nunca del bucle (docs/loop/AUDITOR_FORJA.md, condiciones de parada).
RAMA="${RAMA:-bucle}"
LOOP="docs/loop"
mkdir -p "$LOOP"

# Deteccion de fallo instantaneo (probable limite de uso agotado). Una
# invocacion que dura menos del umbral, o que no reporta costo positivo, no hizo
# trabajo real: se espera y se reintenta la MISMA invocacion, sin avanzar de
# rol. MAX_INTENTOS cuenta el intento original mas los reintentos: 7 intentos
# totales equivalen a 6 reintentos seguidos.
#
# LOS CUATRO SON VARIABLES DE ENTORNO A PROPOSITO, y no por comodidad: sin
# poder bajarlos, la prueba del arnes tardaria horas y no se correria nunca.
# Una guarda que no se puede probar no guarda nada (manual seccion 2).
UMBRAL_SEGUNDOS="${UMBRAL_SEGUNDOS:-120}"
ESPERA_SEGUNDOS="${ESPERA_SEGUNDOS:-1800}"
MAX_INTENTOS="${MAX_INTENTOS:-7}"
CLAUDE_BIN="${CLAUDE_BIN:-claude}"

log() { echo "[$(date '+%Y-%m-%d %H:%M:%S')] $*" | tee -a "$LOOP/loop.log"; }

costo() { # extrae total_cost_usd del json de salida de claude
  local archivo="$1" valor=""
  if command -v jq >/dev/null 2>&1; then
    valor="$(jq -r '.total_cost_usd // empty' "$archivo" 2>/dev/null)"
  fi
  if [ -z "$valor" ]; then
    # respaldo sin jq: extrae el numero directo del json de salida
    valor="$(grep -oE '"total_cost_usd"[[:space:]]*:[[:space:]]*[0-9.]+' "$archivo" 2>/dev/null \
      | grep -oE '[0-9.]+$' | head -1)"
  fi
  printf '%s' "$valor"
}

costo_mayor_que_cero() { # $1 = valor de costo, puede venir vacio
  [ -n "$1" ] && awk -v v="$1" 'BEGIN{exit !(v+0>0)}'
}

hash_fichero() { # $1 = ruta. Vacio si no existe: asi un fichero que NACE cuenta como cambio.
  local archivo="$1"
  [ -f "$archivo" ] || { printf ''; return 0; }
  git hash-object "$archivo" 2>/dev/null || printf 'sin-hash'
}

# ---------------------------------------------------------------------------
# EL ROL INICIAL SE DECIDE POR MEDICION, NO POR COSTUMBRE.
#
# Heredado de My-idea, donde tiene fecha y muerto: la vuelta 34 (15 ago 2026)
# corrio entera y NUNCA fue auditada, porque el auditor murio sin escribir acta
# y al relanzar volvio a ponerse al ejecutor delante, encima de un reporte que
# nadie habia verificado. El testigo cierra el caso DENTRO de una corrida; esta
# medicion lo cierra ENTRE corridas.
#
# LA MEDICION, y es de las baratas: la fecha del ultimo commit que toco el
# REPORTE contra la del ultimo que toco el ACTA. Si el reporte es mas nuevo, hay
# una vuelta sin auditar delante y la corrida empieza por el AUDITOR.
#
# EMPATE: si las dos fechas son iguales (o las dos son "nunca"), empieza el
# EXTRACTOR. Es la salida conservadora y se declara: un empate no es prueba de
# que falte un acta.
# ---------------------------------------------------------------------------
ROL_INICIAL=""

fecha_ultimo_commit() { # $1 = ruta. Imprime segundos unix, o 0 si nunca se commiteo.
  local ct
  ct="$(git log -1 --format=%ct -- "$1" 2>/dev/null)"
  printf '%s' "${ct:-0}"
}

fecha_legible() { # $1 = segundos unix
  [ "$1" = "0" ] && { printf 'nunca'; return 0; }
  date -d "@$1" '+%Y-%m-%d %H:%M:%S' 2>/dev/null || printf '%s' "$1"
}

decidir_rol_inicial() { # fija ROL_INICIAL. No imprime a stdout: escribe al log.
  local ct_reporte ct_acta
  if [ -n "${EMPEZAR_EN:-}" ]; then
    case "$EMPEZAR_EN" in
      extractor|auditor)
        ROL_INICIAL="$EMPEZAR_EN"
        log "ROL INICIAL FORZADO por EMPEZAR_EN: $ROL_INICIAL (gana sobre la medicion)"
        return 0
        ;;
      *)
        # Fallar ruidoso: una variable mal escrita que se ignora en silencio
        # deja la corrida haciendo lo contrario de lo que se le mando.
        log "DETENIDO: EMPEZAR_EN=\"$EMPEZAR_EN\" no es un rol valido. Usa extractor o auditor."
        exit 1
        ;;
    esac
  fi

  ct_reporte="$(fecha_ultimo_commit "$LOOP/REPORTE.md")"
  ct_acta="$(fecha_ultimo_commit "$LOOP/ACTA_AUDITOR.md")"

  if [ "$ct_reporte" -gt "$ct_acta" ]; then
    ROL_INICIAL="auditor"
    log "ROL INICIAL POR MEDICION: AUDITOR. El REPORTE es mas nuevo que el ACTA, asi que la vuelta anterior quedo SIN AUDITAR."
  else
    ROL_INICIAL="extractor"
    log "ROL INICIAL POR MEDICION: EXTRACTOR. El ACTA no es mas vieja que el REPORTE: no hay vuelta sin auditar delante."
  fi
  log "  ultimo commit de REPORTE.md      : $(fecha_legible "$ct_reporte") ($ct_reporte)"
  log "  ultimo commit de ACTA_AUDITOR.md : $(fecha_legible "$ct_acta") ($ct_acta)"
}

para_alexis_por_fallo() { # rol modelo vuelta duracion costo motivo testigo
  local rol="$1" modelo="$2" vuelta="$3" duracion="$4" c="$5" motivo="${6:-instantaneo}" testigo="${7:-}"
  cat > "$LOOP/PARA_ALEXIS.md" <<EOF
# PARA_ALEXIS: el arnes se detuvo por fallo repetido del $rol

Motivo: la invocacion del $rol ($modelo) fallo $MAX_INTENTOS veces seguidas en
la vuelta $vuelta, por la especie "$motivo".

Las DOS especies que el arnes trata igual (esperar $ESPERA_SEGUNDOS segundos y
reintentar el MISMO turno, sin avanzar de rol):

- instantaneo: la invocacion duro menos de $UMBRAL_SEGUNDOS segundos, o el json
  de salida no trae total_cost_usd mayor que 0. Es el patron esperable de un
  limite de uso agotado: el rol no llego a trabajar.
- turno mudo: el turno corrio y cobro, pero su testigo quedo IDENTICO al de
  antes del turno. El testigo del extractor es docs/loop/REPORTE.md y el del
  auditor es docs/loop/ACTA_AUDITOR.md. Es lo que paso de verdad en My-idea: la
  vuelta 34 (15 ago 2026) tuvo un auditor que corrio dieciocho minutos y termino
  sin escribir acta, y las vueltas 166 y 167 (4 sep 2026) terminaron las dos sin
  reporte, dos seguidas.

Ultimo intento: duracion ${duracion}s, costo reportado "${c:-vacio}"${testigo:+, testigo "$testigo"}.

Estado: rama $RAMA, hash $(git rev-parse --short HEAD 2>/dev/null || echo desconocido).

Lo que se necesita de Alexis: confirmar si el limite de uso ya se libero, o por
que el turno no escribe su fichero.

Como retomar: borra este fichero cuando el motivo ya no aplique y vuelve a
correr bash orquestador_forja.sh. El arnes sigue leyendo
docs/loop/PROMPT_SIGUIENTE.md desde donde quedo; no hace falta rehacer nada.
EOF
  git add "$LOOP/PARA_ALEXIS.md"
  git commit -m "Arnes detenido: fallo repetido del $rol por \"$motivo\"" >>"$LOOP/loop.log" 2>&1
  git push origin "$RAMA" >>"$LOOP/loop.log" 2>&1
}

invocar_claude() { # rol modelo prompt salida vuelta [testigo]
  # TESTIGO: fichero que el turno TIENE que haber cambiado para contar como
  # trabajo hecho. Nace de la vuelta 34 de My-idea, donde el auditor corrio
  # dieciocho minutos, cobro, y termino sin escribir acta: el turno parecia
  # bueno por duracion y por costo, y no lo era.
  #
  # AQUI LOS DOS ASIENTOS LLEVAN TESTIGO, y esa es la unica diferencia de fondo
  # con el primo de My-idea, donde solo lo llevaba el auditor. El motivo esta
  # medido y fechado en la cosecha (docs/COSECHA_2026-09.md, seccion 1.E, EL
  # REPORTE ABRE CON LA VUELTA): las vueltas 166 y 167 de My-idea terminaron las
  # DOS sin reporte, y cuando el reporte se cae no queda nada, ni las tareas que
  # si salieron. Un extractor mudo es la misma averia que un auditor mudo.
  #
  # Un turno que no movio su testigo se trata IGUAL que el fallo instantaneo: se
  # espera y se reintenta el MISMO turno, sin avanzar de rol y con el mismo tope.
  local rol="$1" modelo="$2" prompt="$3" salida="$4" vuelta="$5" testigo="${6:-}"
  local intento inicio duracion c hash_antes hash_despues motivo
  for intento in $(seq 1 "$MAX_INTENTOS"); do
    hash_antes="$(hash_fichero "$testigo")"
    inicio=$SECONDS
    "$CLAUDE_BIN" -p --model "$modelo" --dangerously-skip-permissions \
      --output-format json \
      "$prompt" \
      > "$salida" 2>>"$LOOP/loop.log"
    duracion=$((SECONDS - inicio))
    c="$(costo "$salida")"
    hash_despues="$(hash_fichero "$testigo")"

    motivo=""
    if [ "$duracion" -lt "$UMBRAL_SEGUNDOS" ] || ! costo_mayor_que_cero "$c"; then
      motivo="instantaneo"
    elif [ -n "$testigo" ] && [ "$hash_antes" = "$hash_despues" ]; then
      motivo="$rol mudo"
    fi

    if [ -z "$motivo" ]; then
      log "$rol listo${c:+ (USD $c)}, ${duracion}s, intento $intento de $MAX_INTENTOS"
      return 0
    fi

    if [ "$motivo" = "$rol mudo" ]; then
      log "$rol: TURNO MUDO, el turno corrio ${duracion}s y cobro \"${c:-vacio}\" pero $testigo quedo identico, intento $intento de $MAX_INTENTOS"
    else
      log "$rol: fallo instantaneo (probable limite de uso), ${duracion}s, costo \"${c:-vacio}\", intento $intento de $MAX_INTENTOS"
    fi
    if [ "$intento" -eq "$MAX_INTENTOS" ]; then
      para_alexis_por_fallo "$rol" "$modelo" "$vuelta" "$duracion" "$c" "$motivo" "$testigo"
      log "DETENIDO en la vuelta $vuelta: $rol fallo por \"$motivo\" $MAX_INTENTOS veces seguidas. Ver $LOOP/PARA_ALEXIS.md"
      exit 1
    fi
    log "fallo \"$motivo\"; espero $ESPERA_SEGUNDOS segundos y reintento"
    sleep "$ESPERA_SEGUNDOS"
  done
}

PROMPT_EXTRACTOR="Estas en el repo forja-nodos. Lee docs/loop/EXTRACTOR.md (tus reglas permanentes) y despues docs/loop/PROMPT_SIGUIENTE.md (tu encargo). Ejecuta el encargo al pie de la letra. NINGUN NODO ENTRA SIN PASAR POR LA ADUANA: se inserta con python forja.py insertar, un candidato por vez, y si la aduana bloquea escribes el veredicto con su razon. Abre docs/loop/REPORTE.md al empezar y hazlo crecer por anexion, con los discutibles marcados antes de saber si aciertas. Commitea y pushea TODO a la rama activa antes de terminar."

PROMPT_AUDITOR="Estas en el repo forja-nodos. Lee docs/loop/AUDITOR_FORJA.md entero y actua como el auditor: verifica docs/loop/REPORTE.md contra el repo con tus propios comandos (python forja.py gate, python forja.py guiones, python tests/test_aceptacion.py y tu propio conteo del dataset), haz la relectura ciega empezando por los discutibles marcados, adjudica lo adjudicable, registra tu acta en docs/loop/ACTA_AUDITOR.md apendiendo, y escribe el encargo siguiente completo en docs/loop/PROMPT_SIGUIENTE.md. Si se cumple una condicion de parada de AUDITOR_FORJA.md, escribe docs/loop/PARA_ALEXIS.md con el motivo y el estado, y deja PROMPT_SIGUIENTE.md vacio. Commitea y pushea docs/loop/ antes de terminar."

for i in $(seq 1 "$MAX_VUELTAS"); do
  git pull --rebase origin "$RAMA" >/dev/null 2>&1 || true

  if [ -f "$LOOP/PARA_ALEXIS.md" ]; then
    log "DETENIDO en la vuelta $i: existe $LOOP/PARA_ALEXIS.md. Leelo."
    break
  fi
  if [ ! -s "$LOOP/PROMPT_SIGUIENTE.md" ]; then
    log "DETENIDO en la vuelta $i: no hay PROMPT_SIGUIENTE.md con contenido."
    break
  fi

  # La medicion del rol inicial se hace DESPUES del primer pull, para que mida
  # el estado de verdad de la rama y no una copia local rezagada.
  if [ "$i" -eq 1 ]; then
    decidir_rol_inicial
  fi

  if [ "$i" -eq 1 ] && [ "$ROL_INICIAL" = "auditor" ]; then
    log "VUELTA $i : SE SALTA EL TURNO DEL EXTRACTOR, la corrida empieza por el AUDITOR"
  else
    log "VUELTA $i : EXTRACTOR ($MODELO_EXTRACTOR)"
    invocar_claude "extractor" "$MODELO_EXTRACTOR" \
      "$PROMPT_EXTRACTOR" \
      "$LOOP/ultimo_extractor.json" "$i" "$LOOP/REPORTE.md"

    git pull --rebase origin "$RAMA" >/dev/null 2>&1 || true
  fi

  log "VUELTA $i : AUDITOR ($MODELO_AUDITOR)"
  invocar_claude "auditor" "$MODELO_AUDITOR" \
    "$PROMPT_AUDITOR" \
    "$LOOP/ultimo_auditor.json" "$i" "$LOOP/ACTA_AUDITOR.md"

  git pull --rebase origin "$RAMA" >/dev/null 2>&1 || true
done

log "Arnes terminado. Revisa $LOOP/PARA_ALEXIS.md si existe, y $LOOP/ACTA_AUDITOR.md."
