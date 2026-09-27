# DICTAMEN DEL 16 SEP 2026: **DOS ESPECIES EN LA MISMA PARADA.** `ARNES` CURADA, `CREDITO` PENDIENTE

*Escrito siguiendo el guion de reanudacion del fundador del 13 sep 2026.*

> ### **ESTO NO ES UNA DECISION DEL FUNDADOR.** Es un dictamen y una cura parcial.
>
> `docs/loop/PARA_ALEXIS.md` **sigue existiendo y sigue deteniendo el bucle**, porque
> la mitad que queda es del fundador y solo suya.

---

## 1. LAS DOS ESPECIES, SEPARADAS

La `ACTA 26` trae **dos motivos de parada** en el mismo documento, y son de especies
distintas. Los separo porque el guion manda tratarlos distinto.

| # | lo que el auditor trae | especie | quien lo resuelve |
|---|---|---|---|
| **1** | su racha propia llega a **3 de 3** | **`CREDITO`** | **el fundador** (`5.4`) |
| **2** | **`D.38.5` vigente contra `src/aduana.py`** | **`ARNES`**, defecto del instrumento | **yo**, y esta hecho |

---

## 2. LA `ARNES`, CURADA. **Y EL DEFECTO ERA MIO**

**`D.38.5` DICE `TAMBIEN PARA LA ADUANA` EN SU PROPIO TITULAR.** La escribi yo el 12
sep y **la cablee solo en `src/informe.py`**, que corre EN SECO. **La que decide es
`src/aduana.py`**, y ahi seguia midiendo solo el grafo:

    src/informe.py:222   poblacion = list(nodos) + list(bandejas)
    src/aduana.py:797    vecinos = buscar_vecinos(candidato, nodos, umbrales)
    $ grep -n "poblacion_de_bandejas" src/aduana.py   ->  cero coincidencias

**NO ES UNA PREGUNTA DE DOCTRINA Y POR ESO NO ESPERO A NADIE.** La doctrina esta
escrita, es literal, y lleva el titular puesto. **Lo que no coincidia era el codigo.**

### Lo que se hizo

**LA POBLACION SE MUDA A `src/aduana.py`**, que es donde se decide, y el informe la
toma de ahi. Los nombres se conservan en `informe.py` porque es su sede historica y
hay actas que lo citan.

**LA TABLA DE `D.38.5` NO CAMBIA NI UNA LINEA:**

| pieza | poblacion | y sigue igual |
|---|---|---|
| el barrido de vecinos | **grafo mas bandejas** | ahora **tambien al insertar** |
| `el id ya vive en el grafo` | **solo el grafo** | ensancharlo convertiria la bandeja entera en un lote rechazado |
| los instrumentos de `calibracion/` | **solo el grafo** | miden contra un catalogo con su tag |
| el propio candidato | **excluido** | por su id, la errata de `D.38.4` que corrigio la `ACTA 18` |

### Los dos casos, porque una guarda sin caso positivo no guarda nada

| | |
|---|---|
| **POSITIVO** | un candidato cuyo unico vecino **vive en la bandeja** queda **BLOQUEADO** por la aduana de verdad. **Antes entraba limpio**, y ese es exactamente el aplazamiento que la `ACTA 26` midio |
| **NEGATIVO** | sin vecino en la bandeja **entra limpio**: una aduana que bloquea todo es un candado, no una guarda |
| **NEGATIVO** | `el id ya vive en el grafo` **sigue mirando solo el grafo** |

**6 pruebas** (`PruebaAduanaMideBandejas`), y la bandeja se puede sobreescribir
(`FORJA_CUARENTENA`) como el dataset y la bitacora: **sin eso la prueba mediria contra
los candidatos del repo de verdad y cambiaria de una vuelta a otra.**

### El coste que esto tenia, medido por el auditor y no por mi

**Cinco pares por encima de umbral sin veredicto**, los cinco con un extremo en la
bandeja. El sexto, el unico con los dos extremos en el grafo, **si lo tiene**. **No era
perdida: era aplazamiento.** Pero `D.38.5` nacio para que un par **no dependa de que
alguien se acuerde**, y eso es justo lo que estaba pasando.

---

## 3. LA `CREDITO`, QUE NO TOCO

**La racha del auditor esta en `3 de 3` y ahi se queda.** `AUDITOR_FORJA.md` `5.4`: la
reinicia una tanda limpia o una decision del fundador escrita en `docs/loop/paradas/`,
y **ninguna de las dos soy yo**. El guion solo me autoriza a relanzar en la especie
`ARNES`.

**Y LA ESPECIE DE SUS DOS CAIDAS NO TIENE CURA MECANICA ESCRITA**, que es lo que el
guion me manda comprobar antes de nada:

| su caida | la cura que ya existe | por que no la cubre |
|---|---|---|
| publicar *ningun nodo dice de que capitulo sale* contando **campos** y concluyendo sobre **contenido** | `D.38.3` (toda cifra con su instrumento pegado) | **pego un instrumento.** `D.38.3` exige que haya instrumento, **no que mida lo que la frase dice** |
| declarar `NO APLICA` un heredado con un motivo falso | `D.40` (la herencia se declara con motivo) | **escribio el motivo.** `D.40` exige motivo, **no que el motivo sea cierto** |

**LA PROPUESTA VA EN `PARA_ALEXIS.md` `A.4`**, que es donde el guion manda escribirla,
y es la del propio auditor porque le pega a las dos caidas a la vez.

---

## 4. LO QUE NO HICE

- **NO reinicie ninguna racha.** La del auditor sigue en `3 de 3`.
- **NO relance el arnes.** El bucle sigue parado y es correcto.
- **NO resolvi la ambiguedad de `tanda limpia`**, que dos actas seguidas han tenido
  que razonar contra si mismas. **Esa es doctrina y es del fundador.**
- **NO toque el texto del auditor** en `PARA_ALEXIS.md`: solo anadi el anexo.

## 5. ESTADO

    rama            : extraccion-mundo-11
    PARA_ALEXIS.md  : EXISTE. El bucle sigue detenido, y es correcto
    nodos           : 234        bitacora : 240 veredictos
    lote 4          : 31 de 142 insertados, 111 en bandeja
    racha del auditor: 3 de 3    racha REPORTE del extractor: 1 de 3

    python forja.py gate                 GATE VERDE, 234 nodos
    python forja.py guiones              VERDE
    python scripts/tallar_reporte.py     VERDE
    python scripts/censar_rutas.py       VERDE
    python tests/test_aceptacion.py      136 pruebas, 0 fallos   (eran 130)
    bash tests/prueba_arnes.sh           128 comprobaciones en VERDE
