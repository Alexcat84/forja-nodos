# -*- coding: utf-8 -*-
"""Anexa las filas de HH.3 y HH.4 al reporte, con las tablas PEGADAS de su instrumento."""
import io

SAL = io.open(".v46/tanda_cap_04.txt", encoding="utf-8").read().split("\n")


def bloque(titulo):
    i = SAL.index(titulo)
    j = i + 2
    while j < len(SAL) and SAL[j].startswith("|"):
        j += 1
    k = j
    while k < len(SAL) and not SAL[k].startswith("="):
        k += 1
    return "\n".join(SAL[i + 2:j]), "\n".join(SAL[j:k]).strip("\n")


t1, _ = bloque("1. LA TANDA DE cap_04, CANDIDATO POR CANDIDATO")
t2, p2 = bloque("2. PASOS INVENTADOS DE cap_04 (D.30), CON SU DENOMINADOR")
t3, p3 = bloque("3. LA COLA DE LECTURA QUE ESTA TANDA ABRE, PAR A PAR")
p3s = "\n".join("    " + l for l in p3.split("\n") if l.strip())
p2s = "\n".join("    " + l for l in p2.split("\n") if l.strip())

TXT = u"""
## HH.3. TAREA 3. **`cap_04` MINADO: OCHO CANDIDATOS, CADA UNO POR SU ADUANA EN EL ACTO, CERO INSERCIONES**

**Un candidato por vez y en el orden del libro** (`EXTRACTOR.md` 12.3), **y cada uno pasa
`python forja.py informe <candidato>` en el mismo acto en que se escribe** (16). Los `8` informes
estan en `.v46/informe_01.txt` a `.v46/informe_08.txt` y sus relojes en `.v46/reloj_c01.txt` a
`.v46/reloj_c08.txt`.

**CERO INSERCIONES, Y NO POR FALTA DE PERMISO:** la corrida llega con `MODO_INSERCION=insertar`,
pero el lote 7 esta **ABIERTO** (`HH.0`), y `D.39` dice que los candidatos de un lote abierto se
quedan en cuarentena. **Meterlos antes es una caida de dato.**

<!-- TALLADO: script=.v46/tanda.py salida=.v46/tanda_cap_04.txt -->

%(t1)s

**`50` pasos escritos, `50` TRANSCRIPCION, `0` PUENTE, `13` pares de cola y `4.044` segundos de
aduana.** Ningun candidato `CAERIA`: **`2` entrarian sin leer nada y `6` bloquearian**, que no es
rechazo sino cola de lectura.

### HH.3.a. **LA COLA DE LECTURA, PAR A PAR, CON SUS TRES SENIALES**

<!-- TALLADO: script=.v46/tanda.py salida=.v46/tanda_cap_04.txt -->

%(t3)s

%(p3s)s

**LO QUE ESTA BANDA DICE, Y LO QUE NO** (`EXTRACTOR.md` 11, calibracion del 9 sep 2026 contra
`3.169` nodos):

- **`12` de los `13` pares caen entre `0,350` y `0,376`**, o sea pegados al umbral y **por debajo
  de `0,4`**. Es la figura del **capitulo monotematico** que `EXTRACTOR.md` 12 nombra por su
  nombre: *eso no es una senal de duplicado, es una senal de que el libro trata un tema*. `cap_04`
  entero trata de la palanca del mando. **La cola larga es el precio, no un fallo de la aduana, y
  lo que NO se hace es subir un umbral para que se acorte.**
- **`1` par pasa de `0,40` y se lee antes que ningun otro**, que es lo que la regla manda:
  `buscar_actividad_alta_palanca_tres_vias` contra `subir_productividad_gerencial_tres_vias`,
  **`0,437`**. **Mi lectura dice `CONTINUA` y no `REPITE`**, y la razon va escrita en las dos
  fichas **antes de que la senal hablara**: son **cabeza de serie y cabeza de subserie**, la
  segunda cuelga del paso `3` de la primera por `D.37`, y **lo que queda fuera es procedimiento en
  los dos lados** (manual seccion 4, *no tiene bascula*). **Y esto NO contradice la banda
  calibrada**: lo que la calibracion midio es que por encima de `0,4` no hay **ajenos**, y este par
  no es ajeno. Que la senal no sepa separar un gemelo de una jerarquia **ya estaba medido**
  (`D.19`), y por eso la jerarquia la busca la lectura.
- **Ninguna senal de familia levanta nada por si sola**: `familia_id` da `0,000` en `11` de los
  `13` pares. **Las `13` vecindades las levanta la similitud de texto, las `13`.**

**LOS VEREDICTOS NO SE ESCRIBEN HOY, Y ESO NO ES UN OLVIDO:** un veredicto vive en
`bitacora/VEREDICTOS.jsonl` y **lo escribe `forja.py insertar`** (`EXTRACTOR.md` 14). Sin
insercion no hay acto donde escribirlo, asi que **la cola queda publicada aqui, par a par, con su
lectura ya hecha**, y los veredictos y las aristas **se escriben el dia que el lote 7 cierre**.

### HH.3.b. **LAS ARISTAS DECLARADAS POR LECTURA, PARA CABLEARLAS EL DIA DE LA INSERCION**

Van escritas **dentro de la ficha de cada candidato**, que es donde sobreviven a este reporte:

| madre | hijo | regla | por que, en una linea |
|---|---|---|---|
| `reunir_informacion_gerencial_vias_variadas` | `escalonar_fuentes_informacion_gerencial` | `D.29` | el paso `7` de la madre prefiere la via verbal en **una linea**, y el hijo despliega los escalones y su solape en **siete pasos** que la madre no tiene |
| `transmitir_objetivos_prioridades_preferencias` | el nodo de la delegacion, de `L243` a `L249` | `D.29` | el paso `5` de la madre dice que transmitir objetivos es la llave de la delegacion, **y el hijo aun no esta escrito**: cae fuera del tramo de esta vuelta |
| `subir_productividad_gerencial_tres_vias` paso `3` | `buscar_actividad_alta_palanca_tres_vias` | **`D.37`** | el texto dice **cuantas** vias tiene y **las nombra**, y el paso `3` es literalmente la palanca |
| `subir_productividad_gerencial_tres_vias` paso `2` | los nodos del ritmo, de `L267` en adelante | **`D.37`** | misma serie, **y esos hijos caen fuera del tramo de esta vuelta** |
| `buscar_actividad_alta_palanca_tres_vias` | `elegir_momento_actividad_palanca_maxima` | `D.29` | el hijo despliega la primera via con su condicion de tiempo |

**Y LA TERCERA VIA DE LA SERIE NO TIENE HIJO, Y LO DIGO EN VEZ DE CALLARLO:** *correr la mezcla de
actividades* **el libro la numera y no la despliega en ningun tramo de `cap_04`**. Su arista queda
sin cablear porque **no hay parte que cablear**, no porque se me haya pasado.

| tarea | que pide | estado |
|---|---|---|
| `HH.3` | minar `cap_04`, cada candidato por su aduana, cero inserciones | **CERRADA EN `8` DE `22`**: `8` candidatos escritos y pasados por la aduana en el acto, `0` `CAERIA`, `13` pares de cola publicados par a par, **cero inserciones** y la razon medida del corte en `HH.5` |

## HH.4. TAREA 4. **`PASOS INVENTADOS` DE `cap_04`, CON SU DENOMINADOR ESCRITO**

**La relectura de fidelidad `D.30` se hizo EN EL ACTO de escribir cada candidato**, paso contra
parrafo, y la cifra de cada ficha vive dentro de su propio `resumen_teorico`, que es donde `D.30`
manda ponerla. **Esta tabla no la vuelve a juzgar: la cuenta de las ocho fichas, y se para si una
ficha declara mas pasos de los que tiene.**

<!-- TALLADO: script=.v46/tanda.py salida=.v46/tanda_cap_04.txt -->

%(t2)s

%(p2s)s

**EL DENOMINADOR VA ESCRITO AUNQUE EL NUMERADOR SEA CERO**, que es lo que el encargo pide tras
haber tenido que publicarse *sin denominador* en las tres filas de la `ACTA 44` `44.8`: **`0` de
`50`, el `0,00` por ciento, contra un tope de `10`.** No hay escalada que decidir, porque el peor
capitulo de esta vuelta es el unico y da cero.

**LOS TRES SITIOS DONDE ESTUVE A PUNTO DE ESCRIBIR UN PUENTE, dichos por su nombre**, porque una
cifra de cero no prueba que no hubiera tentacion:

| donde | la especie de `15.4` | que me paro |
|---|---|---|
| `programar_visita_area_observar_despachar` | **el periodo** | iba a escribir cada cuanto se visita. `L157` da **la duracion** de la visita (*spend an hour or so*) y **no da frecuencia**: escribi la hora y no la frecuencia |
| `elegir_momento_actividad_palanca_maxima` | **el periodo** | *a certain amount of time in advance*: el libro **no pone cifra**, asi que el paso dice *por delante del acontecimiento* y no cuanto |
| `transmitir_objetivos_prioridades_preferencias` | **el procedimiento de otro** | el renglon acaba remitiendo a la cultura de empresa con un *as we will see later*. **Escribir aqui sus pasos era fabricar el gemelo de su donante antes de que el donante exista** |

**Y EL AVISO DE `15.4` SE CUMPLIO AL REVES QUE EN EL LOTE 1:** los tramos que elegi son los que
traen inventario propio y denso, y **los `23` tramos que dan cero son justamente los pobres**. Un
parrafo pobre no produce un nodo pobre: **produce un nodo inventado**, y por eso no lo extraje.

| tarea | que pide | estado |
|---|---|---|
| `HH.4` | `PASOS INVENTADOS` de `cap_04` con su fila, su total y su denominador | **CERRADA**: `0` PUENTE de `50` pasos escritos, `0,00` por ciento contra un tope de `10`, contado de las ocho fichas por su instrumento |
""" % {"t1": t1, "t2": t2, "t3": t3, "p2s": p2s, "p3s": p3s}

with io.open("docs/loop/REPORTE.md", "a", encoding="utf-8", newline="\n") as f:
    f.write(TXT)
print("anexado")
