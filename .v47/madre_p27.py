# -*- coding: utf-8 -*-
"""LA ARISTA D.29 DE P27, ESCRITA TAMBIEN EN LA FICHA DE LA MADRE (encargo 2.c).

La madre `transmitir_objetivos_prioridades_preferencias` ya declaro esta arista en la
vuelta 46, pero apuntando al hijo POR SU TRAMO (el nodo de la delegacion, de L243 a
L249), porque el hijo aun no estaba escrito. Hoy el hijo existe y tiene nombre.

CORRECCION DECLARADA: se ANADE al final del resumen_teorico y NO se borra nada, que es
lo que manda el manual principio 6 y lo que hace src/correccion.py con los nodos ya
insertados. Esta ficha esta en CUARENTENA, asi que la correccion se escribe aqui y la
ficha vuelve a pasar la aduana en el mismo acto (EXTRACTOR.md 16).
"""
import io
import json

RUTA = "cuarentena/grove_high_output/transmitir_objetivos_prioridades_preferencias.json"

ANADIDO = (
    " CORRECCION DECLARADA EN LA VUELTA 47, SIN BORRAR NADA DE LO DE ARRIBA (encargo de la"
    " vuelta 47, TAREA 2.c): la arista D.29 que este nodo declaro en la vuelta 46 apuntaba a"
    " su hijo POR SU TRAMO, el nodo de la delegacion de L243 a L249, porque en aquel momento"
    " el hijo no estaba escrito y no tenia nombre que citar."
    " EL HIJO SE ESCRIBIO EN LA VUELTA 47 Y SE LLAMA delegar_tarea_base_comun_seguimiento."
    " La arista queda declarada en las DOS fichas y con el paso citado en las dos: el paso 5 de"
    " esta madre dice que transmitir los objetivos y los modos preferidos es la llave de una"
    " delegacion que salga bien, y el hijo despliega esa delegacion en diez pasos que esta madre"
    " no tiene. Se cablea con python forja.py arista el dia en que el lote 7 cierre y se inserte,"
    " y no hoy, porque la puerta de D.39 mide CERRADA."
)

d = json.load(io.open(RUTA, encoding="utf-8"))
if "CORRECCION DECLARADA EN LA VUELTA 47" in d["resumen_teorico"]:
    print("YA ESTABA: no se escribe dos veces.")
else:
    d["resumen_teorico"] = d["resumen_teorico"] + ANADIDO
    io.open(RUTA, "w", encoding="utf-8", newline="\n").write(
        json.dumps(d, ensure_ascii=False, indent=2) + "\n")
    print("escrito")
print("pasos de la ficha: %d" % len(d["pasos_accionables"]))
