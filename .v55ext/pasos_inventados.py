# -*- coding: utf-8 -*-
"""PASOS INVENTADOS POR CAPITULO, UNA FILA POR CAPITULO Y NO UNA MEDIA (D.59, TAREA 4).

Mismo instrumento que la vuelta 53 (.v53/pasos_inventados.py) con MI marca dentro, y con UNA
pieza mas que aquel no tenia y que esta vuelta si necesita: **la marca TRANSCRIPCION no se
promete, se comprueba**. Para cada paso de la muestra escribo el fragmento del libro del que
sale, y el instrumento LO BUSCA en el fichero del capitulo y publica la linea en la que lo
encuentra. Es el remedio mecanico de D.35 aplicado a la relectura de D.30: un paso cuyo
fragmento no aparezca en el fichero **no puede marcarse TRANSCRIPCION**, y el instrumento lo
declara PUENTE por su cuenta, sin que yo pueda salvarlo.

CERO CIFRAS TECLEADAS: el numero de pasos de cada candidato se cuenta del JSON, la lista de la
muestra se lee de .v55ext/muestra.txt, que es la salida del instrumento que la repartio, y la
linea de cada fragmento la encuentra la busqueda.
"""
import io
import json
import os
import re
import sys
import unicodedata

if hasattr(sys.stdout, "buffer"):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", newline="\n")

TOPE = 10.0
LIBRO = "grove_high_output"


def llana(texto):
    texto = texto.replace(chr(0x2014), "-").replace(chr(0x2013), "-")
    texto = texto.replace(chr(0x2018), "'").replace(chr(0x2019), "'")
    texto = texto.replace(chr(0x201C), '"').replace(chr(0x201D), '"')
    texto = texto.replace(chr(0x2026), "...")
    return "".join(c for c in unicodedata.normalize("NFD", texto)
                   if unicodedata.category(c) != "Mn")


# MI MARCA, paso a paso: el fragmento del libro del que sale ese paso. La clave es
# (id recortado como lo imprime la muestra, P<n>). El instrumento busca el fragmento.
FRAGMENTOS = {
    "cap_07": {
        ("cerrar_brecha_dos_preguntas_estrategia", 1):
            "The final step of planning consists of undertaking new tasks or modifying old ones",
        ("cerrar_brecha_dos_preguntas_estrategia", 2):
            "The first question is, What do you need to do to close the gap?",
        ("contestar_dos_preguntas_direccion_objetivos", 3):
            "The answer provides the objective",
        ("contestar_dos_preguntas_direccion_objetivos", 4):
            "How will I pace myself to see if I am getting there?",
        ("definir_entorno_grupo_clientes_proveedores_com", 4):
            "vendors who are able to provide you with certain capabilities",
        ("examinar_demanda_entorno_dos_marcos_temporales", 2):
            "What do my customers want from me now?",
        ("examinar_demanda_entorno_dos_marcos_temporales", 5):
            "You need to focus on the difference between what your environment demands from you now",
        ("fijar_horizonte_ventana_replanificacion", 1):
            "But what is really being influenced here? It is the next year",
        ("fijar_horizonte_ventana_replanificacion", 2):
            "you implement only that portion of a plan that lies within the time window",
        ("fijar_horizonte_ventana_replanificacion", 3):
            "Everything else you can look at again",
        ("fijar_periodo_direccion_objetivos_retroaliment", 5):
            "if we plan on a yearly basis, the corresponding MBO system",
        ("planificar_tres_pasos_demanda_estado_brecha", 1):
            "Your general planning process should consist of analogous thinking",
        ("planificar_tres_pasos_demanda_estado_brecha", 2):
            "Step 1 is to establish projected need or demand",
        ("planificar_tres_pasos_demanda_estado_brecha", 4):
            "where will your business be if you do nothing different from what you are now doing?",
        ("planificar_tres_pasos_demanda_estado_brecha", 6):
            "what more (or less) do you need to do to produce what your environment will demand?",
    },
    "cap_09": {},
    "cap_10": {
        ("repartir_supervision_puesto_funcional_mision", 1):
            "you need a way to coordinate the mission-oriented units and the functional groups",
        ("repartir_supervision_puesto_funcional_mision", 2):
            "His professional methods, practices, and standards are set by the functional group",
        ("repartir_supervision_puesto_funcional_mision", 3):
            "should report to someone in both the functional and the mission-oriented organizations",
        ("repartir_supervision_puesto_funcional_mision", 4):
            "with the type of supervision reflecting the varying needs of the two",
        ("repartir_supervision_puesto_funcional_mision", 5):
            "gives the controller mission-oriented priorities by asking him to work on specific business problems",
        ("repartir_supervision_puesto_funcional_mision", 6):
            "makes sure that the controller is trained to do his work in a technically proficient manner",
        ("repartir_supervision_puesto_funcional_mision", 7):
            "supervises and monitors his technical performance",
        ("repartir_supervision_puesto_funcional_mision", 8):
            "looks after his career inside finance, promoting him",
    },
}
REGIMEN = {"cap_07": "MUESTRA de 15", "cap_09": "ENTERO", "cap_10": "ENTERO, 8 de 8"}

