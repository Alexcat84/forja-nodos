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
