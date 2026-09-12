#!/usr/bin/env bash
# PRUEBA DEL ARNES DEL EXTRACTOR, corrida FUERA del repo forja-nodos.
#
# Monta un repo de usar y tirar con su remoto bare, mete dentro
# orquestador_forja.sh y un CLAUDE FALSO cuyo comportamiento se dicta por
# variables de entorno, y corre DIECISEIS escenarios. Ninguno toca el repo de verdad.
#
# El claude falso es la unica forma de probar el arnes: un turno mudo o un fallo
# instantaneo no se pueden pedir a un modelo de verdad, y una guarda que no se
# puede probar no guarda nada (manual seccion 2).
set -uo pipefail

ORQUESTADOR="$1"
RAIZ_REPO="$(cd "$(dirname "$ORQUESTADOR")" && pwd)"
BANCO="$(mktemp -d)"
trap 'rm -rf "$BANCO"' EXIT

# Con escape, nunca literal: si esta prueba llevara el caracter, el barrido
# tendria que perdonar al fichero que lo comprueba.
GUION_LARGO="$(printf '\u2014')"

verdes=0
rojos=0

comprobar() { # descripcion, esperado, salida
  local desc="$1" esperado="$2" salida="$3"
  if echo "$salida" | grep -qF "$esperado"; then
    echo "    VERDE  $desc"
    verdes=$((verdes + 1))
  else
    echo "    ROJO   $desc"
    echo "           esperaba encontrar: $esperado"
    rojos=$((rojos + 1))
  fi
}

comprobar_no() { # descripcion, no_esperado, salida
  local desc="$1" no_esperado="$2" salida="$3"
  if echo "$salida" | grep -qF "$no_esperado"; then
    echo "    ROJO   $desc"
    echo "           NO deberia aparecer: $no_esperado"
    rojos=$((rojos + 1))
  else
    echo "    VERDE  $desc"
    verdes=$((verdes + 1))
  fi
}

