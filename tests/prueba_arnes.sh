#!/usr/bin/env bash
# PRUEBA DEL ARNES DEL EXTRACTOR, corrida FUERA del repo forja-nodos.
#
# Monta un repo de usar y tirar con su remoto bare, mete dentro
# orquestador_forja.sh y un CLAUDE FALSO cuyo comportamiento se dicta por
# variables de entorno, y corre seis escenarios. Ninguno toca el repo de verdad.
#
# El claude falso es la unica forma de probar el arnes: un turno mudo o un fallo
# instantaneo no se pueden pedir a un modelo de verdad, y una guarda que no se
# puede probar no guarda nada (manual seccion 2).
set -uo pipefail

ORQUESTADOR="$1"
BANCO="$(mktemp -d)"
trap 'rm -rf "$BANCO"' EXIT

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
  echo "encargo de prueba del arnes" > "$taller/docs/loop/PROMPT_SIGUIENTE.md"

  # EL CLAUDE FALSO. Distingue el rol por el documento que el prompt nombra.
  cat > "$taller/bin/claude" <<'FALSO'
#!/usr/bin/env bash
prompt="${!#}"
if echo "$prompt" | grep -q "EXTRACTOR.md"; then
  rol=extractor; testigo="docs/loop/REPORTE.md"; escribe="${FALSO_EXTRACTOR:-si}"
else
  rol=auditor;   testigo="docs/loop/ACTA_AUDITOR.md"; escribe="${FALSO_AUDITOR:-si}"
fi
sleep "${FALSO_SEGUNDOS:-2}"
if [ "$escribe" = "si" ]; then
  echo "linea del $rol, $(date '+%H:%M:%S.%N')" >> "$testigo"
  git add -A >/dev/null 2>&1
  git commit -q -m "turno del $rol (claude falso)" >/dev/null 2>&1
  git push -q origin bucle >/dev/null 2>&1
fi
echo "{\"total_cost_usd\": ${FALSO_COSTO:-0.42}, \"result\": \"turno del $rol\"}"
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
      CLAUDE_BIN="$1/bin/claude" RAMA=bucle \
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

echo ""
echo "================================================================"
echo "RESULTADO: $verdes comprobaciones en VERDE, $rojos en ROJO"
echo "================================================================"
[ "$rojos" -eq 0 ] || exit 1
