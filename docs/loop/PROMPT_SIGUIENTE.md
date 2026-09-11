# ENCARGO DE LA VUELTA 12: CERRAR EL LOTE 3, `zhuo_manager`

*Escrito por **Alexis** el 11 sep 2026, al levantar la parada de la vuelta 11
(`docs/loop/paradas/2026-09-11-credito-y-la-quinta-peticion.md`).*

---

## LO PRIMERO: LAS TRES RACHAS, Y POR QUE NINGUNA TE DETIENE

    racha CLASE                     0
    racha CIFRA PUBLICADA           0
    racha REPORTE                   1 de 3
    racha propia del AUDITOR        0

**LA RACHA `REPORTE` NUNCA ESTUVO EN 3 DE 3**, y eso no es un perdon: es que
*"seguidas"* significa **consecutivas**, y la vuelta 10 fue limpia. Queda escrito
como **`D.38.1`** y en `AUDITOR_FORJA.md` 5.2 por correccion declarada.

> **UNA TANDA LIMPIA EN MEDIO PONE EL CONTADOR A CERO. NO LO CONGELA.**

**Y la del auditor arranca en cero porque su remedio cambio de genero**, no porque
se le perdonara: **la fase ciega ya no depende de su voluntad.** Ver abajo.

---

## LO QUE HA CAMBIADO EN TU TURNO

1. **`D.38.3`: la fase ciega retira CUATRO ficheros**, no uno. A ti te cambia una
   cosa y es grande: **tu mensaje final ya no es una via por la que el auditor
   pueda leerte en corto.** `ultimo_extractor.json` no esta cuando el clasifica.
2. **`D.37` tiene titular nuevo, y es el estrecho** (correccion del 11 sep 2026):
   la enumeracion cuenta **solo si dice CUANTAS partes hay Y las nombra**. **Si
   solo enumera sin contarlas, eso es `D.29`** y la arista se declara con razon
   escrita que la sostenga. **Tu lectura de la vuelta 11 era la correcta** (0 de 6
   pasaron) y ahora el titular lo dice.
3. **`config/pares_mutuos.jsonl` EXISTE y esta VACIO**, con su cabecera y su
   `LEEME`. La sede ya no hace dudar de si el protocolo la lee. **No la escribes
   tu:** la escribe la aduana cuando un veredicto declara `MUTUO`.
4. **VOLUMEN: CUATRO CAPITULOS POR VUELTA.** La cifra del lote 3 quedo firmada en
   **3,31 por ciento**, once veces menos que el 36 del lote 1.
5. **EL LOTE 2 ESTA CERRADO E INSERTADO, y el 3 tambien en lo ya minado.** El
   grafo paso de 52 a **135 nodos**. **La aduana va a levantar vecinos de verdad.**

---

## EL VOLUMEN, Y SU FRENO CON NUMERO

**CUATRO CAPITULOS POR VUELTA** (decision del fundador 5.8). **La linea base deja
de ser el 36 por ciento del lote 1**: era la cifra de una casa que empezaba, y
comparar contra ella ya no dice nada.

> **EL FRENO ES UN NUMERO FIJO: si tus puentes por capitulo suben por encima del
> 10 POR CIENTO, el lote siguiente baja un escalon.**

**Y LA UNIDAD ATOMICA SIGUE SIENDO EL CAPITULO**, cuatro o uno: se lee y se corrige
entero antes de abrir el siguiente, con su propio commit. **La cifra que decide el
volumen es POR CAPITULO**, y si lees cuatro juntos y corriges al final, **ya no
sabes cual produjo cada puente y la medida se pierde para siempre.**

---

## LO QUE QUEDA DEL LIBRO, CON SU `grep -n` AL LADO

**Seis ficheros, 33.183 palabras.** Esta vuelta son los **cuatro primeros**.

| fichero | unidad | titulo textual | palabras |
|---|---|---|---:|
| `cap_07.md` | Cap. 6 | Amazing Meetings | 5.285 |
| `cap_08.md` | Cap. 7 | Hiring Well | 7.315 |
| `cap_09.md` | Cap. 8 | Making Things Happen | 7.184 |
| `cap_10.md` | Cap. 9 | Leading a Growing Team | 6.137 |
| *(vuelta 13)* `cap_11.md` | Cap. 10 | Nurturing Culture | 3.751 |
| *(vuelta 13)* `cap_12.md` | Epilogue | The Journey Is 1% Finished | 3.511 |

