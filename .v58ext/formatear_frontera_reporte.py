# -*- coding: utf-8 -*-
"""Formatea .v58ext/frontera.txt al formato de REPORTE.md (bloques 'COMPROBACION' y
'EL TECHO' indentados como salida de comando, tablas markdown sueltas con su marca TALLADO
encima), replicando exactamente el patron que uso la vuelta 57. Cero texto inventado: es
un formateador mecanico del mismo fichero que ya paso la comprobacion suma==cuerpo.
"""
import io

lineas = io.open(".v58ext/frontera.txt", encoding="utf-8").read().split("\n")

out = []
out.append("## XX.2. TAREA 2. LA FRONTERA DE `cap_14`, `cap_15` Y `cap_16`, ANTES DE CORTAR NADA (`EXTRACTOR.md` 10)")
out.append("")
out.append("**Reuso `.v57ext/frontera.py` sin tocar su maquinaria de medir**, copiado a `.v58ext/frontera.py`")
out.append("(`EXTRACTOR.md` 13, la moratoria de maquinaria). **Lo unico que cambia es MI TABLA DE TRAMOS**")
out.append("sobre los tres capitulos de hoy. No retiro ninguna linea del bloque que imprime.")
out.append("")
out.append("**DOS PIEZAS SE ARMAN CON TRAMOS NO CONTIGUOS, y lo declaro aqui como manda `EXTRACTOR.md` 10:**")
out.append("")
out.append("1. **La pieza de las tres claves de `cap_14`** (entrega de la revision) se lee en `L107`, `L109`,")
out.append("   `L111`, `L113`, `L115` y `L119`, con `L117` (la analogia del profesor de aula) EXCLUIDA por ser")
out.append("   CASO.")
out.append("2. **La pieza de las etapas de resistencia de `cap_14`** se lee en `L167`, `L171` y `L179`, con")
out.append("   `L169` (pie de figura), `L173`, `L175` (otra taxonomia) y `L177` (CASO de Andy) EXCLUIDAS.")
out.append("")
out.append("**Y UNA REPETICION INTERNA SE DECLARA ANTES DE MINAR** (`P.19`): en `cap_15`, las cuatro")
out.append("categorias de informacion de entrevista (`L57`, `L59` a `L87`) reparten las MISMAS nueve preguntas")
out.append("ya dadas en `L39` a `L55`. El objeto ya esta en casa: esa fila no genera nodo propio.")
out.append("")

marcado = False
en_tabla = False
i = 0
primero = True
while i < len(lineas):
    l = lineas[i]
    if l.startswith("| tramo de") or l.startswith("|---"):
        if not en_tabla:
            out.append("<!-- TALLADO: salida=.v58ext/frontera.txt -->")
            out.append("")
            en_tabla = True
        out.append(l)
    elif l.startswith("| "):
        out.append(l)
    else:
        if en_tabla:
            out.append("")
            en_tabla = False
        if l.strip() == "":
            out.append("")
        else:
            prefijo = "    $ python .v58ext/frontera.py" if primero and l.startswith("====") else "    " + l
            if primero and l.startswith("===="):
                out.append("    $ python .v58ext/frontera.py")
                out.append("")
                primero = False
            out.append("    " + l)
    i += 1

out.append("")
out.append("**LAS TRES UNIDADES CIERRAN: cero lineas sin cubrir y cero solapes en `cap_14`, `cap_15` Y**")
out.append("**`cap_16`, cada una contra su propio cuerpo (`suma == cuerpo` en las tres).** Mi frontera preve")
out.append("`7` candidatos, dentro del techo de `30`.")

io.open(".v58ext/task2_seccion.md", "w", encoding="utf-8", newline="\n").write("\n".join(out))
print("escrito .v58ext/task2_seccion.md, %d lineas" % len(out))
