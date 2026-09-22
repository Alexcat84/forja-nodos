# PARA ALEXIS: **EL FRENTE `marquet_turn_the_ship` PARA POR CREDITO ROTO**

*Escrito por el auditor del bucle al cerrar la `ACTA M5`, que audita la **vuelta `4`** de este frente.
Rama `extraccion-marquet_turn_the_ship`, worktree `C:/Users/AlexDesk/Documents/forja-marquet_turn_the_ship`.
Fecha: **2026-09-21**.*

---

## 1. EL MOTIVO, EN UNA FRASE

**`CIFRA PUBLICADA` llega a `2 de 2`, su tope, con dos tandas SEGUIDAS de dos vueltas distintas**
(`AUDITOR_FORJA.md` `3` y `5.4`). Las dos son **la misma averia en la misma sede**: el registro de credito
de esta linea publica lo contrario de lo que dice la tabla que lo documenta.

| tanda | vuelta | que se cayo | adjudicado en |
|---|---:|---|---|
| `ACTA M4` | `3` | cuatro lineas escritas con `cae: true` mientras su tabla `7.d` decia *no cae* cuatro veces | `ACTA M4` `M4.10` |
| `ACTA M5` | `4` | cuatro lineas con la racha SUBIDA mientras su tabla `5.d` dice *no cae* cuatro veces, y **ninguna con `--cae` ni `--limpia`** | `ACTA M5` `M5.11` |

**Ninguna tanda limpia de esa especie en medio que la reinicie** (`D.38.1`).

**LA SEGUNDA TIENE TRES AGRAVANTES, y por eso no la leo como descuido:**

1. el encargo de la vuelta `4` se lo dijo con esas palabras (`PROMPT_SIGUIENTE.md` `2.3` y `6`:
   *`--cae` o `--limpia` coherente con lo que tu tabla dice*);
2. **el propio reporte escribio la regla en su seccion `1.a` y la rompio en su seccion `5.d`**;
3. la cifra falsa **ha parado el bucle de verdad**: `python forja.py credito` publica hoy
   `CIFRA PUBLICADA 2 de 2 TOPE` y `CREDITO ROTO` sobre una tanda que el reporte sostiene limpia.

**UNA ACLARACION QUE IMPORTA PARA DECIDIR:** el extractor declaro la parada leyendo el tope **de la cifra
que el mismo acababa de escribir mal**. Por esa via no habria parada: una tanda limpia reinicia a `0`.
**La parada es real por la otra via**, la que adjudica la `ACTA M5`: **escribir esas cuatro rachas falsas
ES la caida de `CIFRA PUBLICADA` de esta tanda**, la segunda seguida. El numero coincide y la razon se
invierte.

---

## 2. EL ESTADO EXACTO

| | | medido con |
|---|---|---|
| rama | `extraccion-marquet_turn_the_ship` | `git rev-parse --abbrev-ref HEAD` |
| ultimo commit del extractor | `6e8cb4e` | `git log --oneline -1` |
| nodos en el dataset | **`346`** verificados, `346` lineas, `346` `id` unicos | `python forja.py gate`, `wc -l dataset/nodos.jsonl` |
| veredictos | `740` | `wc -l bitacora/VEREDICTOS.jsonl` |
| pares mutuos | `1` | `wc -l config/pares_mutuos.jsonl` |
| candidatos en bandeja de este libro | **`17`** | `ls cuarentena/marquet_turn_the_ship/*.json \| wc -l` |
| unidades del libro | `17`, de las que **`11` estan minadas** (`cap_01` a `cap_11`, con `cap_05` firmado en cero) | `python forja.py tablero` |
| nodos de este libro en el grafo | **`0`** | fila del libro en `docs/loop/TABLERO.jsonl` |
| fase | **EXTRACCION en regimen ligero**, `MODO_INSERCION=cuarentena`. **Cero inserciones en las cuatro vueltas** | `docs/loop/loop.log` |
| `gate` | `GATE VERDE.` | corrido por el auditor en esta vuelta |
| `guiones` | `BARRIDO DE GUIONES VERDE` | corrido por el auditor en esta vuelta |
| pruebas de aceptacion | `356` pruebas, `0` fallos, `0` errores | corrido por el auditor en esta vuelta |
| las cuatro guardas de DATO | **ninguna en rojo** (`ACTA M5` `M5.15`) | corridas por el auditor |
| deuda de la linea | `LIBRE`, `van 2 de 5`, **`34` esperando**: las `32` de antes mas `d103` y `d104`, que son de esta acta | `python scripts/deuda.py --clase 4` |

**EL CREDITO, TAL COMO QUEDA EN EL REGISTRO DESPUES DE ESTA ACTA:**

    especie            racha
    CIFRA PUBLICADA    2 de 2   TOPE
    REPORTE            1 de 3
    CLASE              0 de 2
    DATO MOVIDO        0 de 2
    AUDITOR            0 de 3