montar_banco() { # $1 = nombre del escenario
  local nombre="$1" taller="$BANCO/$1"
  rm -rf "$taller"
  mkdir -p "$taller/docs/loop" "$taller/bin"

  git init -q --bare "$BANCO/$nombre.git"
  git init -q -b bucle "$taller"
  git -C "$taller" config user.email prueba@arnes.local
  git -C "$taller" config user.name "prueba del arnes"
  git -C "$taller" remote add origin "$BANCO/$nombre.git"

  cp "$ORQUESTADOR" "$taller/orquestador_forja.sh"
  # EL BANCO LLEVA EL INSTRUMENTO DE VERDAD, y no es un lujo: D.40 depende de
  # `python forja.py herencia`, y dejar que el arnes siga adelante cuando el
  # instrumento falta seria darle una salida silenciosa a la guarda.
  cp "$RAIZ_REPO/forja.py" "$taller/forja.py"
  cp -r "$RAIZ_REPO/src" "$taller/src"
  rm -rf "$taller/src/__pycache__"
  # Un acta con una TAREA BLOQUEANTE de verdad, para que haya algo que heredar.
  cat > "$taller/docs/loop/ACTA_AUDITOR.md" <<'ACTA'
# ACTA 1. VUELTA 1 de prueba

## 7. MIS CAIDAS

> ### **TAREA BLOQUEANTE DEL AUDITOR DE LA VUELTA 2, ESCRITA POR EL AUDITOR DE LA 1**
>
> **Una orden y se comprueba corriendo un comando.** Pega el instrumento al lado
> de cada cifra que publiques.
ACTA
  echo "encargo de prueba del arnes" > "$taller/docs/loop/PROMPT_SIGUIENTE.md"

  # EL CLAUDE FALSO. Distingue el rol por el documento que el prompt nombra.
  cat > "$taller/bin/claude" <<'FALSO'
#!/usr/bin/env bash
prompt="${!#}"
visto=""
declara=""
huella=""
if echo "$prompt" | grep -q "APERTURA CIEGA"; then
  # EL TERCER ROL (D.34). El auditor ciego escribe su clasificacion antes de
  # que exista el reporte, y aqui deja constancia de si LO VIO o no: es lo
  # unico que la prueba necesita comprobar de la fase ciega.
  rol="auditor ciego"; testigo="docs/loop/APERTURA_CIEGA.md"
  escribe="${FALSO_APERTURA:-si}"
  # EL AUDITOR CIEGO INTENTA ABRIR LOS CUATRO, y anota cual encontro. Es la
  # comprobacion de D.34 ampliada: no basta con que el arnes diga que los
  # retira, tiene que constar que NO estaban cuando alguien fue a por ellos.
  # D.40: el ciego declara su herencia solo si se le pide. Sin esto, la guarda
  # no tendria caso positivo.
  if [ "${FALSO_HERENCIA:-si}" = "si" ]; then
    huella="$(git hash-object docs/loop/ACTA_AUDITOR.md 2>/dev/null || echo sin-huella)"
    # ESCRITAS COMO LAS ESCRIBE EL AUDITOR DE VERDAD, en el markdown de la casa y
    # repitiendo la declaracion en la tabla de cierre. Asi era la apertura de la
    # vuelta 19, que la guarda vieja tumbo pidiendo el texto desnudo (12 sep 2026).
    declara="> ### **ACTA ANTERIOR LEIDA: \`$huella\`**

### \`HEREDADO 1\`: **CUMPLIDO**

| **herencia \`D.40\`** | **\`HEREDADO 1\`: CUMPLIDO**, fila a fila |"
  else
    declara=""
  fi
  visto="ausentes:"
  for f in REPORTE.md loop.log ultimo_extractor.json ultimo_auditor.json; do
    if [ -f "docs/loop/$f" ]; then visto="$visto ENCONTRADO_$f"; else visto="$visto $f"; fi
  done
elif echo "$prompt" | grep -q "EXTRACTOR.md"; then
  rol=extractor; testigo="docs/loop/REPORTE.md"; escribe="${FALSO_EXTRACTOR:-si}"
else
  rol=auditor;   testigo="docs/loop/ACTA_AUDITOR.md"; escribe="${FALSO_AUDITOR:-si}"
fi
# El prompt recibido se guarda para que la prueba pueda afirmar SOBRE EL. Sin
# esto, MODO_INSERCION solo se podria comprobar por sus efectos, y el efecto de
# "no insertes" es que no pasa nada, que es indistinguible de un turno vago.
printf '%s' "$prompt" > "prompt_${rol// /_}.txt"
sleep "${FALSO_SEGUNDOS:-2}"
if [ "$escribe" = "vacio" ]; then
  # el turno TOCA su testigo pero lo deja en cero bytes: la ruta promete
  # prueba y no la hay
  : > "$testigo"
  git add -A >/dev/null 2>&1
  git commit -q -m "turno del $rol con testigo vacio (claude falso)" >/dev/null 2>&1
elif [ "$escribe" = "si" ]; then
  echo "linea del $rol, $(date '+%H:%M:%S.%N')${visto:+ | $visto}" >> "$testigo"
  [ -n "${declara:-}" ] && printf '%s
' "$declara" >> "$testigo"
  git add -A >/dev/null 2>&1
  git commit -q -m "turno del $rol (claude falso)" >/dev/null 2>&1
  git push -q origin bucle >/dev/null 2>&1
fi
# El arnes vuelca ESTO en el artefacto DESPUES del ultimo commit (D.33).
sucio=""
if [ "${FALSO_SUCIO:-no}" = "si" ]; then sucio=" $(printf '\u2014') con guion largo"; fi
# Y un auditor que reescribe su apertura ciega tras ver el reporte (D.34).
if [ "$rol" = "auditor" ] && [ "${FALSO_ROMPE_SELLO:-no}" = "si" ]; then
  echo "linea escrita DESPUES de ver el reporte" >> "docs/loop/APERTURA_CIEGA.md"
fi
echo "{\"total_cost_usd\": ${FALSO_COSTO:-0.42}, \"result\": \"turno del $rol$sucio\"}"
FALSO
  chmod +x "$taller/bin/claude"

  git -C "$taller" add -A >/dev/null 2>&1
  git -C "$taller" commit -q -m "banco de pruebas del arnes" >/dev/null 2>&1
  git -C "$taller" push -q -u origin bucle >/dev/null 2>&1
  printf '%s' "$taller"
}

correr() { # taller, y el resto son variables de entorno ya exportadas
  ( cd "$1" && MAX_VUELTAS="${MAX_VUELTAS:-1}" \
      UMBRAL_SEGUNDOS=1 ESPERA_SEGUNDOS=1 MAX_INTENTOS=2 \
      CLAUDE_BIN="$1/bin/claude" RAMA="${RAMA:-bucle}" \
      bash orquestador_forja.sh 2>&1 )
}

echo "================================================================"
echo "PRUEBA DEL ARNES DEL EXTRACTOR"
echo "banco de pruebas: $BANCO   (fuera del repo, se borra al terminar)"
echo "umbral 1s, espera 1s, tope de intentos 2, claude FALSO"
echo "================================================================"

# ---------------------------------------------------------------- escenario 1
echo ""
echo "ESCENARIO 1: los dos asientos escriben. La vuelta pasa entera."
taller="$(montar_banco e1)"
salida="$(FALSO_EXTRACTOR=si FALSO_AUDITOR=si correr "$taller")"
echo "$salida" | sed 's/^/  | /'
comprobar "el extractor corre"                "VUELTA 1 : EXTRACTOR"        "$salida"
comprobar "el extractor pasa la guarda"       "extractor listo"             "$salida"
comprobar "el auditor corre"                  "VUELTA 1 : AUDITOR"          "$salida"
comprobar "el auditor pasa la guarda"         "auditor listo"               "$salida"
comprobar "la corrida cierra sola"            "Arnes terminado"             "$salida"
comprobar_no "no se escribe PARA_ALEXIS"      "PARA_ALEXIS.md. Leelo"       "$salida"
[ -f "$taller/docs/loop/PARA_ALEXIS.md" ] \
  && { echo "    ROJO   PARA_ALEXIS.md no deberia existir"; rojos=$((rojos+1)); } \
  || { echo "    VERDE  PARA_ALEXIS.md no existe"; verdes=$((verdes+1)); }

# ---------------------------------------------------------------- escenario 2
echo ""
echo "ESCENARIO 2: EXTRACTOR MUDO. Corre, cobra, y no mueve REPORTE.md."
taller="$(montar_banco e2)"
salida="$(FALSO_EXTRACTOR=no FALSO_AUDITOR=si correr "$taller")"
echo "$salida" | sed 's/^/  | /'
comprobar "el arnes lo llama turno mudo"      "extractor: TURNO MUDO"       "$salida"
comprobar "nombra el testigo que no se movio" "docs/loop/REPORTE.md quedo identico" "$salida"
comprobar "reintenta el MISMO turno"          "intento 2 de 2"              "$salida"
comprobar "espera entre intentos"             "espero 1 segundos y reintento" "$salida"
comprobar "detiene la corrida"                "DETENIDO en la vuelta 1"     "$salida"
comprobar "el motivo va nombrado"             "extractor mudo"              "$salida"
comprobar_no "el auditor NO llega a correr"   "VUELTA 1 : AUDITOR"          "$salida"
[ -f "$taller/docs/loop/PARA_ALEXIS.md" ] \
  && { echo "    VERDE  PARA_ALEXIS.md escrito"; verdes=$((verdes+1)); } \
  || { echo "    ROJO   falta PARA_ALEXIS.md"; rojos=$((rojos+1)); }
echo "  --- PARA_ALEXIS.md, primeras lineas ---"
sed -n '1,8p' "$taller/docs/loop/PARA_ALEXIS.md" 2>/dev/null | sed 's/^/  | /'

# ---------------------------------------------------------------- escenario 3
echo ""
echo "ESCENARIO 3: AUDITOR MUDO. El extractor pasa; el auditor no mueve su acta."
taller="$(montar_banco e3)"
salida="$(FALSO_EXTRACTOR=si FALSO_AUDITOR=no correr "$taller")"
echo "$salida" | sed 's/^/  | /'
comprobar "el extractor SI pasa"              "extractor listo"             "$salida"
comprobar "el auditor es turno mudo"          "auditor: TURNO MUDO"         "$salida"
comprobar "nombra el acta como testigo"       "docs/loop/ACTA_AUDITOR.md quedo identico" "$salida"
comprobar "reintenta el MISMO turno"          "intento 2 de 2"              "$salida"
comprobar "detiene la corrida"                "DETENIDO en la vuelta 1"     "$salida"
comprobar "el motivo va nombrado"             "auditor mudo"                "$salida"
[ -f "$taller/docs/loop/PARA_ALEXIS.md" ] \
  && { echo "    VERDE  PARA_ALEXIS.md escrito"; verdes=$((verdes+1)); } \
  || { echo "    ROJO   falta PARA_ALEXIS.md"; rojos=$((rojos+1)); }

# ---------------------------------------------------------------- escenario 4
echo ""
echo "ESCENARIO 4: PARADA POR PARA_ALEXIS.md. Existe antes de arrancar."
taller="$(montar_banco e4)"
echo "# parada de prueba" > "$taller/docs/loop/PARA_ALEXIS.md"
salida="$(FALSO_EXTRACTOR=si FALSO_AUDITOR=si correr "$taller")"
echo "$salida" | sed 's/^/  | /'
comprobar "detiene por el fichero de parada"  "existe docs/loop/PARA_ALEXIS.md. Leelo" "$salida"
comprobar_no "el extractor NO corre"          "VUELTA 1 : EXTRACTOR"        "$salida"
comprobar_no "el auditor NO corre"            "VUELTA 1 : AUDITOR"          "$salida"

# ---------------------------------------------------------------- escenario 5
echo ""
echo "ESCENARIO 5: ROL INICIAL POR MEDICION. El REPORTE es mas nuevo que el ACTA."
taller="$(montar_banco e5)"
echo "acta vieja" > "$taller/docs/loop/ACTA_AUDITOR.md"
git -C "$taller" add -A >/dev/null 2>&1
git -C "$taller" commit -q -m "acta de la vuelta anterior" >/dev/null 2>&1
sleep 1
echo "reporte nuevo, sin auditar" > "$taller/docs/loop/REPORTE.md"
git -C "$taller" add -A >/dev/null 2>&1
git -C "$taller" commit -q -m "reporte que nadie audito" >/dev/null 2>&1
git -C "$taller" push -q origin bucle >/dev/null 2>&1
salida="$(FALSO_EXTRACTOR=si FALSO_AUDITOR=si correr "$taller")"
echo "$salida" | sed 's/^/  | /'
comprobar "mide y elige auditor"              "ROL INICIAL POR MEDICION: AUDITOR" "$salida"
comprobar "dice por que"                      "quedo SIN AUDITAR"           "$salida"
comprobar "se salta el turno del extractor"   "SE SALTA EL TURNO DEL EXTRACTOR" "$salida"
comprobar_no "el extractor NO corre"          "extractor listo"             "$salida"
comprobar "el auditor SI corre"               "auditor listo"               "$salida"

# ---------------------------------------------------------------- escenario 6
echo ""
echo "ESCENARIO 6: FALLO INSTANTANEO. El turno vuelve sin costo y en cero segundos."
taller="$(montar_banco e6)"
salida="$(FALSO_EXTRACTOR=si FALSO_AUDITOR=si FALSO_SEGUNDOS=0 FALSO_COSTO=0 correr "$taller")"
echo "$salida" | sed 's/^/  | /'
comprobar "lo llama fallo instantaneo"        "fallo instantaneo (probable limite de uso)" "$salida"
comprobar "reintenta el MISMO turno"          "intento 2 de 2"              "$salida"
comprobar "detiene la corrida"                "DETENIDO en la vuelta 1"     "$salida"
comprobar "el motivo va nombrado"             "instantaneo"                 "$salida"

# ---------------------------------------------------------------- escenario 7
echo ""
echo "ESCENARIO 7: LA RUTA QUE PROMETE PRUEBA. El turno TOCA su testigo y lo"
echo "             deja en CERO BYTES. Cambia de hash, asi que sin la guarda"
echo "             de la cosecha 7.B pasaria por turno bueno."
taller="$(montar_banco e7)"
salida="$(FALSO_EXTRACTOR=vacio FALSO_AUDITOR=si correr "$taller")"
echo "$salida" | sed 's/^/  | /'
comprobar "lo caza como turno mudo"          "extractor: TURNO MUDO"        "$salida"
comprobar "dice que lo dejo en cero bytes"   "lo dejo en CERO BYTES"        "$salida"
comprobar "reintenta el MISMO turno"         "intento 2 de 2"               "$salida"
comprobar "detiene la corrida"               "DETENIDO en la vuelta 1"      "$salida"
comprobar_no "el auditor NO llega a correr"  "VUELTA 1 : AUDITOR"           "$salida"
[ -s "$taller/docs/loop/REPORTE.md" ] \
  && { echo "    ROJO   el testigo no deberia tener contenido"; rojos=$((rojos+1)); } \
  || { echo "    VERDE  el testigo existe y esta vacio, como el escenario pide"; verdes=$((verdes+1)); }

# ---------------------------------------------------------------- escenario 8
echo ""
echo "ESCENARIO 8: MODO_INSERCION POR DEFECTO. Desde D.39 (11 sep 2026) el"
echo "             default es INSERTAR, y no cuarentena: la insercion de un lote"
echo "             cerrado dejo de pedir firma. Pero el prompt tiene que llevar"
echo "             la letra que la limita, o el default seria una barra libre."
taller="$(montar_banco e8)"
salida="$(correr "$taller")"
echo "$salida" | sed 's/^/  | /'
comprobar "declara el modo al arrancar"      "MODO_INSERCION=insertar"      "$salida"
comprobar "la vuelta corre igual"            "VUELTA 1 : EXTRACTOR"         "$salida"
prompt="$(cat "$taller/prompt_extractor.txt" 2>/dev/null || echo SIN_PROMPT)"
comprobar "el prompt abre la insercion"      "LA INSERCION ESTA ABIERTA"    "$prompt"
comprobar "SOLO para un lote cerrado"        "SOLO PARA UN LOTE CERRADO"    "$prompt"
comprobar "y dice que pasa con el abierto"   "se quedan en cuarentena hasta que su lote cierre" "$prompt"
comprobar "manda uno por vez"                "UN CANDIDATO POR VEZ"         "$prompt"
comprobar "y nombra D.36 y D.37"             "D.36"                         "$prompt"

# ---------------------------------------------------------------- escenario 9
echo ""
echo "ESCENARIO 9: CASO POSITIVO DEL 8. Con MODO_INSERCION=cuarentena el mismo"
echo "             arnes PROHIBE insertar. Sin esto, el escenario 8 solo probaria"
echo "             que el prompt dice siempre lo mismo. El modo sigue existiendo"
echo "             para una vuelta que no deba insertar nada."
taller="$(montar_banco e9)"
salida="$(MODO_INSERCION=cuarentena correr "$taller")"
echo "$salida" | sed 's/^/  | /'
comprobar "declara el modo al arrancar"      "MODO_INSERCION=cuarentena"    "$salida"
prompt="$(cat "$taller/prompt_extractor.txt" 2>/dev/null || echo SIN_PROMPT)"
comprobar "el prompt prohibe insertar"       "NO INSERTAS NADA EN ESTA CORRIDA" "$prompt"
comprobar "y manda el informe en seco"       "forja.py informe"             "$prompt"
comprobar_no "no abre la insercion"          "LA INSERCION ESTA ABIERTA"    "$prompt"

# --------------------------------------------------------------- escenario 10
echo ""
echo "ESCENARIO 10: UN MODO MAL ESCRITO NO CAE AL DEFAULT. Un valor invalido"
echo "              detiene el arnes ANTES de gastar un turno: adivinar una"
echo "              autorizacion es justo lo que la variable existe para impedir."
taller="$(montar_banco e10)"
salida="$(MODO_INSERCION=insertarr correr "$taller")"
echo "$salida" | sed 's/^/  | /'
comprobar "se detiene antes de arrancar"     "DETENIDO ANTES DE ARRANCAR"   "$salida"
comprobar "nombra el valor recibido"         "insertarr"                    "$salida"
comprobar "nombra los dos valores validos"   "insertar (el default desde D.39) o cuarentena" "$salida"
comprobar "y dice la regla"                  "NI CAE AL DEFAULT"            "$salida"
comprobar_no "no gasta ni un turno"          "VUELTA 1 :"                   "$salida"

# --------------------------------------------------------------- escenario 11
echo ""
echo "ESCENARIO 11: EL FRENO DE RAMA. El arnes no hace checkout, asi que"
echo "              lanzarlo desde otra rama trabajaria sobre la que estas y"
echo "              empujaria a otra. Se detiene NOMBRANDO LAS DOS."
taller="$(montar_banco e11)"
git -C "$taller" checkout -q -b otra_rama
salida="$(correr "$taller")"
echo "$salida" | sed 's/^/  | /'
comprobar "se detiene antes de arrancar"     "DETENIDO ANTES DE ARRANCAR"   "$salida"
comprobar "nombra la rama activa"            'la rama activa es "otra_rama"' "$salida"
comprobar "nombra la rama pedida"            'RAMA es "bucle"'              "$salida"
comprobar "y dice como salir"                "git checkout bucle"           "$salida"
comprobar_no "no gasta ni un turno"          "VUELTA 1 :"                   "$salida"

# CASO POSITIVO DEL 11: el MISMO banco, de vuelta en su rama, corre.
git -C "$taller" checkout -q bucle
salida="$(correr "$taller")"
comprobar "en la rama correcta si arranca"   "arranque: rama bucle"         "$salida"
comprobar "y la vuelta corre"                "VUELTA 1 : EXTRACTOR"         "$salida"

# --------------------------------------------------------------- escenario 12
echo ""
echo "ESCENARIO 12: EL ARTEFACTO DEL ARNES NO TUMBA LA VUELTA (D.33). El arnes"
echo "              vuelca el texto del turno DESPUES del ultimo commit, asi"
echo "              que es la unica escritura del repo que no pasa por su"
echo "              propio hook. En la vuelta 7 un guion largo dentro de"
echo "              ultimo_extractor.json puso en rojo la prueba entera."
taller="$(montar_banco e12)"
salida="$(FALSO_SUCIO=si correr "$taller")"
echo "$salida" | sed 's/^/  | /'
comprobar "la vuelta corre entera"           "Arnes terminado"             "$salida"
comprobar "el extractor pasa"                "extractor listo"             "$salida"
comprobar "el auditor pasa"                  "auditor listo"               "$salida"
comprobar_no "no se escribe PARA_ALEXIS"     "PARA_ALEXIS.md. Leelo"       "$salida"
# Y EL GUION ESTA DE VERDAD AHI DENTRO: si no, la prueba no probaria nada.
artefacto="$(cat "$taller/docs/loop/ultimo_extractor.json" 2>/dev/null || echo AUSENTE)"
comprobar "el artefacto SI trae el guion"    "$GUION_LARGO"                "$artefacto"

# --------------------------------------------------------------- escenario 13
echo ""
echo "ESCENARIO 13: LA APERTURA CIEGA SELLA ANTES DE EXPONER (D.34). Durante"
echo "              siete actas fue una promesa y las siete se rompieron. El"
echo "              artefacto documenta, no impide: lo que impide es que el"
echo "              fichero no este."
taller="$(montar_banco e13)"
# LOS CUATRO EXISTEN ANTES, que es la situacion de cualquier vuelta que no sea
# la primera: si no existieran, "volvio a su sitio" no probaria nada.
echo "reporte de la vuelta anterior" > "$taller/docs/loop/REPORTE.md"
echo "[hora] log de la vuelta anterior" > "$taller/docs/loop/loop.log"
echo '{"result": "mensaje final del extractor anterior"}' > "$taller/docs/loop/ultimo_extractor.json"
echo '{"result": "mensaje final del auditor anterior"}' > "$taller/docs/loop/ultimo_auditor.json"
git -C "$taller" add -A >/dev/null 2>&1
git -C "$taller" commit -q -m "los cuatro artefactos de la vuelta anterior" >/dev/null 2>&1
salida="$(correr "$taller")"
echo "$salida" | sed 's/^/  | /'
comprobar "la fase ciega corre y lo dice"    "APERTURA CIEGA"              "$salida"
comprobar "dice que retira los CUATRO"       "retirados: REPORTE.md loop.log ultimo_extractor.json ultimo_auditor.json" "$salida"
comprobar "sella la apertura"                "apertura ciega sellada"      "$salida"
comprobar "y verifica el sello despues"      "sello de la apertura ciega verificado" "$salida"
comprobar "el auditor corre DESPUES"         "VUELTA 1 : AUDITOR"          "$salida"

# LA COMPROBACION QUE IMPORTA: el auditor ciego FUE A POR LOS CUATRO y no
# encontro ninguno. No basta con que el arnes diga que los retira.
apertura="$(cat "$taller/docs/loop/APERTURA_CIEGA.md" 2>/dev/null || echo AUSENTE)"
comprobar "el ciego no encontro el reporte"  "ausentes: REPORTE.md"        "$apertura"
comprobar "ni el log del arnes"              "loop.log"                    "$apertura"
comprobar "ni el testigo del extractor"      "ultimo_extractor.json"       "$apertura"
comprobar "ni el testigo del auditor"        "ultimo_auditor.json"         "$apertura"
comprobar_no "NINGUNO de los cuatro estaba"  "ENCONTRADO_"                 "$apertura"
comprobar_no "y la apertura ciega no se rompio" "APERTURA CIEGA ROTA"      "$salida"

# Y LOS CUATRO VUELVEN a su sitio para el turno normal.
for fichero in REPORTE.md loop.log ultimo_extractor.json ultimo_auditor.json; do
  [ -f "$taller/docs/loop/$fichero" ] \
    && { echo "    VERDE  $fichero vuelve a su sitio tras sellar"; verdes=$((verdes+1)); } \
    || { echo "    ROJO   $fichero no volvio"; rojos=$((rojos+1)); }
done

# Y LA VENTANA CIEGA NO SE PIERDE DEL REGISTRO por haber ocurrido con el log
# fuera: sus lineas se anexan al de verdad cuando vuelve.
comprobar "el log recupera la ventana ciega" "APERTURA CIEGA" \
  "$(cat "$taller/docs/loop/loop.log" 2>/dev/null || echo AUSENTE)"

sellos="$(cat "$taller/docs/loop/SELLOS_APERTURA.jsonl" 2>/dev/null || echo AUSENTE)"
comprobar "el sello queda en su registro"    '"vuelta": 1'                 "$sellos"

# CASO POSITIVO DEL SELLO: un auditor que reescribe su apertura DESPUES de ver
# el reporte es exactamente la averia que el sello existe para cazar.
echo ""
echo "ESCENARIO 13b: EL CASO POSITIVO DEL SELLO. El auditor reescribe su"
echo "               apertura ciega DESPUES de ver el reporte."
taller="$(montar_banco e13b)"
salida="$(FALSO_ROMPE_SELLO=si correr "$taller")"
echo "$salida" | sed 's/^/  | /'
comprobar "el sello roto se caza"            "SELLO ROTO"                  "$salida"
comprobar "dice las dos huellas"             "Sellado "                    "$salida"
comprobar "detiene la corrida"               "DETENIDO en la vuelta 1"     "$salida"
comprobar "y escribe la parada"              "PARA_ALEXIS.md"              "$salida"

# --------------------------------------------------------------- escenario 14
echo ""
echo "ESCENARIO 14: LA HERENCIA LA ENTREGA EL ARNES (D.40). Tres actas seguidas"
echo "              perdieron el mismo remedio por tener que ir a buscarlo en un"
echo "              fichero de dieciseis mil lineas. Ahora el arnes lo extrae del"
echo "              acta anterior, lo antepone al prompt, y EXIGE que se declare."
taller="$(montar_banco e14)"
salida="$(correr "$taller")"
echo "$salida" | sed 's/^/  | /'
comprobar "dice cuantos hereda"              "hereda 1 remedio(s) del acta anterior" "$salida"
comprobar "y que los entrega el prompt"      "entregados en el prompt (D.40)" "$salida"
comprobar "la herencia queda declarada"      "herencia declarada"           "$salida"
comprobar "y la vuelta cierra"               "Arnes terminado"              "$salida"

# LA HERENCIA LLEGO DE VERDAD AL PROMPT, no solo al log.
prompt="$(cat "$taller/prompt_auditor_ciego.txt" 2>/dev/null || echo SIN_PROMPT)"
comprobar "el prompt trae el titulo"         "REMEDIOS PENDIENTES QUE HEREDAS" "$prompt"
comprobar "y el texto del remedio heredado"  "TAREA BLOQUEANTE DEL AUDITOR DE LA VUELTA 2" "$prompt"
comprobar "y dice que el acta SI se abre"    "ACTA_AUDITOR.md SI ESTA Y SI PUEDES ABRIRLO" "$prompt"

# --------------------------------------------------------------- escenario 14b
echo ""
echo "ESCENARIO 14b: EL CASO POSITIVO. Una apertura ciega SIN la linea de"
echo "               lectura se caza, y el arnes se detiene ANTES de que se"
echo "               escriba el acta. Sin este, el 14 solo probaria que el"
echo "               prompt lleva texto."
taller="$(montar_banco e14b)"
salida="$(FALSO_HERENCIA=no correr "$taller")"
echo "$salida" | sed 's/^/  | /'
comprobar "la caza"                          "APERTURA CIEGA INCOMPLETA"    "$salida"
comprobar "se detiene ANTES del acta"        "ANTES de que se escriba el acta" "$salida"
comprobar "nombra la linea que falta"        "ACTA ANTERIOR LEIDA"          "$salida"
comprobar "y el heredado sin declarar"       "HEREDADO 1"                   "$salida"
comprobar "detiene la corrida"               "DETENIDO en la vuelta 1"      "$salida"
comprobar_no "el auditor NO llega a correr"  "VUELTA 1 : AUDITOR"           "$salida"
# Y LOS CUATRO FICHEROS VUELVEN: una parada no deja el arbol a medias.
[ -f "$taller/docs/loop/REPORTE.md" ]   && { echo "    VERDE  el reporte vuelve a su sitio aun deteniendose"; verdes=$((verdes+1)); }   || { echo "    ROJO   el reporte no volvio tras la parada"; rojos=$((rojos+1)); }

echo ""
echo "================================================================"
echo "RESULTADO: $verdes comprobaciones en VERDE, $rojos en ROJO"
echo "================================================================"
[ "$rojos" -eq 0 ] || exit 1
