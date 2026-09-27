# -*- coding: utf-8 -*-
import io
p = 'docs/loop/REPORTE.md'
s = io.open(p, encoding='utf-8').read()

PARES = [
 ("Y 1 puente cazado y corregido en el acto** de 40 cifras barridas (`O.3.e`) |",
  "Y 1 puente cazado y corregido en el acto**, de **41** cifras y numerales barridos en la "
  "primera corrida y **40 en la segunda, con 0 fallos** (`O.3.e`) |"),
 ("| **5** | **`P27` de `cap_09` como UN nodo de 31 pasos**, el mas grande del lote 4 por "
  "numero de pasos |",
  "| **5** | **`P27` de `cap_09` como UN nodo de 31 pasos**, el mas grande del lote 4 por "
  "numero de pasos, **y medido y no supuesto**: `$ python .t1_v20/maxpasos.py` da "
  "`31 conducir_reuniones_salto_nivel_diez_reglas`, "
  "`22 entregar_evaluacion_formal_desempenio_nueve_consejos`, "
  "`20 abrazar_incomodidad_arrancar_critica_equipo`. **Los dos nodos mas grandes de los 83 "
  "del lote son los dos mios de hoy**, y eso solo es inocente si mi corte es el mismo que el "
  "de las cuatro vueltas anteriores |"),
]
for a, b in PARES:
    n = s.count(a)
    print(n, repr(a[:60]))
    assert n == 1, n
    s = s.replace(a, b)
io.open(p, 'w', encoding='utf-8').write(s)
print('arreglado')
