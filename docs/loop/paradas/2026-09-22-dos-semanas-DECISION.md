# DECISION DEL FUNDADOR, 22 SEP 2026: **DOS SEMANAS. GERBER SE FUNDE, MARQUET SIGUE, LA SERIAL INSERTA**

*Responde a tres paradas a la vez: el cierre del frente `gerber_emyth` (`ACTA G9`), el credito
roto del frente `marquet_turn_the_ship` (`ACTA M5`) y la serial aparcada por cuota desde el
`21` sep. **La decision va arriba, literal. Los tres cuerpos van debajo sin tocar una coma.***

> ## **ESTE FICHERO REINICIA LA RACHA `CIFRA PUBLICADA` DE `marquet_turn_the_ship`.**
> `AUDITOR_FORJA.md` `5.4`: la reinicia una tanda limpia o una decision escrita del fundador
> en `docs/loop/paradas/`. Esta es la segunda.

---

## LA DECISION, LITERAL

> SESION DE CHAT en forja-nodos. Commitea y pushea lo pendiente en la
> rama activa antes de tocar nada. DECISION DEL FUNDADOR (22 sep 2026).
> Archivala en docs/loop/paradas/2026-09-22-dos-semanas-DECISION.md y
> aplicala en este orden:
>
> 1. FUSION DE GERBER, AUTORIZADA POR ESTA VEZ AL AGENTE: confirma que el
>    frente gerber no tiene proceso vivo, y en la rama de insercion
>    ejecuta git merge --no-ff extraccion-gerber_emyth; corre gate,
>    guiones, suite y cierre; el TABLERO pasa gerber a COSECHADO, dueño
>    NINGUNO. Si algo sale rojo, no fuerces nada: para y dimelo.
> 2. LA RACHA CIFRA PUBLICADA DE marquet_turn_the_ship SE REINICIA: las
>    dos caidas son la misma averia del instrumento, ya corregida y con
>    su prueba (una fila que se contradice a si misma ya no se escribe).
>    LAS DOCE FILAS INCOHERENTES preexistentes (8 serial, 4 marquet) se
>    corrigen por correccion declarada, anotadas en DEUDA.jsonl, sin
>    reabrir rachas cerradas: son historia que el instrumento viejo no
>    veia, no caidas nuevas.
> 3. MODELOS DESDE HOY: el extractor sigue en claude-sonnet-5; todo
>    asiento que hoy corre Opus 5 pasa a claude-opus-5-5. Antes de
>    relanzar, comprueba con claude --version y /model que la
>    instalacion ofrece claude-opus-5-5 (si no, claude update), y mira
>    en claude --help como fijar el esfuerzo: en la serial de insercion
>    el esfuerzo va en ALTO en los dos asientos; en el frente de
>    extraccion el auditor queda en su esfuerzo por defecto. Escribe en
>    el TABLERO la tabla de modelos y esfuerzo por linea y asiento.
> 4. DOS LINEAS VIVAS: la SERIAL en regimen completo inserta Grove
>    (primero reconcilia los informes de aduana ya corridos y corre solo
>    los que falten) y despues Gerber, en tandas de hasta 20 por vuelta;
>    el FRENTE MARQUET sigue extrayendo desde su capitulo 12, cuatro
>    capitulos por vuelta, cuarentena y regimen ligero. Al cerrar
>    Marquet, se cosecha e inserta como septimo libro. El mundo 11
>    cierra con siete libros; no se abre ningun libro nuevo.
> 5. Escribe los dos PROMPT_SIGUIENTE y deja los dos comandos exactos con
>    sus modelos. No lances: lanzo yo.

**Y DOS MENSAJES DEL MISMO DIA QUE LA COMPLETAN**, tambien literales. El primero confirma los
comandos; el segundo **deroga el `No lances: lanzo yo` del punto `5`** y va archivado aparte,
en `docs/loop/paradas/2026-09-22-tu-lanzas-MANDATO.md`, porque es una delegacion permanente
y no una decision sobre esta parada.

> Los comandos quedarán parecidos a estos (confirma los de CC, que llevarán además el esfuerzo):
>
> cd /c/Users/AlexDesk/Documents/forja-nodos
> git checkout extraccion-mundo-11
> RAMA=extraccion-mundo-11 MODO_INSERCION=insertar MODELO_EXTRACTOR=claude-opus-5-5 MODELO_AUDITOR=claude-opus-5-5 MAX_VUELTAS=20 bash orquestador_forja.sh
> cd /c/Users/AlexDesk/Documents/forja-marquet_turn_the_ship
> RAMA=extraccion-marquet_turn_the_ship MODO_INSERCION=cuarentena MODELO_EXTRACTOR=claude-sonnet-5 MODELO_AUDITOR=claude-opus-5-5 MAX_VUELTAS=20 bash orquestador_forja.sh

