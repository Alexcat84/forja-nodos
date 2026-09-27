
## 2.f. EL SALDO DEL LOTE ENTERO, CORRIDO AL CERRAR EL CAPITULO

*`EXTRACTOR.md` 16: **el informe de lote se hace igual, al cerrar el capitulo**, y los dos no se
pisan: el de candidato es mi correccion, el de lote es la prueba que lee el fundador. **Esta
corrida me lo devuelve al turno**, porque el arnes no le sello ninguno a este frente
(`docs/loop/PROMPT_SIGUIENTE.md` no entrega `INFORME_DE_LOTE.txt`), y lo declaro asi en la
apertura.*

**Y ES LA UNICA CIFRA QUE UN INFORME DE UNO EN UNO NO PUEDE VER:** `CHOCAN entre si dentro del
lote`. Los nueve informes de candidato de esta vuelta dan cada uno su propio `CHOCAN` en `0`, pero
**cada uno se mide contra los demas de a uno**; el del lote los cruza a todos a la vez.

`python forja.py informe --carpeta cuarentena/marquet_turn_the_ship`, guardada en
`.vm01/informe_lote.txt`.

<!-- TALLADO: parcial salida=.vm01/informe_lote.txt -->

@@SALDO_LOTE@@

@@NOTA_LOTE@@

### 2.f.1. LAS DOS CORRECCIONES DE `cap_02` VUELTAS A PASAR POR LA ADUANA

*Las dos son correcciones declaradas de frontera (`3.d`), y ninguna es de esta unidad; pero
`EXTRACTOR.md` 16 no distingue: **un candidato tocado vuelve a la puerta.***

<!-- TALLADO: parcial salida=.vm01/aduana/c0_encargar_meta_especifica_dejar_libre_metodo.txt -->

| candidato | que se le corrigio | veredicto en seco tras corregir | fichero |
|---|---|---|---|
| `encargar_meta_especifica_dejar_libre_metodo` | declarada `L51` en su frontera (`3.d.1`) | **@@VER_C0@@** | `.vm01/aduana/c0_encargar_meta_especifica_dejar_libre_metodo.txt` |
| `cambiar_forma_trabajar_conservar_plantilla` | declarada `L27` en su frontera (`3.d.2`), hallazgo del auditor ciego | **@@VER_C00@@** | `.vm01/aduana/c00_cambiar_forma_trabajar_conservar_plantilla.txt` |

**LAS DOS SIGUEN EN VERDE DE ADUANA, Y ESO ERA LO ESPERADO:** lo que se les cambio es el
`resumen_teorico`, que es texto y no estructura. **La aduana no vio la frontera corrida ni antes ni
despues**, que es exactamente lo que `D.30` dice de ella: **mide otra cosa.**

### 2.f.2. LOS DOS INFORMES QUE SALIERON A CERO BYTES, Y LO QUE ESO DICE DEL PARALELO

**Dos de las corridas de esta vuelta terminaron con codigo `1` y la salida VACIA**, cero bytes, sin
una linea de error: las primeras relanzadas de
`auditar_formacion_premios_ultima_fila` y de `encargar_meta_especifica_dejar_libre_metodo`.
**Relanzadas por segunda vez, las dos dieron su informe normal**, que es el que esta pegado arriba.

| | |
|---|---|
| que hice | **relanzarlas y decirlo**, no dar por buena una salida vacia |
| que NO hice | contar ese `0` como `0 CAERIA`. **Una salida vacia no es un verde: es una medicion que no ocurrio** |
| cuando paso | con el arbol lleno: conte **`28` y luego `70` procesos de Python a la vez**, porque el auditor ciego estaba corriendo sus propios informes sobre la misma bandeja |
| por que lo escribo | porque es la primera vez que este repo corre **dos sesiones a la vez sobre el mismo arbol** (`D.45`), y **el primer efecto medido del paralelo no es una discrepancia de lectura: es una medicion que se cae sin avisar** |

**VA COMO PROPUESTA `2` EN `C.8`**, junto con el reloj de la aduana, porque las dos cosas son la
misma: **el instrumento mas caro de la casa corriendo dos veces sobre el mismo arbol.**
