# PARA ALEXIS: **LA SERIAL QUEDA PARADA ESTA SEMANA. LA INSERCION DE GROVE SE POSPONE POR CUOTA**

*Escrito por la sesion de chat del 21 sep 2026 al aplicar la enmienda del fundador del mismo
dia, archivada en `docs/loop/paradas/2026-09-21-grove-consumado-DECISION.md`. **Esta parada
no es del auditor y no es una averia: es una decision de gasto, y esta escrita para que
nadie relance la serial creyendo que se paro sola.***

> ## **NO HAY NADA ROTO. La extraccion del mundo `11` esta consumada, las guardas estan en
> VERDE y la bandeja de Grove esta intacta. Lo que no se hace esta semana es INSERTAR.**

---

## 1. EL MOTIVO, LITERAL

> Considero que por tema d elimite de cuota semanal, podemos postponer la insersion y solo
> dedicarnos a extraer, asi la siguiente semana podemos reanudar la insersion.

**Deroga para esta semana el punto `2` de la decision del `21` sep**, que autorizaba la
insercion del lote `7`. **La autorizacion no se retira: se aplaza.**

---

## 2. EL ESTADO CON EL QUE SE PARA

    $ python forja.py gate
    GATE VERDE.
      nodos verificados: 346

    $ python forja.py guiones
    BARRIDO DE GUIONES VERDE: cero guiones largos y cero guiones medios.

    $ python tests/test_aceptacion.py
    total: 340 pruebas, 0 fallos, 0 errores

| | |
|---|---|
| **rama** | `extraccion-mundo-11`, commiteada y pusheada |
| **grafo** | `346` nodos, `740` veredictos. **Sin tocar** |
| **bandeja de Grove** | `91` fichas, intactas, con veredicto de aduana las `91` |
| **lo que falta del mundo `11`** | **`1` de `5` libros del corte: `grove_high_output`** (`D.60`) |

---

## 3. QUE SI ESTA CORRIENDO

**El frente `gerber_emyth`**, en su worktree `C:/Users/AlexDesk/Documents/forja-gerber_emyth`
y su rama `extraccion-gerber_emyth`, **en extraccion y en regimen ligero**. Es la unica linea
viva esta semana (`config/frentes.json`, `alcance.lineas_a_la_vez` en `1`).

**El frente no inserta nunca** (`PARALELO.md`), asi que **el grafo no se mueve mientras esta
parada dure.**

---

## 4. COMO SE RETOMA LA SEMANA QUE VIENE

**NO se relanza la serial tal cual.** `PROMPT_SIGUIENTE.md` esta VACIO a proposito, y `D.49`
haria que el arnes buscase el encargo, lo encontrase vacio y no abriese la vuelta.

**Hace falta escribir el encargo de insercion, y su TAREA `1` esta ya decidida:**

    $ python forja.py informe --carpeta cuarentena/grove_high_output > <la carpeta de esa vuelta>/informe.txt

**Ese barrido se lanzo el `21` sep a las `07:08:59` y se mato a proposito** cuando llego la
enmienda (`.v63rec/informe_bandeja_440.meta` dice por que). **Es computo puro y cuesta cero
USD**; lo que cuesta es reloj, entre `10` y `27` horas segun la banda medida en la
`ACTA 61`.

**Y hay que relanzarlo aunque ya existiera**, porque si `gerber_emyth` cierra su extraccion y
se cosecha por `D.50`, **sus candidatos entran a esta bandeja y la poblacion deja de ser
`440`**.

**LO QUE NO HAY QUE REHACER** es la reconciliacion de los informes, que ya esta hecha y
publicada en `docs/CIERRE_LOTE_7_GROVE.md` seccion `4`: **los `91` tienen veredicto, y `73`
lo tienen contra una poblacion de `423` que no incluia a `17` hermanos suyos.**

El comando de la serial, cuando el encargo exista:

    cd /c/Users/AlexDesk/Documents/forja-nodos && \
      RAMA=extraccion-mundo-11 MODO_INSERCION=insertar MAX_VUELTAS=20 \
      bash orquestador_forja.sh

**Con Opus en las dos sillas** (decision del fundador del `21` sep): la insercion es la unica
fase que toca el grafo y la unica que no se deshace leyendo.