**Una lectura que ese primer mensaje resuelve, y conviene dejarla escrita:** el punto `3` dice
*el extractor sigue en `claude-sonnet-5`*, y podia leerse como TODOS los extractores. **El
comando del fundador pone `claude-opus-5-5` en el extractor de la serial**, que es lo que su
nota del `21` sep ya decia: *la insercion va con Opus en las dos sillas a proposito; es la
unica fase que toca el grafo y la unica que no se deshace leyendo*. **Sonnet queda en el
extractor de EXTRACCION; la insercion va con Opus en los dos asientos.**

---

## CUERPO 1 DE 3: EL CIERRE DE GERBER, `ACTA G9`, SIN TOCAR UNA COMA

# PARA ALEXIS: **EL FRENTE `gerber_emyth` HA TERMINADO SU LIBRO Y SE DETIENE. ES LA PARADA FELIZ, Y LO QUE SIGUE ES TUYO**

*Escrito por el auditor del bucle al cerrar la `ACTA G9`, 21 sep 2026. Rama
`extraccion-gerber_emyth`, worktree `C:/Users/AlexDesk/Documents/forja-gerber_emyth`.
Hash auditado: `9ca4073`.*

---

## 1. EL MOTIVO, Y SON DOS DE LA SECCION `3` DE `AUDITOR_FORJA.md`

**NO ES CREDITO ROTO.** Las cinco rachas de esta linea cierran en `0`.

| condicion | por que se cumple |
|---|---|
| **CAMPANIA CONSUMADA** | **el libro esta minado `22` de `22` unidades**, sin un solo hueco. `d094`, que apartaba `cap_01` a `cap_03`, **esta pagada**. Al frente **no le queda una sola unidad que le este permitida** (seccion `4`) |
| **DECISION DE ALEXIS** | lo que sigue son **tres cosas que la casa te reserva** y que el bucle no hace: fundir la rama, firmar tres capitulos en `config/` y tocar una guarda. Van en la seccion `3` |

**Y `PARALELO.md` `5.0.b` paso `(a)` PEDIA EXACTAMENTE ESTE FICHERO EN EL ARBOL** para que el
relevo pueda empezar: el frente queda **detenido y sin proceso vivo**, y este es su
`PARA_ALEXIS.md`.

**`docs/loop/PROMPT_SIGUIENTE.md` QUEDA VACIO**, que es lo que el encargo de esta vuelta pide
en su seccion `6` y lo que la parada manda.

---

## 2. EL ESTADO EXACTO, MEDIDO HOY CON EL INSTRUMENTO DELANTE

### 2.a. Las guardas, corridas por el auditor en esta vuelta

    $ python forja.py gate
    GATE VERDE.  nodos verificados: 346
    $ python forja.py guiones
    BARRIDO DE GUIONES VERDE: cero guiones largos y cero guiones medios.
    $ python tests/test_aceptacion.py | tail -1
      total: 353 pruebas, 0 fallos, 0 errores
    $ python scripts/tallar_reporte.py | tail -1
    TALLADO VERDE: las 181 tabla(s) comprobables son las de su instrumento, celda a celda.
    $ python scripts/censar_rutas.py | tail -1
    CENSO VERDE: las 1161 rutas publicadas sostienen lo que dicen sostener.

**LAS CINCO VERDES. CERO GUARDA DE DATO EN ROJO.**

### 2.b. Las cinco rachas: **el frente cierra entero en cero**

    $ python forja.py credito | sed -n '5,11p'
      especie            racha      de donde sale
      ----------------------------------------------------------------------
      AUDITOR            0 de 3     ACTA G9
      CIFRA PUBLICADA    0 de 2     ACTA G9
      CLASE              0 de 2     ACTA G9
      DATO MOVIDO        0 de 2     ACTA G9
      REPORTE            0 de 3     ACTA G9

**NUEVE TANDAS, CERO CAIDAS ACUMULADAS EN NINGUNA DE LAS CINCO ESPECIES.** La unica caida de
la ultima tanda (`d135`, una razon de lectura mas ancha que el capitulo) **no acumula por
sede** (`5.2`), y el veredicto que sostenia **se sostiene** (`ACTA G9` `4.1`).

