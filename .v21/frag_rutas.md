
**LA TABLA SE CUENTA AL FINAL DE TODO, y esa es la unica parte del remedio que la vuelta 20 no
tenia.** Cada fila lleva su comando y su salida **corridos ahora**, con el arbol ya quieto.

| ruta | comando que la cuenta | su salida, ahora |
|---|---|---:|
| `.aduana_v21/` (raiz) | `ls .aduana_v21/*.txt \| wc -l` | **16** |
| `.aduana_v21/final/` | `ls .aduana_v21/final/*.txt \| wc -l` | **13** |
| los dictamenes de `final/` | `cat .aduana_v21/final/*.txt \| grep -cE "^\["` | **13** |
| los dictamenes de la raiz | `cat .aduana_v21/*.txt \| grep -cE "^\["` | **14** |
| `.aduana_v21/sellos_candidatos.txt` | `wc -l < .aduana_v21/sellos_candidatos.txt` | **13** |
| `.aduana_v21/arista_intento_1.txt` | `grep -c "RECHAZADO" .aduana_v21/arista_intento_1.txt` | **1** |
| `.t1_v21/` guiones | `ls .t1_v21/*.py \| wc -l` | **9** |
| `.t1_v21/` salidas guardadas | `ls .t1_v21/*.txt \| wc -l` | **13** |
| `.v21/` fragmentos del reporte | `ls .v21/*.md \| wc -l` | **14** |

**LOS NUEVE GUIONES DE `.t1_v21/`, LOS NUEVE CITADOS POR SU NOMBRE EN ESTE REPORTE, Y NINGUNO SIN
CITAR:** `frontera21.py` (`O.3.b`), `cifras21.py` (`O.3.d`), `cuentas21.py` (`O.3.d`),
`arreglo_cuentas.py` (`O.3.d`), `puentes21.py` (`O.3.e`), `muestra21.py` (`O.3.f`), `par_lupa.py`
(`O.5.b`), `reparto21.py` (`O.6.3`), `saldo21.py` (`O.6.2`).

    $ ls .t1_v21/*.py | wc -l
      9

> ### **NUEVE GUIONES, NUEVE CITADOS, CERO SIN CITAR.** Es exactamente la fila que me costo la caida
> de especie `REPORTE` en la vuelta 20 (`ACTA 20` `1.5`: decia `13` donde habia `16`, y citaba nueve
> de once). **La cuento al cierre y la cuadro a cero para que no haya nada que descubrir.**

**Y LA DIFERENCIA ENTRE EL `16` Y EL `13`, EXPLICADA FICHERO A FICHERO, porque dos cifras distintas
para la misma clase de cosa invitan a sospechar:**

    $ ls .aduana_v21/*.txt | sed 's|.*/||'
      01_conversar_historia_vida.txt        ...        13_reconocer_excelencia.txt
      07b_admitir_pronto_corregido.txt
      arista_intento_1.txt
      sellos_candidatos.txt

**Los `16` de la raiz son: los `13` de la primera pasada, mas `07b` (el reintento del id que cayo),
mas `arista_intento_1.txt` (que NO es un informe de candidato: es el rechazo de `forja.py arista`),
mas `sellos_candidatos.txt` (que NO es un informe: es la lista de `git hash-object`).** De ahi que
los dictamenes de la raiz sean **14** y no 16: **13 de la primera pasada mas el reintento**. Y los
`13` de `final/` son **los del estado final del fichero**, uno por candidato, que son los que la
tabla de `O.6.2` cita.
