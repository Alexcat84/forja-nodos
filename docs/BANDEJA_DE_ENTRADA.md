# LA BANDEJA DE ENTRADA, LLENA Y VERIFICADA

**10 sep 2026, decision del fundador: se llena la bandeja entera de una vez**, los
mundos 10 y 11, en vez de traer un libro por lote. La vuelta 3 se habia detenido
por falta de material (`docs/loop/paradas/2026-09-10-falta-el-libro-del-lote-2.md`).

    fuentes/<clave>/cap_NN.md      164 capitulos, 557.501 palabras de cuerpo

**`fuentes/*/` sigue fuera de git** (texto con derechos de otro autor). Lo que
viaja es esta cuenta y `fuentes/FUENTES_CANONICAS.json`.

---

## 1. LA TABLA, LIBRO POR LIBRO

| clave | caps | rango | palabras | declara el recorte | cuadra | FRONTERA |
|---|---:|---|---:|---:|---|---|
| `onu_consumidor` | 4 | `cap_00..03` | 1.534 | 1.534 | **si** | **cap_01** |
| `smart_who` | 7 | `cap_01..07` | 44.133 | 44.133 | **si** | |
| `zhuo_manager` | 12 | `cap_01..12` | 70.041 | 70.041 | **si** | |
| `scott_radical_candor` | 15 | `cap_00..14` | 108.161 | 107.943 | 14 de 15 | |
| `marquet_turn_the_ship` | 17 | `cap_01..17` | 33.702 | 33.702 | **si** | |
| `openstax_business_ethics` | 17 | `cap_01..17` | 54.148 | 54.118 | 16 de 17 | |
| `grove_high_output` | 18 | `cap_01..18` | 64.372 | 64.372 | **si** | |
| `bernerslee_bananas` | 19 | `cap_01..19` | 21.509 | 21.631 | 17 de 19 | |
| `gerber_emyth` | 22 | `cap_01..22` | 62.648 | 62.648 | **si** | |
| `openstax_org_behavior` | 32 | `cap_01..32` | 93.408 | 93.152 | 27 de 32 | |
| `gerber_emyth_cap17_reservado` | 1 | `cap_17` | 3.845 | 3.845 | **si** | |
| **total** | **164** | | **557.501** | **557.119** | **155 de 164** | |

## 2. QUE PRUEBA CADA COLUMNA, PORQUE NO PRUEBAN LO MISMO

**LA COPIA SE PRUEBA POR HUELLA, NO POR RECUENTO.**

> **164 ficheros copiados, 164 huellas `sha256` identicas al origen, 0 distintas.**

**El recuento de palabras no comprueba la copia: comprueba el MANIFIESTO** del
mundo 11, que declara las palabras de cada fichero. Son dos verificaciones
distintas y la primera es la que importa para saber que se copio bien.

## 3. LOS DESCUADRES, EXPLICADOS Y NO ESCONDIDOS

**155 de 164 ficheros cuadran al alma. Los 9 que no, suman 382 palabras sobre
557.501: el 0,07 por ciento.** Y ninguno es un fallo de copia.

**PRIMERO HUBO 50 DESCUADRES, Y ERAN DE METODO.** Todos por una cifra constante:
**+32** en cada fichero de los dos openstax y **+13** en el `cap_01` de la ONU.

- **+32** es la **atribucion obligatoria CC BY 4.0** que el recorte inserta en
  cursiva al principio de cada fichero de OpenStax. Tiene 32 palabras exactas.
- **+13** es la **marca FRONTERA** del `cap_01` de la ONU.

**El recorte conto el texto DEL LIBRO, no lo que el mismo escribio encima.**
Descontando las lineas enteras en cursiva (`_..._`, que es la forma de sus notas),
los 50 bajan a 9.

**LOS 9 QUE QUEDAN SON INCONSISTENCIAS DEL PROPIO MANIFIESTO, no de la copia**, y
se comprobo uno: `bernerslee_bananas/06_bandas.md` declara 142 palabras, que es el
cuerpo **incluyendo** su nota de 30 palabras. En el `cap_01` de la ONU la excluyo.
**El recorte no aplico el mismo criterio en los 164 ficheros**, y eso es un dato
sobre el MANIFIESTO que conviene saber antes de citarlo como cifra exacta.

**`scott_radical_candor/cap_00` no tiene palabras declaradas en el MANIFIESTO**
(por eso 14 de 15): es su pagina de copyright, y de ahi sale su ficha.

## 4. LA NUMERACION: `cap_NN` ES LA DEL RECORTE, Y NO SE RENUMERA

**El numero de cada fichero es el prefijo que le puso el recorte**, no un contador
nuestro. Eso tiene tres consecuencias que hay que saber leer:

| |  |
|---|---|
| **solo dos libros tienen `cap_00`** | `onu_consumidor` (portada y creditos) y `scott_radical_candor` (pagina de copyright). **Los otros nueve empiezan en `cap_01` y no se les inventa una portada** |
| **`gerber_emyth` salta de `cap_16` a `cap_18`** | su capitulo 17 esta apartado a proposito, bajo `gerber_emyth_cap17_reservado`. **El salto es la prueba de que se fue, no un fallo** |
| **el reservado se llama `cap_17`** | conserva su numero de origen. Es un solo fichero en una carpeta propia |

**RENUMERAR HABRIA BORRADO LAS TRES COSAS.** Una cita del extractor apunta a
`cap_NN` y tiene que poder rastrearse hasta el fichero del recorte.

## 5. LO QUE NO SE COPIO, Y POR QUE NO ES UN CAPITULO

| |  |
|---|---|
| `MANIFIESTO.md`, `INDICE_REAL.md`, `CENSO_DE_CUERPOS.md`, `LISTADO_ARCHIVOS_AUDITORIA.md` | son los documentos **del propio recorte**, no del libro. Se citan en la ficha de cada fuente, no se minan |
| `bernerslee_bananas/_insumos_apendice/` (2 ficheros) | extracciones auxiliares que el fundador aporto para completar el apendice. **Respaldo de auditoria**, no texto de capitulo |

**Se quedan en `OCR/fuentes/mundo_11/`, que es donde siguen siendo utiles.**

## 6. LA MARCA `FRONTERA`, COPIADA INTACTA

**`onu_consumidor/cap_01.md` lleva su marca en la linea 9 y se copio tal cual:**

    _Nota: seccion FRONTERA, no se mina en el nucleo (ver plan de recorte)._

**Es el unico fichero de los 164 que la lleva**, contado. **El extractor la lee y
la respeta**: es una decision previa del fundador tomada en el plan de recorte, y
una vuelta no reabre una decision del fundador. Ese capitulo quedo registrado como
no minado en la vuelta 1, con la lectura de vara escrita al lado como ejemplar.

## 7. COMO SE REPRODUCE

El copiador vive en el scratchpad de la sesion y **no se commitea**: es maquinaria
de una vez, no del repo (moratoria, cosecha 7.F). Lo que se commitea es esta
cuenta. Para rehacer la bandeja desde `OCR/fuentes/`, la regla es una linea:

    por cada libro, cada fichero NN_*.md pasa a fuentes/<clave>/cap_NN.md,
    tal cual, sin renumerar y sin tocar un byte.
