# DICTAMEN DEL 13 SEP 2026: **ESPECIE `CREDITO`.** LA RUTA VACIA QUE SOSTENIA UNA CIFRA

*Escrito siguiendo el guion de reanudacion del fundador del 13 sep 2026, punto 3.*

> ### **ESTO NO ES UNA DECISION DEL FUNDADOR. ES UN DICTAMEN Y UNA CURA PARCIAL.**
>
> Los demas ficheros de esta carpeta archivan decisiones firmadas. **Este no**: la
> decision que esta parada necesita **sigue pendiente**, y esta escrita como propuesta
> en el anexo `A.4` de `docs/loop/PARA_ALEXIS.md`, que **sigue existiendo y sigue
> deteniendo el bucle.**

---

## 1. LA ESPECIE, Y POR QUE ESA Y NO OTRA

**`CREDITO`.** Racha `REPORTE` del extractor en **3 de 3** (`AUDITOR_FORJA.md` `3`).

**NO ES `ARNES`:** el arnes corrio tres vueltas enteras sin un solo defecto propio, el
grafo paso de `203` a `222` nodos, la insercion del lote 4 arranco, y las cinco guardas
cerraron en verde. **Y la medida del rol inicial que arregle esta manana funciono:** el
log la registra eligiendo `EXTRACTOR` con sus cuatro fechas pegadas.

**NO ES `DOCTRINA`:** la regla que se incumplio esta escrita y es literal (cosecha
`7.B`, `AUDITOR_FORJA.md` `5.5`): *una ruta publicada como evidencia de una corrida
cuenta como cifra publicada en su sede; si apunta a un fichero inexistente o de cero
bytes, es caida de cifra.*

## 2. LA CAIDA

La vuelta 25 publico en `S.10` la cifra **`2`** con sede `.v25/cola_lectura.txt`, y:

    $ ls -la .v25/cola_lectura.txt
      -rw-r--r-- 1 AlexDesk 197609 0 Sep 13 18:30 .v25/cola_lectura.txt
                                   ^ CERO BYTES
    $ python forja.py informe cuarentena/.../decidir_momento_despedir_persona.json
      vecinos levantados en total : 4     con veredicto ya escrito : 0

**La cifra es `4` y la sede que la probaba no probaba nada.**

## 3. LO QUE CURE: UN HUECO MIO DENTRO DE `D.41`

**`D.41` tenia que haber cazado esto en el commit y daba VERDE.** El tallador leia el
fichero vacio sin error, no encontraba tabla dentro, y lo despachaba con la lectura mas
generosa posible: *el instrumento no imprime ninguna tabla: esta la resume, no la
reproduce.*

| antes | ahora |
|---|---|
| salida de cero bytes, `SIN COMPROBAR`, **verde** | salida de cero bytes, **`RUTA VACIA`, ROJO**, y nombra la ruta |

**CON SU CASO NEGATIVO, porque la distincion tiene que aguantar:** una salida **con
contenido pero sin tabla** sigue siendo `SIN COMPROBAR` y no tumba nada. Un instrumento
que imprime un saldo y no una tabla esta cumpliendo. **Tres pruebas nuevas**, y
`PruebaTallado` pasa de 13 a 16.

> **ESE HUECO LO ABRI YO ESTA MISMA MANANA AL ESCRIBIR `D.41`.** Queda cerrado y no
> depende de ninguna decision.

## 4. Y POR QUE ESO **NO** CURA LA PARADA

**La caida tiene otra forma.** `D.41` ata **un instrumento a una tabla entera**. La
tabla de `S.10` no declara nada encima: **publica una ruta POR FILA**, en su tercera
columna, titulada *de donde sale*. **La unidad de `D.41` es la tabla; aqui la unidad es
la celda**, y por eso la caida no esta ni podria estar entre las **55 tablas declaradas
y 41 talladas** que el instrumento revisa hoy.

## 5. LA CURA QUE FALTA ES DEL FUNDADOR, Y LA MEDIDA DICE POR QUE

Corri el censo de rutas sobre el reporte **antes** de proponerlo:

| | |
|---|---:|
| rutas distintas publicadas | **234** |
| existen y tienen contenido | **147** |
| **existen y estan VACIAS** | # **3** |
| no existen en el arbol | **84** |

**De las tres vacias, solo una es la caida.** Las otras dos estan vacias **a proposito y
por regla**: `docs/loop/PROMPT_SIGUIENTE.md` porque `AUDITOR_FORJA.md` `3` manda dejarlo
vacio en una parada, y `.barrido_C_con_ensayo_v16.txt` porque la `ACTA 15` `1.9` ya lo
adjudico. **Y de las 84 que no existen, la mayoria no son rutas: son PATRONES**
(`.aduana_v22/*.txt`, `.frag_*.md`).

> ### **`7.B` APLICADA AL PIE DE LA LETRA HOY DISPARARIA TRES VECES Y ACERTARIA UNA.**

Eso no se arregla escribiendo mejor el codigo: **se arregla decidiendo dos cosas que son
del fundador** (como se declara una ruta vacia a proposito, y que hace el censo con un
patron), y son exactamente las que el auditor nombro en su `5.1`. **Estan propuestas en
`PARA_ALEXIS.md` `A.4` y ahi se quedan.**

## 6. LO QUE NO HICE

- **NO reinicie la racha.** Sigue en **3 de 3**. `5.4`: la reinicia una tanda limpia o
  una decision escrita del fundador, y **ninguna de las dos soy yo.**
- **NO relance el arnes.** El guion solo autoriza relanzar en la especie `ARNES`.
- **NO impuse el censo de rutas**, que es la condicion que esta decision necesita.
- **NO toque el texto del auditor** en `PARA_ALEXIS.md`: solo anadi el anexo que el
  guion pide, rotulado con quien lo escribe.

## 7. ESTADO

    rama            : extraccion-mundo-11
    PARA_ALEXIS.md  : EXISTE. El bucle sigue detenido, y es correcto
    nodos           : 222        bitacora : 203 lineas
    racha REPORTE   : 3 de 3     racha del auditor : 2 de 3

    python forja.py gate                 GATE VERDE, 222 nodos
    python forja.py guiones              VERDE
    python scripts/tallar_reporte.py     VERDE, 55 declaradas, 41 talladas, 0 difieren
    python tests/test_aceptacion.py      114 pruebas, 0 fallos
    bash tests/prueba_arnes.sh           128 comprobaciones en VERDE
