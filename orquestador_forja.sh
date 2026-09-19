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
# Y DOS FRENOS PROPIOS DE ESTA CASA, del 10 sep 2026, que se comprueban ANTES de
# gastar un turno:
#
#   - la rama activa tiene que ser $RAMA, y si no, se detiene NOMBRANDO LAS DOS
#   - MODO_INSERCION manda si el extractor inserta o deja en cuarentena. Su
#     default paso a `insertar` el 11 sep 2026: LA INSERCION DE UN LOTE CERRADO
#     ES AUTOMATICA (D.39), y la letra de lo que eso NO autoriza esta abajo
#   - la fase ciega ENTREGA al auditor lo que el acta anterior le dejo escrito,
#     y EXIGE que lo declare: lo que un auditor le deja al siguiente lo entrega
#     el arnes, no la memoria (D.40, 12 sep 2026)
#
# EL CRITERIO NO VIVE AQUI, Y DESDE EL 9 SEP 2026 YA ESTA ESCRITO: vive en
# docs/loop/EXTRACTOR.md (secciones 9 a 14) y docs/loop/AUDITOR_FORJA.md
# (secciones 5 a 7), que salieron de borrador con la cosecha
# (docs/COSECHA_2026-09.md seccion 7) y la calibracion (docs/CALIBRACION_D4.md).
# Este fichero sigue siendo fontaneria: mueve turnos, no decide nada sobre nodos.
#
# SE DETIENE SOLO SI: la rama activa no es $RAMA, MODO_INSERCION no es uno de
# sus dos valores, existe docs/loop/PARA_ALEXIS.md, no hay prompt siguiente, se
# alcanza MAX_VUELTAS, una invocacion falla MAX_INTENTOS veces seguidas por una
# de las dos especies que el arnes vigila (instantanea o turno mudo), el sello de
# la apertura ciega se rompe, o la apertura ciega no declara la herencia (D.40).
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

# LA INSERCION DE UN LOTE CERRADO ES AUTOMATICA (D.39, 11 sep 2026, decision del
# fundador). El default pasa de `cuarentena` a `insertar`.
#
# CORRECCION DECLARADA A D.26, que decia lo contrario y tenia razon el dia que se
# escribio: la insercion era una autorizacion del fundador porque el instrumento
# no se habia medido nunca. Ya se ha medido, seis veces, y el fundador dejo de
# pedir la firma: tres lotes con pasos inventados entre el 3 y el 8 por ciento,
# la aduana mordiendo, el auditor ciego en codigo y CERO inserciones indebidas.
#
# LO QUE EL DEFAULT NO AUTORIZA, y esta en la letra de D.39: solo entra un lote
# CERRADO EN EXTRACCION cuyo informe certifique el acta del auditor. Los
# candidatos de un lote ABIERTO siguen en cuarentena hasta que su lote cierre.
# El arnes no puede comprobar eso: lo comprueba el extractor leyendo D.39, y el
# auditor lo verifica.
#
#     MODO_INSERCION=cuarentena bash orquestador_forja.sh
#
# sigue disponible para una vuelta que no deba insertar nada.
#
# UN VALOR QUE NO SEA UNO DE LOS DOS DETIENE EL ARNES. No se interpreta ni se
# cae al default: un modo mal escrito es una autorizacion que nadie dio.
MODO_INSERCION="${MODO_INSERCION:-insertar}"

# LA RAMA DONDE SE INSERTA, Y SOLO AHI (D.45, 16 sep 2026). La extraccion de
# libros distintos corre en paralelo, una rama por libro y todas en cuarentena;
# la insercion es serial y unica. El arnes se detiene si alguien pide insertar
# desde una rama de libro.
RAMA_DE_INSERCION="${RAMA_DE_INSERCION:-extraccion-mundo-11}"

# ---------------------------------------------------------------------------
# EL INFORME DE LOTE QUE NO CABE EN UN TURNO SE SACA DEL TURNO
# (12 sep 2026, decision del fundador, punto 2).
#
# LA CIFRA QUE SOLO UN INFORME DE LOTE ENTERO VE es "CHOCAN entre si dentro del
# lote": un informe de uno en uno no puede verla, porque el choque es entre DOS
# candidatos del mismo lote, y de uno en uno nunca hay dos.
#
# Y EL INFORME DE LOTE ENTERO NO CABE EN UN TURNO. Medido el 12 sep 2026:
#
#     2 candidatos contra el grafo (203)            193 s   ->  96,5 s cada uno
#     2 candidatos contra grafo mas bandejas (286)  313 s   -> 156,5 s cada uno
#
# o sea MAS DE TRES HORAS para los 83 del lote 4. Ni el extractor de la vuelta 20
# ni el auditor pudieron terminarlo, y el fichero quedo en 480 bytes con solo la
# cabecera. No es lentitud de un modelo: es el coste del instrumento.
#
# ASI QUE LO CORRE EL ARNES, COMO PASO PROPIO, SIN RELOJ DE MODELO, y le entrega
# al extractor el fichero SELLADO con su hash. El extractor NO LO RECOMPUTA: LO
# CITA. Una cifra que vive donde cabe es una cifra que se puede firmar.
#
#     INFORME_DE_LOTE=cuarentena/scott_radical_candor bash orquestador_forja.sh
#
# VACIO POR DEFECTO, y es deliberado: EL ARNES NO SABE SI UN LOTE ESTA CERRADO
# (D.39 lo dice con esas palabras) ni lee actas. Quien lo sabe lo nombra al
# lanzar, igual que con MODO_INSERCION. Una ruta que no existe detiene el arnes
# antes de gastar un turno, en vez de entregar un informe vacio.
INFORME_DE_LOTE="${INFORME_DE_LOTE:-}"

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

# EL LOG TIENE DESTINO CONMUTABLE, y no es un capricho: durante la fase ciega
# (D.34, ampliada el 11 sep 2026) el arnes RETIRA docs/loop/loop.log del arbol,
# asi que sus propias lineas de esa ventana no pueden ir ahi. Van a un log
# provisional y se anexan al de verdad cuando el fichero vuelve. Sin esto, el
# arnes recrearia el fichero que acaba de retirar.
LOG_ACTIVO=""

log() {
  local destino="${LOG_ACTIVO:-$LOOP/loop.log}"
  echo "[$(date '+%Y-%m-%d %H:%M:%S')] $*" | tee -a "$destino"
}