**Las anclas, leidas con `grep -n` y pegadas aqui:**

    cap_07: 169 INVITE THE RIGHT PEOPLE | 187 GIVE PEOPLE A CHANCE TO COME PREPARED
            209 MAKE IT SAFE FOR PEOPLE TO CONTRIBUTE
    cap_08:  39 DESIGN YOUR TEAM INTENTIONALLY | 63 HIRING IS YOUR RESPONSIBILITY
            105 HIRING IS A GAMBLE, BUT MAKE SMART BETS
            221 HIRING WHEN YOU NEED FIVE, TEN, OR HUNDREDS OF PEOPLE
    cap_09:  31 START WITH A CONCRETE VISION | 141 PERFECT EXECUTION OVER PERFECT STRATEGY
            189 PLANNING | 197 MANAGING PERFORMANCE | 251 GOOD PROCESS IS EVER EVOLVING
    cap_10:  33 BIG TEAMS VERSUS SMALL TEAMS | 89 THE TIGHTROPE ACT OF GREAT DELEGATION
            109 GIVING PEOPLE BIG PROBLEMS IS A SIGN OF TRUST
            125 TWO HEADS, ONE SHARED VISION | 147 WHAT TO DO WHEN A MANAGER STRUGGLES

**Son las anclas que yo vi, no tu frontera.** Tu publicas la tuya entera, pieza a
pieza, **y cada cita con su `sed` pegado** (`D.35`).

**`cap_08` (Hiring Well) SE CRUZA CON EL LOTE 2 ENTERO**, que era un libro de
contratacion y ya vive en el grafo con 59 nodos. **Ahi la aduana va a trabajar de
verdad**, y eso no es un estorbo: es la primera vez que esta casa tiene dos libros
del mismo tema y puede ver si se repiten o se continuan. **Lee esos vecinos con
calma y escribe veredictos largos.**

---

## LAS TAREAS

### TAREA 1. Los cuatro capitulos, uno a uno y enteros

Por cada uno: **frontera publicada antes de cortar** con su `sed` pegado, despues
los candidatos **con la relectura de fidelidad DENTRO del acto** (`D.30`), despues
**su informe y su commit**. Y solo entonces el siguiente.

**Y LAS ARISTAS DE SERIE EN LA MISMA VUELTA** (`D.37`, `EXTRACTOR.md` 15.6): si
escribes una cabeza que dice cuantas partes tiene y las nombra, **declara sus
aristas al insertar las partes, no en la vuelta siguiente.** Con el comando:

    python forja.py arista --madre <cabeza> --hijo <parte> --paso <n> --razon "..."

**Y si la enumeracion no dice cuantas, eso es `D.29`:** se declara igual, con razon
escrita que lo sostenga, y se dice que es `D.29` y no `D.37`.

### TAREA 2. El informe del lote y el reloj

    python forja.py informe --carpeta cuarentena/zhuo_manager

**LA BANDEJA ESTA VACIA AL EMPEZAR ESTA VUELTA**, porque los 68 se insertaron y se
archivaron. **Mide cuanto tarda el informe y dilo**: el coste crecia porque la
carpeta crecia, y con la bandeja vacia tiene que volver a su tamaño.

> **SI EL INFORME SIGUE CRECIENDO CON LA CARPETA CHICA, ENTONCES ES DEL INSTRUMENTO
> Y ESO SE TRAE** (decision del fundador 5.6). No lo arregles: mide y declara.

### TAREA 3. Las cuatro medidas, por capitulo

Candidatos por mil palabras, **puentes sobre pasos escritos**, veredictos, y tiempo.
**Una fila por capitulo**, mas el total. **La fila es la que decide el volumen del
lote 4.**

### TAREA 4. El cierre del lote 3, si los cuatro cierran

Si `cap_11` y `cap_12` no caben, **se dice y se dejan para la vuelta 13**. Un
capitulo cerrado vale mas que dos a medias.

---

## LAS PARADAS

**Paras, lo declaras en TU REPORTE y te detienes si:**

- una regla de la casa te obliga a algo que rompe otra regla de la casa;
- necesitas mover un umbral, el esquema, `D.27`, `D.37` o la vara de continua
  contra repite;
- un capitulo no da ni un procedimiento.

**TU NO ESCRIBES `docs/loop/PARA_ALEXIS.md`** (`D.28`). **Un encargo asigna
trabajo, no mueve una sede.**

**NO paras por:** que la aduana levante muchos vecinos con 135 nodos (**eso es la
aduana funcionando**: lees y escribes el veredicto), que un candidato caiga (lo
corriges y pegas la salida), ni porque el informe tarde (lo mides y lo dices).

**Y NO FABRICAS MAQUINARIA** (seccion 13). En particular, y lo digo porque la
vuelta 11 lo dejo apuntado: **no toques el informe ni los umbrales para que el
reloj baje.** Si el reloj sigue mal con la bandeja vacia, **eso es un dato que se
trae, no un problema que se arregla en una vuelta.**

---

**Cero guiones largos y cero guiones medios. Si algo contradice una regla vigente,
paras y lo traes. No adivines.**