# LOS CANDIDATOS DE CADA CAPITULO SE CUENTAN DE LA BANDEJA, no se teclean.
CANDIDATOS = {}
carpeta = os.path.join("cuarentena", LIBRO)
for nombre in sorted(os.listdir(carpeta)):
    if not nombre.endswith(".json"):
        continue
    crudo = io.open(os.path.join(carpeta, nombre), encoding="utf-8").read()
    m = re.search(r"cap_(\d+)\.md", crudo)
    if not m:
        continue
    cap = "cap_%s" % m.group(1)
    if cap in REGIMEN:
        CANDIDATOS.setdefault(cap, []).append(nombre[:-5])

# LA MUESTRA SE COTEJA CONTRA EL FICHERO QUE LA REPARTIO, no contra mi memoria.
crudo = io.open(".v55ext/muestra.txt", encoding="utf-8").read()
fila = re.compile(r"^    (\S+)\s+P(\d+)\s", re.M)
de_la_salida = sorted((m.group(1), int(m.group(2))) for m in fila.finditer(crudo))
mias = sorted(k for cap in FRAGMENTOS for k in FRAGMENTOS[cap])
print("    pasos que la muestra reparte (leidos de .v55ext/muestra.txt) : %d" % len(de_la_salida))
print("    pasos que yo declaro releidos                                : %d" % len(mias))
print("    LAS DOS LISTAS COINCIDEN, paso a paso                        : %s"
      % (de_la_salida == mias))
print("")

print("=" * 78)
print("LA RELECTURA, PASO A PASO: EL FRAGMENTO SE BUSCA EN EL FICHERO DEL CAPITULO")
print("=" * 78)
print("| capitulo, candidato y paso | marca | linea del libro donde el instrumento lo encuentra |")
print("|---|---|---|")
PUENTES = {}
for cap in sorted(FRAGMENTOS):
    if not FRAGMENTOS[cap]:
        continue
    lineas = io.open("fuentes/%s/%s.md" % (LIBRO, cap), encoding="utf-8").read().split("\n")
    planas = [llana(l) for l in lineas]
    for (corto, n) in sorted(FRAGMENTOS[cap]):
        frag = llana(FRAGMENTOS[cap][(corto, n)])
        donde = [i for i, l in enumerate(planas, 1) if frag in l]
        if donde:
            marca = "TRANSCRIPCION"
            sede = "`L%d`: `%s`" % (donde[0], frag[:72])
        else:
            marca = "**PUENTE**"
            sede = "**el fragmento NO esta en el fichero**"
            PUENTES.setdefault(cap, []).append((corto, n))
        print("| `%s` `%s` P%d | %s | %s |" % (cap, corto, n, marca, sede))
print("")

print("=" * 78)
print("PASOS INVENTADOS POR CAPITULO (D.59): UNA FILA POR CAPITULO, NO UNA MEDIA")
print("=" * 78)
print("| capitulo | candidatos | pasos escritos | regimen `D.58` | pasos releidos | PUENTE | `PASOS INVENTADOS` |")
print("|---|---:|---:|---|---:|---:|---:|")
for cap in sorted(REGIMEN):
    ids = CANDIDATOS.get(cap, [])
    pasos = 0
    for i in ids:
        ruta = os.path.join(carpeta, "%s.json" % i)
        pasos += len(json.load(io.open(ruta, encoding="utf-8"))["pasos_accionables"])
    releidos = len(FRAGMENTOS[cap])
    puentes = len(PUENTES.get(cap, []))
    por_ciento = (100.0 * puentes / releidos) if releidos else 0.0
    print("| `%s` | %d | %d | %s | %d | **%d** | **%s por ciento, %d de %d** |"
          % (cap, len(ids), pasos, REGIMEN[cap], releidos, puentes,
             ("%.1f" % por_ciento).replace(".", ","), puentes, releidos))
print("")
print("    EL NUMERADOR ES `pasos marcados PUENTE` Y EL DENOMINADOR `pasos releidos`,")
print("    no los pasos escritos: la muestra de D.58 no relee todos los pasos del capitulo.")
print("")
for cap in sorted(REGIMEN):
    releidos = len(FRAGMENTOS[cap])
    puentes = len(PUENTES.get(cap, []))
    por_ciento = (100.0 * puentes / releidos) if releidos else 0.0
    if not releidos:
        estado = "SIN SUPERFICIE: 0 candidatos y 0 pasos, no hay que releer"
    elif por_ciento <= TOPE:
        estado = "NO DISPARA"
    else:
        estado = "DISPARA: RELEER ENTERO ANTES DE SEGUIR"
    print("    %-8s %6s por ciento contra un tope de %.0f : %s"
          % (cap, ("%.1f" % por_ciento).replace(".", ","), TOPE, estado))
print("")
total_p = sum(len(v) for v in PUENTES.values())
print("    LA CUARTA GUARDA DE DATO DE D.55, la fidelidad D.30 con puente: %d puente(s)." % total_p)
print("    %s" % ("EN VERDE." if total_p == 0 else "EN ROJO: %d puente(s)." % total_p))