### 2.c. El censo por capitulo, contado por el auditor por `UNIDAD DE ORIGEN` declarada

| capitulo | estado | candidatos | pasos | firma |
|---|---|---:|---:|---|
| `cap_01` | MINADO EN CERO | `0` | `0` | **`ACTA G9` `3.1`, FALTA en `config/frentes.json`** |
| `cap_02` | MINADO EN CERO | `0` | `0` | **`ACTA G9` `3.1`, FALTA en `config/frentes.json`** |
| `cap_03` | MINADO EN CERO | `0` | `0` | **`ACTA G9` `3.1`, FALTA en `config/frentes.json`** |
| `cap_04` | MINADO CON CANDIDATOS | `1` | `7` | bandeja, `UNIDAD DE ORIGEN` declarada |
| `cap_05` | MINADO EN CERO | `0` | `0` | firmado en `config/frentes.json` |
| `cap_06` | MINADO EN CERO | `0` | `0` | firmado en `config/frentes.json` |
| `cap_07` | MINADO CON CANDIDATOS | `1` | `8` | bandeja, `UNIDAD DE ORIGEN` declarada |
| `cap_08` | MINADO CON CANDIDATOS | `2` | `17` | bandeja, `UNIDAD DE ORIGEN` declarada |
| `cap_09` | MINADO EN CERO | `0` | `0` | firmado en `config/frentes.json` |
| `cap_10` | MINADO EN CERO | `0` | `0` | firmado en `config/frentes.json` |
| `cap_11` | MINADO CON CANDIDATOS | `6` | `57` | bandeja, `UNIDAD DE ORIGEN` declarada |
| `cap_12` | MINADO CON CANDIDATOS | `3` | `12` | bandeja, `UNIDAD DE ORIGEN` declarada |
| `cap_13` | MINADO CON CANDIDATOS | `1` | `10` | bandeja, `UNIDAD DE ORIGEN` declarada |
| `cap_14` | MINADO CON CANDIDATOS | `1` | `9` | bandeja, `UNIDAD DE ORIGEN` declarada |
| `cap_15` | MINADO CON CANDIDATOS | `1` | `5` | bandeja, `UNIDAD DE ORIGEN` declarada |
| `cap_16` | MINADO EN CERO | `0` | `0` | firmado en `config/frentes.json` |
| `cap_17` | MINADO EN CERO | `0` | `0` | firmado en `config/frentes.json` |
| `cap_18` | MINADO CON CANDIDATOS | `3` | `26` | bandeja, `UNIDAD DE ORIGEN` declarada |
| `cap_19` | MINADO CON CANDIDATOS | `3` | `25` | bandeja, `UNIDAD DE ORIGEN` declarada |
| `cap_20` | MINADO EN CERO | `0` | `0` | firmado en `config/frentes.json` |
| `cap_21` | MINADO EN CERO | `0` | `0` | firmado en `config/frentes.json` |
| `cap_22` | MINADO EN CERO | `0` | `0` | firmado en `config/frentes.json` |
| **total** | **`22` de `22` minadas** | **`22`** | **`176`** | |