comprobar_arranque() {
  # DOS FRENOS ANTES DE GASTAR UN SOLO TURNO.
  #
  # 1. LA RAMA ACTIVA TIENE QUE SER $RAMA. El arnes usa $RAMA solo para tirar y
  #    empujar, no hace checkout: lanzarlo desde otra rama trabajaria sobre la
  #    rama en la que estas y empujaria a otra. Se detiene NOMBRANDO LAS DOS,
  #    porque "rama equivocada" sin decir cuales obliga a ir a mirar.
  # 2. MODO_INSERCION tiene que ser uno de los dos valores. Un modo mal escrito
  #    NO cae al default: se detiene.
  local activa
  activa="$(git rev-parse --abbrev-ref HEAD 2>/dev/null || echo desconocida)"
  if [ "$activa" != "$RAMA" ]; then
    log "DETENIDO ANTES DE ARRANCAR: la rama activa es \"$activa\" y RAMA es \"$RAMA\"."
    log "  El arnes no hace checkout. Cambia de rama o pasa RAMA=$activa:"
    log "      git checkout $RAMA"
    log "      RAMA=$RAMA bash orquestador_forja.sh"
    exit 1
  fi
  case "$MODO_INSERCION" in
    cuarentena|insertar) ;;
    *)
      log "DETENIDO ANTES DE ARRANCAR: MODO_INSERCION=\"$MODO_INSERCION\" no es un modo."
      log "  Los dos valores son: insertar (el default desde D.39) o cuarentena."
      log "  UN MODO MAL ESCRITO NO SE INTERPRETA NI CAE AL DEFAULT: adivinar una"
      log "  autorizacion es justo lo que esta variable existe para impedir."
      exit 1
      ;;
  esac
  # 3. SI SE VA A INSERTAR, LA RAMA TIENE QUE SER LA DE INSERCION (D.45).
  #
  # LA EXTRACCION DE LIBROS DISTINTOS CORRE EN PARALELO; LA INSERCION NO. El
  # dataset, la bitacora, los censos y los pares mutuos son sedes UNICAS, y cada
  # insercion cambia lo que la siguiente mide (D.36): dos inserciones a la vez no
  # son la misma campania mas deprisa, son dos campanias distintas. La caida de la
  # vuelta 28 ya lo enseño con un nodo perdido y el gate en verde.
  #
  # EL ARNES NO SABE QUE ES UN LIBRO NI QUE ES UN FRENTE, igual que no sabe que es
  # un lote cerrado (D.39). Lo unico que puede comprobar sin leer nada es DONDE
  # esta parado y CON QUE PERMISO corre, y eso basta para que ninguna rama de libro
  # pueda insertar por accidente.
  if [ "$MODO_INSERCION" = "insertar" ] && [ "$activa" != "$RAMA_DE_INSERCION" ]; then
    log "DETENIDO ANTES DE ARRANCAR: MODO_INSERCION=insertar en la rama \"$activa\","
    log "  y la rama de insercion es \"$RAMA_DE_INSERCION\" (D.45)."
    log "  LA INSERCION ES SERIAL Y UNICA. Un frente de extraccion corre asi:"
    log "      MODO_INSERCION=cuarentena RAMA=$activa bash orquestador_forja.sh"
    log "  Si de verdad quieres insertar, hazlo en la rama de insercion, o declara"
    log "  otra con RAMA_DE_INSERCION=<rama>."
    exit 1
  fi
  log "arranque: rama $RAMA, MODO_INSERCION=$MODO_INSERCION"
}

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