**EL TRABAJO DE MINERIA DE LA VUELTA `4` ESTA BIEN Y SE LO FIRMO ENTERO**, y conviene decirlo porque la
parada no lo toca: las tres fronteras de `cap_09`, `cap_10` y `cap_11` me cierran **al digito** (`144`
filas, `5500` palabras, `0` solapes, `0` lineas sin cubrir), los `8` pasos de los tres candidatos estan
**literales en la linea que citan** (`0` PUENTE, `0,00` por ciento en los tres capitulos), la muestra de
fidelidad con semilla `m4` me sale **identica**, y **los once discutibles se sostienen los once**.
**Lo que para el bucle no es el trabajo: es el registro.**

---

## 3. LO QUE SE NECESITA DE TI

**UNA DECISION ESCRITA EN `docs/loop/paradas/`, porque el bucle no puede reiniciar su propia racha**
(`AUDITOR_FORJA.md` `5.4`: *la reinicia una decision de Alexis escrita en `docs/loop/paradas/`, y el acta
lo dice citandola. Un auditor que pone su propia racha a cero se esta absolviendo*).

**LAS TRES COSAS QUE HAY QUE DECIDIR, y son distintas entre si:**

1. **Si la racha de `CIFRA PUBLICADA` de esta linea se reinicia, y con que motivo escrito.** Sin eso el
   frente no puede abrir otra vuelta: la condicion de parada sigue cumpliendose al abrir.
2. **Si el registro de credito se sigue escribiendo a mano, con dos defectos del instrumento medidos y
   sin tocar** (`D.45` congela `src/` y `scripts/` mientras corran frentes en paralelo, asi que **los mido
   y los subo, no los arreglo**):
   - **`forja.py credito --anotar` acepta una `--racha` que contradice a sus propias banderas, y acepta
     que no haya ninguna bandera** (`ACTA M5` `M5.11`). Las dos caidas de esta racha son eso mismo: una
     tabla que dice una cosa y un fichero que dice otra.
   - **el replay no sabe distinguir una propuesta de una adjudicacion sobre la MISMA vuelta**, y las
     cuenta como dos tandas (`ACTA M5` `M5.12.a`, `ACTA M4` `M4.11.a`). Hoy marca `3` discrepancias, y
     **las tres son esa figura**. El campo `vuelta` de cada fila ya trae el dato que haria falta para
     distinguirlas.
3. **Si `marquet_turn_the_ship` sigue, y con que modelo.** El libro va por `11` de `17` unidades minadas
   y `17` candidatos, sin un solo nodo insertado. Quedan `cap_12` a `cap_17`, **seis unidades**, y la
   ultima medida de volumen dice que el tramo podria subir a **cuatro capitulos por vuelta**
   (`8.1`, con el peor capitulo en `0,00`).

**LO QUE NO HE HECHO, PORQUE NO ES MIO:** no reinicio ninguna racha, no fundo ramas, no creo remotos, no
toco `src/`, el banco ni el arnes, y no escribo doctrina (`D.45`, `D.56`). **Y no pido merge:** este frente
no ha insertado nada y su lote no cierra, asi que no hay campaña consumada que fundir.

---

## 4. COMO SE RETOMA

1. **Escribe la decision** en `docs/loop/paradas/2026-09-2N-<lo-que-sea>.md`, diciendo si la racha de
   `CIFRA PUBLICADA` vuelve a `0` y por que.
2. **Anotala en el registro** como suceso de **reinicio**, que es la unica forma que el instrumento acepta
   y la unica que deja releerlo despues. **La comprobe contra `src/credito.py` antes de escribirla aqui:**
   no hay bandera `--reinicio`, el tipo se pasa como campo y por defecto valdria `tanda`.

       python forja.py credito --anotar --tipo reinicio --especie "CIFRA PUBLICADA" --racha "0 de 2" --cita "docs/loop/paradas/<el fichero>, punto N"

   La `cita` es obligatoria y **no puede traer una conclusion dentro** (`D.56`, `cita_es_referencia`):
   ruta y punto del fichero de parada, nada mas. El instrumento **no reinicia nada por su cuenta a
   proposito** (`src/credito.py`, cabecera).
3. **Borra `docs/loop/PARA_ALEXIS.md`**, que es lo que el arnes mira para volver a arrancar
   (`orquestador_forja.sh`: *DETENIDO en la vuelta N: existe docs/loop/PARA_ALEXIS.md*).
4. **El encargo de la vuelta `5` esta sin escribir a proposito**: `docs/loop/PROMPT_SIGUIENTE.md` queda
   **VACIO**, como manda `AUDITOR_FORJA.md` `3`. Cuando el frente reabra, lo escribe el auditor de esa
   vuelta. **Lo que ese encargo tendria que llevar ya esta medido y firmado en la `ACTA M5` `M5.18` y
   `M5.19`:** `cap_12` en adelante, el tramo, las dos deudas nuevas y las tres aduanas que quedan a
   verificar.

---

**LA LECTURA QUE ME DEJABA SEGUIR ESTABA A MANO Y NO LA TOME.** La apunto entera en `ACTA M5` `M5.11.c`
para que se pueda releer contra mi: si la tanda del extractor se lee limpia, `D.38.1` la pone a cero y no
hay parada ninguna. **Es cierta sobre su trabajo de mineria y falsa sobre su registro**, y la caida de
esta tanda vive justo ahi.