**LO QUE ESA TABLA DICE EN UNA LINEA: `22` candidatos en bandeja con `176` pasos, `0` en el
grafo, `12` capitulos minados en cero con su razon leida y firmada por un acta.**

    $ ls cuarentena/gerber_emyth/*.json | wc -l
    22
    $ python <cuenta propia del auditor sobre dataset/nodos.jsonl>
    nodos de dataset/nodos.jsonl : 346   de ellos que nombren 'gerber_emyth': 0

### 2.d. La fase

**`MODO_INSERCION=cuarentena` toda la vida de este frente. CERO INSERCION, CERO DATO MOVIDO.**
`dataset/`, `bitacora/`, `censos/`, `config/pares_mutuos.jsonl`, `cuarentena/` y `fuentes/`
**no se movieron en la vuelta `9`**, medido con `git diff` entre sus dos commits (`ACTA G9`
`1.6`).

---

## 3. LO QUE NECESITO DE TI, Y SON TRES COSAS

### 3.1. **FUNDIR LA RAMA, que es el paso `(b)` de `D.50` y no es del bucle**

**El encargo de la vuelta `9` ya lo anuncia en su seccion `0`** (*el fundador funde tu rama a
`extraccion-mundo-11` y tus `22` candidatos pasan a esperar la insercion de la semana que
viene*). **El bucle no funde ramas y el bucle no crea remotos**, asi que lo pido nombrando la
rama y el estado, que es lo que `PARALELO.md` `5.0.b` manda:

| | |
|---|---|
| **rama** | `extraccion-gerber_emyth` |
| **worktree** | `C:/Users/AlexDesk/Documents/forja-gerber_emyth` |
| **estado en el tablero** | `EN CURSO`, dueno `gerber_emyth`, `22` en bandeja, `ultimo_capitulo` `cap_22` |
| **que lleva** | `22` fichas en `cuarentena/gerber_emyth/`, `0` cambios en el grafo, el reporte y las nueve actas del frente |
| **detras** | `5.1` a `5.3` de `PARALELO.md`: una por vez, gate y suite detras |
| **y luego** | paso `(c)`: `python forja.py tablero --escribir` para dejarlo en dueno `NINGUNO` |

### 3.2. **FIRMAR `cap_01`, `cap_02` Y `cap_03` EN `config/frentes.json`**, porque `config/` no es sede mia

**LA FIRMA YA ESTA ESCRITA Y ES CITABLE**, en `ACTA G9` seccion `3.1`: los tres capitulos
quedan **leidos ENTEROS y adjudicados en CERO NODOS** por el auditor de la vuelta `9`. Lo que
falta es meterla en el campo que `d096` creo para esto. Hoy:

    $ python -c "import json;print(json.load(open('config/frentes.json'))['minados_en_cero']['gerber_emyth']['capitulos'])"
    ['cap_05', 'cap_06', 'cap_09', 'cap_10', 'cap_16', 'cap_17', 'cap_20', 'cap_21', 'cap_22']
    $ python -c "import json;[print(len(json.loads(l)['capitulos_minados'])) for l in open('docs/loop/TABLERO.jsonl') if json.loads(l).get('clave')=='gerber_emyth']"
    19

**Anadiendo `cap_01`, `cap_02` y `cap_03` a esa lista, el tablero pasa a `22` de `22` por su
propio canal** y el libro deja de necesitar que nadie lo cuente a mano. **Es la misma
peticion que la `ACTA G8` hizo por los cinco anteriores y que se cumplio.** Queda anotada
como `d136`.

La cita que corresponde, para pegarla en el campo `cita`:

> `ACTA G9` `3.1` (`cap_01` el `Foreword`, `cap_02` la `Introduction` y `cap_03` `Cap. 1`,
> los tres leidos enteros: prefacio personal, las cuatro `IDEA #` como metas sin inventario
> de medios, y el diagnostico del mito con el caso de Sarah). Frente `gerber_emyth`, rama
> `extraccion-gerber_emyth`.

### 3.3. **UNA GUARDA QUE NO VE ESTE FRENTE**, medida y no tocada (`d134`)

**`D.45` me prohibe tocar `src/`, `scripts/`, el banco y el arnes desde un frente, asi que la
mido y te la subo.** `scripts/tallar_reporte.py` define la ventana de la guarda `D.59` como

    CABEZA_DE_VUELTA = re.compile(r"^#{1,2}\s+VUELTA\s+\d+", re.M)

y **las `7` cabeceras de este frente son `# FRENTE <clave>, VUELTA N:`**, que no casan.
Medido hoy sobre `docs/loop/REPORTE.md`:

    cabezas que el regex de D.59 reconoce: 61
    ULTIMA que reconoce: # VUELTA 62, lote 7 (`grove_high_output`), CLASE EXTRACCION
    linea de esa cabeza: 57016  / total lineas: 61799
    lineas que quedan DENTRO de la 'vuelta viva': 4783
    cabezas de FRENTE que el regex NO reconoce: 7

**Su *vuelta viva* son `4783` lineas, las vueltas `2` a `9` enteras del frente, en vez de las
`683` de la vuelta `9`.**

> **LECTURA:** su propio docstring dice que la ventana ancha es justo lo que vino a evitar
> (*sobre el reporte entero caerian `591` lineas de `53` vueltas de historia; sobre la vuelta
> viva cayeron `2`, y las dos eran de verdad*). **En este frente la ventana nunca se
> estrecho**, y de ahi sale el falso positivo de *intermedia* contra *media* que la vuelta `9`
> tuvo que rodear. **Si otros frentes usan la misma cabecera, les pasa lo mismo.**

---

## 4. POR QUE EL FRENTE NO PUEDE SEGUIR SOLO: LAS SEIS CLAVES MEDIDAS

**`D.32` manda medir las dos condiciones de apertura y publicarlas, y las publico. Las seis
salen VERDES en las dos, y aun asi ninguna se abre**, porque en las seis manda un tercer
bloqueo:

| clave | material | canonica | `--puedo` hoy | por que NO |
|---|---:|---|---|---|
| `gerber_emyth_cap17_reservado` | `1` | SI | `SI` | `ORDEN_DE_LOTES.md` `L27`: **RESERVADO, entra el ultimo**, cuando su libro este en el grafo. Hoy hay `0` nodos de `gerber_emyth` en el grafo |
| `marquet_turn_the_ship` | `17` | SI | `NO` | **PAUSADO y NO COSECHADO** en otra rama, con `9` candidatos sin llegar. `D.50`: se releva ENTERO, y el relevo empieza por tu paso `(b)` |
| `grove_high_output` | `18` | SI | `SI` | **nada que continuar**: `18` de `18` minados, `ultimo_capitulo` `cap_18`. El `SI` esta vacio |
| `bernerslee_bananas` | `19` | SI | `SI` | el tablero lo marca con **asterisco**: `FUERA DE CAMPANIA` |
| `openstax_business_ethics` | `17` | SI | `SI` | idem, **FUERA DE CAMPANIA** |
| `openstax_org_behavior` | `32` | SI | `SI` | idem, **FUERA DE CAMPANIA** |

**Tomar cualquiera de las tres de asterisco es cambiar el alcance de la extraccion**, y eso lo
reserva la casa a ti.

---

## 5. UNA CIFRA QUE SUBO SIN ADJUDICARLA, PORQUE NO ES MIA (`d125`)

**`PARALELO.md` `4.d` corto este libro de la campania** sobre la premisa de que insertarlo
*obligaria a minar los dos libros enteros*, con el frente fotografiado en **`10` candidatos y
`4` de `22` capitulos**.

**Hoy el frente esta en `22` candidatos y `22` de `22` capitulos: ese coste ya esta pagado
ENTERO.** El encargo de esta vuelta dice en su seccion `0` que ya lo decidiste (`gerber_emyth`
entra al mundo `11` como sexto libro, por la clausula de `D.60`). **No adjudico nada con esto:
solo dejo la cifra final delante**, que es lo que la `ACTA G8` `8.3` prometio hacer.

---

## 6. COMO RETOMAR

1. **Funde** `extraccion-gerber_emyth` a `extraccion-mundo-11` (`PARALELO.md` `5.1` a `5.3`,
   una por vez, gate y suite detras), y corre `python forja.py tablero --escribir` para
   dejarlo en dueno `NINGUNO`.
2. **Firma** `cap_01`, `cap_02` y `cap_03` en `config/frentes.json` con la cita de `3.2`.
3. **La insercion de los `22` NO es de ningun frente** (`D.45`) y **no la hace el bucle**: se
   pide aparte, en la linea que inserte, y `D.32` dice que **no bloquea** nada.
4. **Los cuatro punteros que la vuelta de insercion no puede perder** siguen publicados sin
   cambio, comprobados en la vuelta `9` (`REPORTE.md` `G9.5.c`): **`d098`** (`D.37`, `cap_05`
   `L29`, terna sin cabeza), **`d104`** (`D.37`, `cap_12` `L21`, terna sin cabeza),
   **`d108`** (releer `cap_14` `L27` contra `L117`) y **`d111`** (la serie de `cap_13`, en `0`
   de `7`).
5. **`d134`** (la guarda) y **`d135`** (la razon de lectura de `cap_01` y `cap_03`) quedan en
   `docs/loop/DEUDA.jsonl` con su cita, y **`d135` la paga la vuelta que vuelva a tocar el
   reporte**, tachando sin borrar.
6. **Para borrar esta parada y volver a abrir el bucle en esta rama**, borra este fichero: el
   arnes se detiene mientras exista (`orquestador_forja.sh`, y el `loop.log` lo registra).

---

*`PARA_ALEXIS.md` del frente `gerber_emyth`, escrito por el auditor, que es su unica sede
(`D.28`, ratificada por el fundador). **El extractor de la vuelta `9` declino escribirlo y
acerto**: la adjudicacion esta en `ACTA G9` seccion `5`. **El libro esta entero, las cinco
rachas en cero, las cinco guardas verdes y cero dato movido en nueve tandas.***

---

## CUERPO 2 DE 3: EL CREDITO ROTO DE MARQUET, `ACTA M5`, SIN TOCAR UNA COMA

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

---

## CUERPO 3 DE 3: LA SERIAL APARCADA DESDE EL 21 SEP, SIN TOCAR UNA COMA

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