vacio_o_ausente() { # $1 = ruta. Cierto si el fichero no existe o mide CERO BYTES.
  # LA RUTA QUE PROMETE PRUEBA ES CIFRA (My-idea, decision del fundador del
  # 5 sep 2026; docs/COSECHA_2026-09.md 7.B). Alli el ejemplar fue un comentario
  # de guarda que decia que cuatro arneses corrian "dentro de la bateria
  # despues (docs/loop/SALIDA_V173_BATERIA.txt)", y ese fichero medía CERO
  # BYTES, tres vueltas seguidas.
  #
  # SIN ESTA COMPROBACION EL TESTIGO TIENE UN AGUJERO EXACTO: un fichero que no
  # existia y aparece VACIO cambia de hash, asi que el turno pasaria por bueno
  # habiendo escrito nada. Un letrero de "aqui esta la prueba" sobre un vacio
  # engaña igual que un numero falso.
  local archivo="$1"
  [ -s "$archivo" ] && return 1
  return 0
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

fecha_modificacion() { # $1 = ruta. Segundos unix del fichero, 0 si no esta.
  # POR QUE mtime Y NO LA FECHA DEL COMMIT: los dos testigos del arnes se
  # commitean JUNTOS, en el mismo commit de artefactos, asi que sus fechas de
  # commit son identicas y no distinguen nada. Lo que si distingue es cuando los
  # ESCRIBIO el arnes, que es al acabar cada turno.
  [ -f "$1" ] || { printf '0'; return 0; }
  date -r "$1" +%s 2>/dev/null || stat -c %Y "$1" 2>/dev/null || printf '0'
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
    # EL REPORTE ES MAS NUEVO QUE EL ACTA. Casi siempre significa lo que parece:
    # hay una vuelta sin auditar delante. PERO NO SIEMPRE, y el 13 sep 2026 esta
    # medida se equivoco: una sesion del fundador REGENERO una tabla del reporte
    # (D.41) despues de que el acta estuviera escrita, y con eso la medida mandaba
    # al auditor a auditar una vuelta QUE YA TENIA ACTA. Un turno entero gastado,
    # y un acta de mas auditando nada.
    #
    # LA PREGUNTA DE VERDAD NO ES QUE FICHERO ES MAS NUEVO: ES QUIEN CORRIO EL
    # ULTIMO TURNO. Y de eso el arnes tiene registro propio y de nadie mas: sus
    # dos testigos, que escribe el al acabar cada turno y que no edita ningun
    # modelo (D.33). Si el ultimo turno que corrio fue el del AUDITOR, entonces
    # nadie ha extraido desde que se audito, y el reporte se toco FUERA de un
    # turno.
    #
    # LA COMPROBACION SOLO CORRIGE EN ESA DIRECCION Y SOLO CON PRUEBA DELANTE:
    # si falta cualquiera de los dos testigos, no hay prueba y manda la medida
    # de siempre. Una guarda que adivina donde no sabe es peor que la que fallo.
    local mt_extractor mt_auditor
    mt_extractor="$(fecha_modificacion "$LOOP/ultimo_extractor.json")"
    mt_auditor="$(fecha_modificacion "$LOOP/ultimo_auditor.json")"
    if [ "$mt_extractor" -gt 0 ] && [ "$mt_auditor" -gt "$mt_extractor" ]; then
      ROL_INICIAL="extractor"
      log "ROL INICIAL POR MEDICION: EXTRACTOR. El REPORTE es mas nuevo que el ACTA, PERO el ultimo turno que corrio el arnes fue el del AUDITOR: el reporte se toco FUERA de un turno y no hay vuelta sin auditar."
      log "  ultimo commit de REPORTE.md      : $(fecha_legible "$ct_reporte") ($ct_reporte)"
      log "  ultimo commit de ACTA_AUDITOR.md : $(fecha_legible "$ct_acta") ($ct_acta)"
      log "  testigo del extractor escrito en : $(fecha_legible "$mt_extractor") ($mt_extractor)"
      log "  testigo del auditor escrito en   : $(fecha_legible "$mt_auditor") ($mt_auditor)"
      return 0
    fi
    ROL_INICIAL="auditor"
    log "ROL INICIAL POR MEDICION: AUDITOR. El REPORTE es mas nuevo que el ACTA, asi que la vuelta anterior quedo SIN AUDITAR."
    if [ "$mt_extractor" -gt 0 ] || [ "$mt_auditor" -gt 0 ]; then
      log "  y los testigos del arnes lo confirman: el ultimo turno NO fue el del auditor"
    fi
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
  antes del turno, O lo movio y lo dejo en CERO BYTES (una ruta que promete
  prueba sobre un vacio engaña igual que una cifra falsa). El testigo del extractor es docs/loop/REPORTE.md y el del
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
  git commit -m "Arnes detenido: fallo repetido del $rol por \"$motivo\"" >>"${LOG_ACTIVO:-$LOOP/loop.log}" 2>&1
  git push origin "$RAMA" >>"${LOG_ACTIVO:-$LOOP/loop.log}" 2>&1
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
      > "$salida" 2>>"${LOG_ACTIVO:-$LOOP/loop.log}"
    duracion=$((SECONDS - inicio))
    c="$(costo "$salida")"
    hash_despues="$(hash_fichero "$testigo")"

    motivo=""
    if [ "$duracion" -lt "$UMBRAL_SEGUNDOS" ] || ! costo_mayor_que_cero "$c"; then
      motivo="instantaneo"
    elif [ -n "$testigo" ] && [ "$hash_antes" = "$hash_despues" ]; then
      motivo="$rol mudo"
    elif [ -n "$testigo" ] && vacio_o_ausente "$testigo"; then
      # Movio su testigo, pero lo dejo VACIO: la ruta promete prueba y no la hay.
      motivo="$rol mudo"
    fi

    if [ -z "$motivo" ]; then
      log "$rol listo${c:+ (USD $c)}, ${duracion}s, intento $intento de $MAX_INTENTOS"
      return 0
    fi

    if [ "$motivo" = "$rol mudo" ]; then
      if [ "$hash_antes" != "$hash_despues" ]; then
        log "$rol: TURNO MUDO, el turno corrio ${duracion}s y cobro \"${c:-vacio}\" y toco $testigo pero lo dejo en CERO BYTES, intento $intento de $MAX_INTENTOS"
      else
        log "$rol: TURNO MUDO, el turno corrio ${duracion}s y cobro \"${c:-vacio}\" pero $testigo quedo identico, intento $intento de $MAX_INTENTOS"
      fi
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

# EL MANDATO DE INSERCION SALE DE MODO_INSERCION, y no de la costumbre. Antes
# el prompt permanente decia SIEMPRE que se inserta, asi que un encargo que
# pedia cero inserciones tenia que contradecirlo por escrito, y dos documentos
# que se contradicen enseñan a elegir cual obedecer. Ahora el arnes dice UNA
# sola cosa, y la dice el fundador al lanzarlo.
if [ "$MODO_INSERCION" = "insertar" ]; then
  MANDATO_INSERCION="LA INSERCION ESTA ABIERTA EN ESTA CORRIDA (MODO_INSERCION=insertar, que es el default desde D.39). PERO SOLO PARA UN LOTE CERRADO EN EXTRACCION cuyo informe haya certificado el acta del auditor: los candidatos de un lote ABIERTO se quedan en cuarentena hasta que su lote cierre, y meterlos antes es una caida de dato. NINGUN NODO ENTRA SIN PASAR POR LA ADUANA: se inserta con python forja.py insertar, UN CANDIDATO POR VEZ, y si la aduana bloquea lees a los vecinos y escribes el veredicto con su razon antes de insertar. Aplicas D.36 (el orden que lee) y D.37 (la serie que dice cuantas partes tiene), los veredictos van a bitacora/VEREDICTOS.jsonl y los insertados a cuarentena/_insertados/<libro>/ en el mismo acto. No existe la carga masiva."
else
  MANDATO_INSERCION="NO INSERTAS NADA EN ESTA CORRIDA (MODO_INSERCION=cuarentena, que es el default). TODO candidato que escribas queda en cuarentena/<libro>/<id_propuesto>.json y pasa por la aduana EN SECO, con python forja.py informe cuarentena/<libro>/<id_propuesto>.json en el mismo acto en que lo escribes; el que caeria lo corriges y lo reintentas. NO uses python forja.py insertar, ni aunque el candidato este perfecto: LA INSERCION ES UNA AUTORIZACION DEL FUNDADOR, NO UN DEFAULT, y en esta corrida no la ha dado. Al cerrar el capitulo corres el informe del lote entero y pegas su saldo en el reporte."
fi

PROMPT_EXTRACTOR_BASE="Estas en el repo forja-nodos. Lee docs/loop/EXTRACTOR.md (tus reglas permanentes) y despues docs/loop/PROMPT_SIGUIENTE.md (tu encargo). Ejecuta el encargo al pie de la letra. $MANDATO_INSERCION Abre docs/loop/REPORTE.md al empezar y hazlo crecer por anexion, con los discutibles marcados antes de saber si aciertas. Commitea y pushea TODO a la rama activa antes de terminar."

INFORME_LOTE_FICHERO="$LOOP/INFORME_DE_LOTE.txt"
SELLOS_INFORME="$LOOP/SELLOS_INFORME.jsonl"
MANDATO_INFORME=""

para_alexis_por_informe() { # vuelta lote motivo
  cat > "$LOOP/PARA_ALEXIS.md" <<EOF
# PARA_ALEXIS: el informe de lote del arnes no se pudo correr

La vuelta $1 iba a entregarle al extractor el informe del lote $2 corrido por el
arnes como paso propio (decision del fundador del 12 sep 2026, punto 2), y no se
pudo.

Motivo:

$3

QUE SIGNIFICA. El informe de lote entero es la unica sede donde se puede medir
**CHOCAN entre si dentro del lote**, y no cabe en un turno de modelo: mas de tres
horas para un lote de 83, medido. Por eso lo corre el arnes. Si el arnes no puede
correrlo, el extractor tampoco, y esa cifra no se puede firmar en esta vuelta.

QUE NO SIGNIFICA. No dice que el lote este mal ni que ningun candidato sea falso.
Dice que el saldo del lote se queda sin instrumento detras.

Estado: rama $RAMA, hash $(git rev-parse --short HEAD 2>/dev/null || echo desconocido).

Como retomar: comprueba que la carpeta existe y relanza. Si no quieres informe de
lote en esta corrida, lanza sin INFORME_DE_LOTE: el paso se salta y queda escrito
en el log que se salto.
EOF
}

# EL PASO PROPIO DEL ARNES, ANTES DEL TURNO DEL EXTRACTOR. Sin reloj de modelo.
informe_de_lote() { # vuelta
  MANDATO_INFORME=""
  if [ -z "$INFORME_DE_LOTE" ]; then
    log "VUELTA $1 : SIN INFORME DE LOTE en esta corrida (INFORME_DE_LOTE vacio)"
    return 0
  fi
  if [ ! -d "$INFORME_DE_LOTE" ]; then
    log "DETENIDO en la vuelta $1: INFORME_DE_LOTE no es una carpeta: $INFORME_DE_LOTE"
    para_alexis_por_informe "$1" "$INFORME_DE_LOTE" "la carpeta no existe en el arbol"
    exit 1
  fi
  local arranque fin sello fecha
  arranque="$(date +%s)"
  log "VUELTA $1 : INFORME DE LOTE sobre $INFORME_DE_LOTE (paso del arnes, sin reloj de modelo)"
  log "  tarda, y esta medido: 156,5 s por candidato con la poblacion de bandejas"
  if ! python forja.py informe --carpeta "$INFORME_DE_LOTE" > "$INFORME_LOTE_FICHERO" 2>&1; then
    log "DETENIDO en la vuelta $1: el informe de lote salio en error. Ver $LOOP/PARA_ALEXIS.md"
    para_alexis_por_informe "$1" "$INFORME_DE_LOTE" "$(tail -5 "$INFORME_LOTE_FICHERO" 2>/dev/null)"
    exit 1
  fi
  fin="$(date +%s)"
  sello="$(git hash-object "$INFORME_LOTE_FICHERO" 2>/dev/null || echo sin-sello)"
  fecha="$(date "+%Y-%m-%d %H:%M:%S")"
  printf '{"vuelta": %s, "fecha": "%s", "lote": "%s", "sello": "%s", "segundos": %s}\n' \
    "$1" "$fecha" "$INFORME_DE_LOTE" "$sello" "$((fin - arranque))" >> "$SELLOS_INFORME"
  log "  informe sellado: $sello  ($((fin - arranque)) s)"
  log "  el extractor lo CITA por su sello y NO lo recomputa (punto 2 del 12 sep 2026)"
  git add "$INFORME_LOTE_FICHERO" "$SELLOS_INFORME" >>"$LOOP/loop.log" 2>&1 || true
  git commit -q -m "Informe del lote $INFORME_DE_LOTE de la vuelta $1, corrido y sellado por el arnes (punto 2 del 12 sep 2026)" >>"$LOOP/loop.log" 2>&1 || true
  MANDATO_INFORME="EL INFORME DEL LOTE YA ESTA CORRIDO Y SELLADO POR EL ARNES, Y NO ES TAREA TUYA. Esta en $INFORME_LOTE_FICHERO, con sello $sello (git hash-object), registrado en $SELLOS_INFORME. NO LO RECOMPUTES: CITALO por su sello, y pega de ahi el saldo y sobre todo la cifra CHOCAN entre si dentro del lote, que es la unica que un informe de uno en uno no puede ver. Lo corre el arnes porque no cabe en un turno: 156,5 segundos por candidato, medidos el 12 sep 2026. El informe de UN candidato suelto ese si lo corres tu, en el mismo acto en que lo escribes."
}

# ---------------------------------------------------------------------------
# LA APERTURA CIEGA, EN CODIGO (D.34, decision del fundador del 10 sep 2026).
#
# El auditor tiene que clasificar el material ANTES de leer el reporte del
# extractor, o su relectura no es ciega. Durante siete actas eso fue una
# PROMESA, y las siete se rompieron. El ACTA 6 la sustituyo por un artefacto
# (un bloque "LO QUE HE LEIDO HASTA AQUI" al principio del acta) y el propio
# auditor midio el resultado en el ACTA 7:
#
#     "Lo escribi, es lo primero del ACTA 7, y NO evito la contaminacion:
#      solo la hizo visible en la primera pagina en vez de en la cuarta.
#      EL ARTEFACTO DOCUMENTA, NO IMPIDE."
#
# LO QUE IMPIDE ES QUE EL FICHERO NO ESTE. La fase ciega RETIRA
# docs/loop/REPORTE.md del arbol, invoca al auditor con el material y sin el
# reporte, SELLA lo que escribio, y solo entonces devuelve el reporte.
#
# Y EL SELLO SE COMPRUEBA DESPUES DEL TURNO NORMAL. Un sello que nadie verifica
# es otra promesa: si la clasificacion ciega cambia despues de que el auditor
# vea el reporte, el arnes lo caza y se detiene.
# ---------------------------------------------------------------------------
APERTURA="$LOOP/APERTURA_CIEGA.md"
SELLOS="$LOOP/SELLOS_APERTURA.jsonl"

PROMPT_APERTURA_CIEGA="Estas en el repo forja-nodos, en la APERTURA CIEGA de tu turno de auditor. Lee docs/loop/AUDITOR_FORJA.md entero. AVISO: docs/loop/REPORTE.md, docs/loop/loop.log, docs/loop/ultimo_extractor.json y docs/loop/ultimo_auditor.json NO ESTAN en el arbol ahora mismo, y no estan a proposito. EN CAMBIO docs/loop/ACTA_AUDITOR.md SI ESTA Y SI PUEDES ABRIRLO: es obra tuya y no del extractor, no es ninguno de los cuatro que D.34.2 retira, y leerlo no es contaminacion sino lo unico que te deja saber que te encargaste a ti mismo (D.40): el mensaje final del extractor es un resumen de su propio reporte, asi que leerlo seria leer lo que vienes a leer a ciegas. NO los recuperes de git ni por ninguna otra via: recuperarlos invalida tu propia apertura y el arnes lo detecta y lo escribe. DOS REGLAS QUE MANDAN EN ESTA FASE. D.38.3: LA APERTURA CIEGA PUBLICA CLASES Y LECTURAS, NO CIFRAS CONTADAS A MANO; toda cifra que escribas aqui sale de un instrumento de la casa corrido en esta misma fase (wc -l, el contador de pasos, el barrido de vecinos) y va con su salida literal pegada al lado, y una cifra sin instrumento al lado NO SE PUBLICA. D.38.4: tu barrido de vecinos se hace sobre GRAFO MAS BANDEJAS, es decir dataset/nodos.jsonl mas todo lo que espera en cuarentena/<libro>/, porque un vecino que esta en la bandeja es vecino. Tu trabajo AHORA es clasificar el material por ti mismo y a ciegas: abre los candidatos del lote en cuarentena/, abre el texto fuente en fuentes/, y escribe en docs/loop/APERTURA_CIEGA.md tu clasificacion de cada candidato y de cada pieza que leas, con las lineas que la sostienen. Es la lectura que despues vas a comparar con la del extractor. Cuando termines, NO commitees: el arnes sella tu fichero y lo commitea el. Despues, en tu turno normal, recibiras el reporte."

apertura_ciega() { # $1 = vuelta
  local vuelta="$1" refugio="" sello fecha reaparecidos=""

  # LA FASE CIEGA RETIRA CUATRO FICHEROS, NO UNO (D.34, ampliada por decision
  # del fundador del 11 sep 2026).
  #
  # El reporte no era la unica via de contaminacion, y la que faltaba era la
  # peor: `ultimo_extractor.json` guarda EL MENSAJE FINAL DEL EXTRACTOR, que es
  # un resumen de su propio reporte escrito por el. Un auditor que lo abre lee
  # la version corta de lo que venia a leer a ciegas. `loop.log` dice lo que
  # hizo el turno, y `ultimo_auditor.json` trae el acta anterior resumida.
  #
  # HASTA HOY ESTO DEPENDIA DE QUE EL AUDITOR NO LOS ABRIERA, o sea de una
  # PROMESA, que es el genero de remedio que esta casa tiene medido que no
  # funciona (D.35: un remedio que se cumple acordandose no es un remedio).
  # Ahora no estan.
  # LA FASE CIEGA SABE QUE NO VE (18 sep 2026, decision del fundador).
  #
  # `loop.log` SALE DE LA RETIRADA. Es registro DEL ARNES, no del extractor, y sin el
  # la ciega no puede comprobar que se le retiro: se retiraba el registro que dice que
  # se retira. El auditor de la ACTA 43 publico, sellado, que `CREDITO_serial.jsonl` se
  # retiraba "y nadie lo declaro"; el arnes lo venia declarando en la linea de su propio
  # turno desde el 17 sep, y el no tenia con que mirarlo. Cargo la caida el solo, y su
  # racha llego a 3 de 3 por tres caidas de la misma familia: publicar sin comprobar.
  #
  # LO QUE SE PIERDE Y POR QUE SE ACEPTA: `loop.log` dice lo que hizo el turno del
  # extractor, asi que es una via de contaminacion. Pero es la UNICA sede donde la ciega
  # puede verificar su propia premisa, y una ciega que no puede comprobar lo que afirma
  # publica sin comprobar, que es peor: eso ya costo tres tandas.
  local retirar="REPORTE.md ultimo_extractor.json ultimo_auditor.json"

  rm -f "$APERTURA"
  refugio="$(mktemp -d)"
  local fichero
  for fichero in $retirar; do
    [ -f "$LOOP/$fichero" ] && mv "$LOOP/$fichero" "$refugio/$fichero"
  done

  # EL LOG YA NO SE DESVIA, y es la mitad que hace util lo de arriba: mientras
  # `loop.log` se retiraba, sus lineas de esta ventana iban a un fichero provisional,
  # asi que la linea de `retirados:` DE ESTE TURNO tampoco estaba donde la ciega podria
  # leerla. Dejar el fichero y seguir escribiendo fuera habria arreglado la mitad.
  LOG_ACTIVO=""

  # LO QUE UN AUDITOR LE DEJA AL SIGUIENTE LO ENTREGA EL ARNES, NO LA MEMORIA
  # (D.40). Se extrae del acta anterior ANTES de invocar, y se antepone al
  # prompt: tres actas seguidas perdieron el mismo remedio por tener que ir a
  # buscarlo en un fichero de dieciseis mil lineas.
  local herencia
  herencia="$(python forja.py herencia 2>&1)"
  local heredados
  heredados="$(printf '%s' "$herencia" | grep -c '^HEREDADO [0-9]* ' || true)"
  # LA FASE CIEGA NO VE EL REGISTRO DE CREDITO (D.52 punto 3, 17 sep 2026,
  # correccion declarada del fundador sobre su propia D.48).
  #
  # EL DEFECTO, MEDIDO POR EL AUDITOR DE LA ACTA 32: el registro trae el campo
  # `cita` de cada tanda, y ahi cabe una conclusion del reporte copiada dentro. A
  # ese auditor le dijo `11 SANO` ANTES de que contara los suyos. El arnes retiraba
  # cuatro ficheros por una puerta y D.48 abrio otra.
  #
  # SE RETIRA SOLO ALREDEDOR DEL TURNO DEL CIEGO, Y EL ORDEN IMPORTA: `herencia` ya
  # esta calculada arriba, porque forja.py herencia PREGUNTA al registro de que
  # linea es (D.48), y retirarlo antes haria que D.40 entregara CERO remedios
  # creyendo que la linea acaba de nacer. Primero se calcula, luego se retira.
  local credito_fichero
  credito_fichero="CREDITO_$(python -c "import sys; sys.path.insert(0, '.'); from src import credito; print(credito.linea_actual())" 2>/dev/null || echo serial).jsonl"
  [ -f "$LOOP/$credito_fichero" ] && mv "$LOOP/$credito_fichero" "$refugio/$credito_fichero"

  local linea_retirados="VUELTA $vuelta : APERTURA CIEGA ($MODELO_AUDITOR), retirados: $retirar $credito_fichero"
  log "$linea_retirados"
  log "  hereda $heredados remedio(s) del acta anterior, entregados en el prompt (D.40)"
  log "  y solo eso: remedios con su motivo, sin cifras ni conclusiones (D.52)"
  invocar_claude "auditor ciego" "$MODELO_AUDITOR" \
    "LO QUE ESTE TURNO NO VE, DICHO POR EL ARNES Y NO POR TI (D.57)

    $linea_retirados

Esa es la linea literal que el arnes acaba de escribir en docs/loop/loop.log para TU
turno. loop.log NO se retira: puedes abrirlo y comprobarla. Si vas a afirmar algo sobre
lo que se te retiro, compruebalo ahi.
Y SI NO PUEDES COMPROBAR ALGO, ESCRIBE LA LIMITACION en vez de la afirmacion (AUDITOR_FORJA.md 1.1: una busqueda negativa no se
puede citar).

$herencia

$PROMPT_APERTURA_CIEGA" \
    "$LOOP/ultimo_apertura.json" "$vuelta" "$APERTURA"

  # EL REGISTRO DE CREDITO VUELVE EN CUANTO EL CIEGO TERMINA, antes de que D.40 se
  # compruebe: esa comprobacion es del arnes, no del ciego, y necesita saber de que
  # linea es el acta. Si reaparecio durante el turno, se dice, igual que los otros.
  if [ -f "$LOOP/$credito_fichero" ]; then
    reaparecidos="$reaparecidos $credito_fichero"
    rm -f "$LOOP/$credito_fichero"
  fi
  [ -f "$refugio/$credito_fichero" ] && mv "$refugio/$credito_fichero" "$LOOP/$credito_fichero"

  # Y SE COMPRUEBA ANTES DE SELLAR. Un remedio entregado y no declarado es un
  # remedio perdido, que es justo lo que D.40 vino a impedir.
  local faltan
  if ! faltan="$(python forja.py herencia --comprobar 2>&1)"; then
    log "APERTURA CIEGA INCOMPLETA en la vuelta $vuelta (D.40). El arnes se detiene"
    log "  ANTES de que se escriba el acta. Lo que falta:"
    printf '%s\n' "$faltan" | while IFS= read -r renglon; do log "    $renglon"; done
    log "DETENIDO en la vuelta $vuelta: la apertura ciega no declaro su herencia (D.40). Ver $LOOP/PARA_ALEXIS.md"
    para_alexis_por_herencia "$vuelta" "$faltan"
    # los ficheros vuelven a su sitio antes de salir: una parada no deja el
    # arbol a medias.
    for fichero in $retirar; do
      [ -f "$refugio/$fichero" ] && mv "$refugio/$fichero" "$LOOP/$fichero"
    done
    LOG_ACTIVO=""
    [ -f "$refugio/loop_provisional.log" ] && cat "$refugio/loop_provisional.log" >> "$LOOP/loop.log"
    rm -rf "$refugio"
    exit 1
  fi
  log "  herencia declarada: acta leida por su huella y los $heredados heredados resueltos"

  # ¿REAPARECIO ALGUNO DURANTE LA FASE CIEGA? Recuperarlos de git es la unica
  # via que queda, y es un acto deliberado. Se dice, no se calla.
  for fichero in $retirar; do
    if [ -f "$LOOP/$fichero" ]; then
      reaparecidos="$reaparecidos $fichero"
      rm -f "$LOOP/$fichero"
    fi
  done
  if [ -n "$reaparecidos" ]; then
    log "APERTURA CIEGA ROTA en la vuelta $vuelta: REAPARECIERON$reaparecidos"
    log "  durante la fase ciega. Solo se recuperan a mano, asi que fue deliberado."
  fi

  # EL TESTIGO DE GUARDAS, ANTES DEL SELLO (D.38.3 ensanchada el 16 sep 2026).
  #
  # UNA CIFRA VALE EN EL INSTANTE DEL SELLO. La apertura de la vuelta 29 publico
  # `guardas en rojo: 2` sostenido con la salida literal de su instrumento, que era
  # VERDE cuando corrio; entre esa corrida y el sello pasaron 44 minutos y cinco
  # guiones largos entraron en el arbol. La cifra era cierta al medirse y falsa al
  # publicarse, y ninguna regla cubria eso.
  #
  # El testigo corre las guardas baratas y deja la verdad del arbol en ese instante.
  # SI ALGUNA ESTA EN ROJO, EL SELLO NO SE ACEPTA: un rojo al cerrar significa que
  # la pagina cerro sobre un arbol que ya no era el que midio.
  log "  testigo de guardas, antes de sellar (D.38.3)"
  python scripts/testigo_guardas.py >>"$LOOP/loop.log" 2>&1 || true
  local desmiente
  if ! desmiente="$(python scripts/testigo_guardas.py --comprobar 2>&1)"; then
    log "SELLO NO ACEPTADO en la vuelta $vuelta: una guarda estaba en ROJO al sellar."
    printf '%s\n' "$desmiente" | while IFS= read -r renglon; do log "    $renglon"; done
    log "DETENIDO en la vuelta $vuelta: el testigo desmiente el estado del sello. Ver $LOOP/PARA_ALEXIS.md"
    para_alexis_por_testigo "$vuelta" "$desmiente"
    for fichero in $retirar; do
      [ -f "$refugio/$fichero" ] && mv "$refugio/$fichero" "$LOOP/$fichero"
    done
    LOG_ACTIVO=""
    [ -f "$refugio/loop_provisional.log" ] && cat "$refugio/loop_provisional.log" >> "$LOOP/loop.log"
    rm -rf "$refugio"
    exit 1
  fi
  log "  testigo: las guardas estaban en verde en el instante del sello"

  # EL SELLO. git hash-object da la misma huella que usa el testigo, asi que no
  # hay dos formas de medir lo mismo en este fichero.
  sello="$(git hash-object "$APERTURA" 2>/dev/null || echo sin-sello)"
  fecha="$(date '+%Y-%m-%d %H:%M:%S')"
  printf '{"vuelta": %s, "fecha": "%s", "sello": "%s"}\n' \
    "$vuelta" "$fecha" "$sello" >> "$SELLOS"
  log "  apertura ciega sellada: $sello"

  # Y AHORA, Y SOLO AHORA, SE LE DEVUELVE TODO.
  for fichero in $retirar; do
    [ -f "$refugio/$fichero" ] && mv "$refugio/$fichero" "$LOOP/$fichero"
  done
  # El log provisional se anexa al de verdad, que ya volvio: la ventana ciega
  # no se pierde del registro por haber ocurrido con el fichero fuera.
  LOG_ACTIVO=""
  if [ -f "$refugio/loop_provisional.log" ]; then
    cat "$refugio/loop_provisional.log" >> "$LOOP/loop.log"
  fi
  rm -rf "$refugio"

  git add "$APERTURA" "$SELLOS" >>"$LOOP/loop.log" 2>&1
  git commit -q -m "Apertura ciega de la vuelta $vuelta, sellada antes de exponer el reporte" \
    >>"$LOOP/loop.log" 2>&1
}

verificar_sello() { # $1 = vuelta. Cierto si la apertura ciega sigue siendo la sellada.
  local vuelta="$1" sello_actual sello_guardado
  [ -f "$APERTURA" ] || return 0
  sello_actual="$(git hash-object "$APERTURA" 2>/dev/null || echo sin-sello)"
  sello_guardado="$(grep -o '"sello": "[^"]*"' "$SELLOS" 2>/dev/null | tail -1 \
    | sed 's/.*"sello": "//; s/"$//')"
  [ -z "$sello_guardado" ] && return 0
  if [ "$sello_actual" != "$sello_guardado" ]; then
    log "SELLO ROTO en la vuelta $vuelta: docs/loop/APERTURA_CIEGA.md cambio DESPUES"
    log "  de exponerse el reporte. Sellado $sello_guardado, ahora $sello_actual."
    para_alexis_por_sello "$vuelta" "$sello_guardado" "$sello_actual"
    return 1
  fi
  log "  sello de la apertura ciega verificado: intacto tras el turno"
  return 0
}

para_alexis_por_testigo() { # vuelta lo_que_desmiente
  cat > "$LOOP/PARA_ALEXIS.md" <<EOF
# PARA_ALEXIS: el testigo de guardas desmiente el estado del sello

La vuelta $1 cerro su apertura ciega con **una guarda en ROJO en el instante del
sello**, y por eso el sello NO se acepta (D.38.3 ensanchada el 16 sep 2026).

Lo que el testigo registro:

$2

QUE SIGNIFICA. Una cifra vale en el instante del sello. Si al cerrar hay una guarda
en rojo, la tabla de cierre de la pagina **no se escribio despues de volver a correr
las guardas**, asi que cualquier cifra de estado que publique puede haber caducado
entre la medida y el sello. Le paso a la vuelta 29 con 44 minutos y cinco guiones en
medio, y costo una racha entera.

QUE NO SIGNIFICA. No dice que la clasificacion sea falsa ni que el trabajo este mal.
Dice que el estado que la pagina publica no se puede firmar.

Estado: rama $RAMA, hash $(git rev-parse --short HEAD 2>/dev/null || echo desconocido).

Como retomar: deja el arbol limpio (lo que ensucio la guarda suele ser un fichero de
trabajo de la propia fase ciega), borra este fichero y relanza. El auditor vuelve a
abrir y esta vez el testigo lo confirma.
EOF
}

para_alexis_por_herencia() { # vuelta lo_que_falta
  cat > "$LOOP/PARA_ALEXIS.md" <<EOF
# PARA_ALEXIS: la apertura ciega no declaro lo que heredaba

La vuelta $1 entrego al auditor los remedios que el acta anterior dejo escritos
(D.40), y su apertura ciega no los declaro. **El arnes se detuvo ANTES de que se
escribiera el acta.**

Lo que falta:

$2

QUE SIGNIFICA. D.40 existe porque tres actas seguidas perdieron el mismo remedio
por tener que ir a buscarlo. El arnes ya lo entrega en el prompt: lo unico que se
pide es declarar que se leyo el acta, por su huella, y que se hizo con cada
remedio heredado. Un remedio entregado y no declarado es un remedio perdido.

QUE NO SIGNIFICA. No dice que el trabajo este mal, ni que la clasificacion sea
falsa. Dice que la vuelta no puede certificar que la herencia se recogio.

Estado: rama $RAMA, hash $(git rev-parse --short HEAD 2>/dev/null || echo desconocido).

Como retomar: borra este fichero y relanza. El auditor recibira la misma herencia
y esta vez tiene que declararla.
EOF
}

para_alexis_por_tablero() { # vuelta salida_de_la_guarda
  cat > "$LOOP/PARA_ALEXIS.md" <<EOF
# PARA_ALEXIS: el encargo no puede abrir el libro que declara (D.49, D.51)

La vuelta $1 no llego a gastar un turno. El arnes volvio a medir el tablero, leyo
que libro DECLARA docs/loop/PROMPT_SIGUIENTE.md, y ese libro no le corresponde a
esta linea.

Lo que midio la guarda:

$2

QUE SIGNIFICA. D.49: un libro, un dueño a la vez. Ninguna linea abre ni continua
un libro cuyo ESTADO no sea SIN EMPEZAR con dueño NINGUNO, o PAUSADO con dueño
NINGUNO y ya COSECHADO. Y D.51: ninguna linea elige libro, toma el de PRIORIDAD
mas baja cuyo estado lo permita.

QUE NO SIGNIFICA. No dice que el trabajo anterior este mal, ni que ninguna cifra
sea falsa. Dice que la vuelta iba a trabajar sobre un libro que otra linea tiene
abierto, o sobre uno que no le toca por el orden del mundo 11.

POR QUE ESTA GUARDA EXISTE. El 17 sep 2026 el lote 4 estaba a punto de cerrar, y
D.32 abre el lote siguiente SIN PARADA entre medias. El siguiente por orden era
el lote 5, que se estaba extrayendo en otra rama con 9 candidatos dentro. Lo unico
que lo impedia era una frase escrita a mano en el encargo, y D.35 dice lo que vale
eso: un remedio que se cumple acordandose no es un remedio.

Estado: rama $RAMA, hash $(git rev-parse --short HEAD 2>/dev/null || echo desconocido).

Como retomar, y son dos caminos distintos:

  1. Si el libro que toca esta PAUSADO en otra rama, lo que falta es el RELEVO
     (D.50): el frente detenido y sin proceso vivo, su rama cosechada a esta, el
     tablero puesto al dia, y solo entonces se continua desde el capitulo
     siguiente al ultimo minado. El paso de fundir es del fundador: el bucle no
     funde ramas.

  2. Si el encargo simplemente declaraba otro libro, corrige su linea
     'LIBRO DE ESTA VUELTA:' con el que 'python forja.py tablero --siguiente'
     nombra, borra este fichero y relanza.
EOF
}

para_alexis_por_sello() { # vuelta sellado actual
  cat > "$LOOP/PARA_ALEXIS.md" <<EOF
# PARA_ALEXIS: la apertura ciega se modifico despues de ver el reporte

La vuelta $1 sello docs/loop/APERTURA_CIEGA.md ANTES de exponerle el reporte al
auditor, y al terminar su turno el fichero ya no es el sellado.

    sellado antes de exponer el reporte : $2
    medido al terminar el turno         : $3

QUE SIGNIFICA. La apertura ciega existe para que la clasificacion del auditor se
escriba SIN el reporte delante (D.34). Si se reescribe despues, deja de ser
ciega y deja de servir para comparar dos lecturas independientes: es la misma
averia que la promesa rota, con un fichero por testigo.

QUE NO SIGNIFICA. No dice que la clasificacion sea falsa, ni que el acta este
mal. Dice que ESA comparacion, en ESTA vuelta, no vale.

Estado: rama $RAMA, hash $(git rev-parse --short HEAD 2>/dev/null || echo desconocido).

Como retomar: decide si la vuelta se repite con apertura ciega limpia o si se
acepta el acta declarando que su comparacion no es ciega. Borra este fichero
cuando lo hayas decidido.
EOF
}

PROMPT_AUDITOR="Estas en el repo forja-nodos. Lee docs/loop/AUDITOR_FORJA.md entero y actua como el auditor: verifica docs/loop/REPORTE.md contra el repo con tus propios comandos (python forja.py gate, python forja.py guiones, python tests/test_aceptacion.py y tu propio conteo del dataset), haz la relectura ciega empezando por los discutibles marcados, adjudica lo adjudicable, registra tu acta en docs/loop/ACTA_AUDITOR.md apendiendo, y escribe el encargo siguiente completo en docs/loop/PROMPT_SIGUIENTE.md. Si se cumple una condicion de parada de AUDITOR_FORJA.md, escribe docs/loop/PARA_ALEXIS.md con el motivo y el estado, y deja PROMPT_SIGUIENTE.md vacio. Commitea y pushea docs/loop/ antes de terminar."

comprobar_arranque

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

  # LA GUARDA DEL TABLERO (D.49, D.51). Vuelve a medir el tablero, lee que libro
  # DECLARA el encargo, y comprueba dos cosas distintas: que esta linea pueda
  # tomarlo (D.49, un libro un dueño a la vez) y que sea el que el orden del
  # mundo 11 le da (D.51, ninguna linea elige libro).
  #
  # VA DESPUES DE LAS DOS DE ARRIBA Y ANTES DE GASTAR UN TURNO, que es donde una
  # guarda cuesta menos: el 17 sep 2026 el lote 4 estaba a punto de cerrar y D.32
  # habria abierto el lote 5 SIN PARADA, que se estaba extrayendo en otra rama con
  # 9 candidatos dentro. Lo unico que lo impedia era una frase escrita a mano.
  if ! guarda_tablero="$(python scripts/guarda_tablero.py 2>&1)"; then
    echo "$guarda_tablero" >> "$LOOP/loop.log"
    log "DETENIDO en la vuelta $i: la guarda del tablero esta en ROJO (D.49, D.51)."
    log "  El encargo no puede abrir el libro que declara. Ver $LOOP/TABLERO.jsonl"
    para_alexis_por_tablero "$i" "$guarda_tablero"
    break
  fi
  echo "$guarda_tablero" >> "$LOOP/loop.log"
  log "  tablero comprobado: la vuelta puede abrir (D.49, D.51)"

  # La medicion del rol inicial se hace DESPUES del primer pull, para que mida
  # el estado de verdad de la rama y no una copia local rezagada.
  if [ "$i" -eq 1 ]; then
    decidir_rol_inicial
  fi

  if [ "$i" -eq 1 ] && [ "$ROL_INICIAL" = "auditor" ]; then
    log "VUELTA $i : SE SALTA EL TURNO DEL EXTRACTOR, la corrida empieza por el AUDITOR"
  else
    # EL INFORME DE LOTE VA ANTES DEL TURNO, NO DENTRO (punto 2 del 12 sep 2026).
    # Deja MANDATO_INFORME puesto si corrio, vacio si no habia lote que informar.
    informe_de_lote "$i"
    log "VUELTA $i : EXTRACTOR ($MODELO_EXTRACTOR)"
    invocar_claude "extractor" "$MODELO_EXTRACTOR" \
      "$PROMPT_EXTRACTOR_BASE $MANDATO_INFORME" \
      "$LOOP/ultimo_extractor.json" "$i" "$LOOP/REPORTE.md"

    git pull --rebase origin "$RAMA" >/dev/null 2>&1 || true
  fi

  apertura_ciega "$i"

  log "VUELTA $i : AUDITOR ($MODELO_AUDITOR)"
  invocar_claude "auditor" "$MODELO_AUDITOR" \
    "$PROMPT_AUDITOR" \
    "$LOOP/ultimo_auditor.json" "$i" "$LOOP/ACTA_AUDITOR.md"

  if ! verificar_sello "$i"; then
    log "DETENIDO en la vuelta $i: sello de la apertura ciega roto. Ver $LOOP/PARA_ALEXIS.md"
    exit 1
  fi

  git pull --rebase origin "$RAMA" >/dev/null 2>&1 || true
done

log "Arnes terminado. Revisa $LOOP/PARA_ALEXIS.md si existe, y $LOOP/ACTA_AUDITOR.md."
