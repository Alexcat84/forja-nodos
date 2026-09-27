# -*- coding: utf-8 -*-
import io

RUTA = "docs/loop/REPORTE.md"
s = io.open(RUTA, encoding="utf-8").read()


def sangrado(ruta):
    texto = io.open(ruta, encoding="utf-8").read().rstrip()
    lineas = texto.split(chr(10))
    return chr(10).join(("    " + l) if l.strip() else "" for l in lineas)


def tabla(ruta):
    lineas = io.open(ruta, encoding="utf-8").read().rstrip().split("\n")
    return "\n".join(l for l in lineas if l.startswith("|")).strip()


x6 = """## X.6. LOS DISCUTIBLES, MARCADOS ANTES DE SABER SI ACIERTO (`EXTRACTOR.md` 8)

**LOS MARCO A CIEGAS, y el orden es el de lo que mas me costaria defender.** La metrica de credito
distingue una caida dentro del marcado de una fuera, **y esa diferencia solo significa algo si el
marcado se hizo antes.**

| # | el discutible | lo que decidi | lo que me haria dudar |
|---:|---|---|---|
| **1** | **las SEIS aristas cabeza a parte de `decidir_quien_comunica_cada_cuanto`, que nadie me encargo** | las declaro por `D.29`, porque su paso `6` enumera los diez rotulos de `L17` a `L35` uno a uno y seis de ellos ya viven | **es la lectura mas ancha que he hecho en una vuelta.** Nadie me la pidio, y el paso `6` del candidato es la transcripcion de un INDICE del libro. **Si un indice no cuenta como enumeracion, las seis se caen juntas** |
| **2** | **NO declarar la septima**, la de `Meeting-Free Zones` hacia `pelear_proliferacion_reuniones_bloquear_ejecucion` | no la declaro: el paso nombra *las zonas libres de reuniones* y el nodo sale de la seccion `EXECUTION TIME` | **es incoherente con el `1` si se mira de lejos**: seis si y una no. Lo que las separa es que en las seis el paso NOMBRA al hijo y en esta el emparejamiento lo pongo yo por posicion en la lista |
| **3** | `escribir_apuntes_sala_estudio_equipo` paso `10` marcado **`TRANSCRIPCION`** | *el texto nombra los sitios donde vale hacerlo* **sin nombrarlos**, y `L155` nombra los tres. Digo MENOS que el libro, no mas | quien lea `D.30` como *el paso tiene que reproducir el inventario del libro* lo marcaria **defecto de transcripcion**. Yo lo leo como que `PUENTE` es lo que el libro NO dice, y esto lo dice |
| **4** | el `SANO` de `montar_reunion_gran_debate` contra `montar_reunion_gran_decision` | hermanos, y el solape es del libro (`L201`) | **son las señales mas altas de toda la tanda**: `familia_id 0,600` y `paso_contra_nodo 0,726`. Quien mire solo el numero dira gemelos. Lo que me sostiene es `ACTA 27` `2.2`: *una remision hacia atras no es una cabeza* |
| **5** | la **TERCERA madre** de `bloquear_tiempo_pensar_calendario` | la declaro: las tres citan lineas distintas de nodos distintos | **tres madres para un nodo de seis pasos** es mucho. Si alguna de las tres sobra, es esta, que es la del indice |
| **6** | el `SANO` de `preguntar_seguimiento_hallar_huecos` contra `calibrar_normalidad_preguntas_jefe`, **en vez de `MUTUO`** | las dos direcciones apuntan a **la misma linea**, y `A.4` llama a eso solape, no enlace mutuo | es la misma pregunta en los dos libros, con el emisor invertido. **Quien lea la inversion como dos procedimientos distintos veria un `MUTUO`** |
| **7** | **entregar `4` remedios para la `ACTA 28` cuando el encargo dice `2`** | gana mi instrumento y declaro la discrepancia (`X.2.c`): su tabla tiene cuatro filas y los dos que el encargo describe son los de la `ACTA 27` | quien lea *los remedios que el acta escribe DE NUEVO* como criterio diria `2`, porque dos de las cuatro dicen *se mantiene de la `ACTA 27`*. **Yo entrego las cuatro porque la tabla las escribe las cuatro** |
| **8** | exigir que la celda de cabecera sea **exactamente** `REMEDIO` o `REMEDIOS` | es lo que separa la tabla que los escribe de la que habla de ellos (`ACTA 29` `9.4`) | **es una regla estrecha**: un acta que titule la columna *REMEDIO PARA EL SIGUIENTE* no seria vista. Lo que me sostiene es que entonces el instrumento **grita** con su `AVISO` en vez de entregar cero callando |
| **9** | contar la cola de aristas **de la bitacora entera** y no solo las dos filas del encargo | `4` escritas, `3` resueltas, `1` abierta | quien lea la fila del encargo como la cifra oficial vera que publico un numero distinto. **Lo hago porque `ACTA 29` `6.5` dice que esa marca no la lee nadie**, y una cifra que solo vive en una tabla copiada a mano es la que ya se perdio una vez |

"""

x7 = """## X.7. LAS PROPUESTAS (`EXTRACTOR.md` 14: el extractor PROPONE en su reporte, y no se adjudica a si mismo)

### **PROPUESTA 1. LA COLA DE VECINOS SELLADA SIGUE SIN LLEGAR, Y ESTA VUELTA MIDE LO QUE CUESTA**

*Es la propuesta `3` de mi reporte anterior, adjudicada dentro de la `TAREA 2.d` y devuelta aqui con
la cifra de hoy en vez de la de ayer.*

| | |
|---|---:|
| corridas de la aduana dentro de mi turno | **12** (`11` inserciones mas `1` informe cronometrado) |
| segundos por corrida, medido hoy | **`109`** el mas rapido, **`321`** el mas lento |
| minutos de esta vuelta que se fueron en eso | **unos `53`**, de las `17:31` a las `18:24` |
| lo que impidio | **`cap_04` releido**, por tercera vuelta seguida |

**LO QUE PROPONGO, y no lo construyo yo:** que el arnes corra la cola por candidato **antes** del turno
y la entregue sellada, como `D.43` extendida ya manda. **No pido mas candidatos por vuelta**: el propio
`D.43` dice que el coste del instrumento es motivo para pedir menos, no para correr dos a la vez.

### **PROPUESTA 2. `censos/series_y_cabezas.md` LLEVA `0` FILAS CON `267` NODOS DENTRO**

**LA CIFRA:** el fichero tiene `8` lineas y **ninguna es una fila de datos**: solo cabecera y
explicacion. **`EXTRACTOR.md` 9 manda registrar la serie al entrar**, y esta vuelta ha metido **una
cabeza de diez partes** y **una serie de tres bloques**.

**POR QUE NO LO ARREGLO YO:** el propio fichero dice *lo escribe la aduana al insertar. No se edita a
mano salvo para corregir.* La via existe (`insertar --censo serie=...`), pero **se pasa en el acto de
insertar**, y los once ya entraron. **Y `EXTRACTOR.md` 13 me prohibe fabricar el instrumento que lo
rellenaria a posteriori.**

**LO QUE PROPONGO:** que la aduana **pregunte por la serie tambien con `--sin-preguntas`**, o que
declare en su salida que el censo no se escribio. **Hoy el silencio es indistinguible de no haber
serie**, y llevamos `267` nodos sin una sola fila.

### **PROPUESTA 3. LA MARCA `arista_en_cola` SIGUE SIN LECTOR EN EL ARBOL**

`ACTA 29` `6.5` lo midio y esta vuelta lo confirma: **para saber cuantas aristas en cola quedan
abiertas tuve que escribir un lector de vuelta** (`.v31/cola.py`), **que se va con la vuelta.**

**LO QUE PROPONGO:** que `forja.py gate` publique en su linea de salida **cuantas `arista_en_cola`
siguen sin cablear**, que es una cuenta de dos lineas sobre un fichero que ya lee. **No es maquinaria
nueva: es una cifra mas en un instrumento que ya corre en cada commit.**

**LA CIFRA DE HOY, para que la propuesta no vaya desnuda:** `4` escritas, `3` resueltas, **`1`
abierta**.

"""

x8 = """## X.8. EL CIERRE DE LA VUELTA 31

### X.8.a. LAS GUARDAS, CORRIDAS AL CIERRE Y NO AL EMPEZAR

<!-- TALLADO: parcial salida=.v31/guardas_cierre.txt -->

""" + sangrado(".v31/guardas_cierre.txt") + """

### X.8.b. **LAS CIFRAS DEL CIERRE, RECOMPUTADAS AL CIERRE** (`EXTRACTOR.md` 4)

<!-- TALLADO: script=.v31/cuentas_cierre.py salida=.v31/cuentas_cierre.txt -->

""" + tabla(".v31/cuentas_cierre.txt") + """

**LOS `+10` DE ARISTAS CUADRAN AL DIGITO CON LO QUE ESCRIBI:** `9` declaradas por lectura con
`forja.py arista` mas `1` que cablo la aduana al cerrar la cola de `nutrir_ideas_nuevas_reunion_solas`.
**Y los `+16` de la bitacora son esas `9` mas los `7` vecinos juzgados en la tanda.**

**Y LAS `14` LINEAS `no_consumada` NO SE MUEVEN**, que es lo que tiene que pasar: **ninguna corrida
mia quedo a medias.** Las `11` inserciones movieron el censo de `256` a `267` **de una en una y sin un
solo hueco**, y el cerrojo no aviso ni una vez.

### X.8.c. LA IDENTIDAD, LEIDA DE GIT (`EXTRACTOR.md` 5)

<!-- TALLADO: salida=.v31/identidad_cierre.txt -->

RELLENO_IDENTIDAD

### X.8.d. LAS CINCO TAREAS, CON SU ESTADO AL CERRAR

| # | tarea | estado | donde |
|---:|---|---|---|
| **1** | los registros de la `ACTA 29` y sus dos correcciones declaradas | **CERRADA.** Registro anexado, `D.38.4` tachada en su sitio, linea `300` anotada sin tocar la clase | `X.1` |
| **2** | **BLOQUEANTE**: que el arnes entregue los remedios que el acta ESCRIBE | **CERRADA.** Arreglado, caso positivo contra tres actas, `7` pruebas nuevas y la mordida probada contra el codigo viejo | `X.2` |
| **3** | la arista `D.29` que nadie juzgo | **CERRADA.** Cableada y comprobada por los dos extremos en el dato | `X.3` |
| **4** | seguir insertando el lote 4 por `cap_11` | **CERRADA EN EL TRAMO DECLARADO**: `11` de los `14` de `cap_11`, con la arista de `4.d` declarada en el acto. **`3` pasan a la vuelta siguiente y van con su nombre** | `X.4` |
| **5** | la cola entera, recontada fila a fila contra el dato | **CERRADA como tarea.** `1` fila se cierra, `1` nace, y la cola de aristas queda contada de su sede | `X.5` |

**Son CINCO y el tope son cinco** (`EXTRACTOR.md` 1.3). **Ninguna queda a medias.**

> ### **LA VUELTA CIERRA EN `11` DE `14` Y LO DECLARA CON SU CIFRA** (`EXTRACTOR.md` 12.4)
>
> **`11` candidatos contra un tramo de entre `5` y `15`**, y el techo que manda hoy **no es
> `PASOS INVENTADOS`** (que esta en `0,00` y permitiria subir) **sino el reloj de la aduana**: `109`
> segundos la corrida mas rapida y `321` la mas lenta, **unos `53` minutos** de turno.
>
> **LOS TRES QUE QUEDAN VAN CON SU NOMBRE Y NO COMO UN NUMERO:**
> `montar_tablero_kanban_medir_actividades` (`L235` a `L249`),
> `pasear_organizacion_hallar_problemas_pequenios` (`L251` a `L269`) y
> `debatir_decidir_asuntos_cultura_evitar_delegar` (`L301` a `L305`). **Los tres son rotulos `8`, `9`
> y `10` de la cabeza de `cap_11`**, asi que **la vuelta que los inserte cierra tres aristas cabeza a
> parte mas**, y eso ya esta medido en `X.4.e`.

### X.8.e. **LAS SEIS CONDICIONES DE PARADA, REPASADAS UNA A UNA** (`EXTRACTOR.md` 7)

| condicion | lo que mido | veredicto |
|---|---|---|
| algo contradice una regla vigente | **ninguna.** Los casos dudosos (la anchura de las seis aristas del indice, el septimo rotulo que no cablo, el paso `10` que dice menos que el libro) **se resuelven DENTRO de la regla y van marcados como discutibles**, que es lo que `EXTRACTOR.md` 8 manda | **NO ES PARADA** |
| algo contradice una cifra publicada con su corte | **HAY DOS Y LAS DOS SE DECLARAN, que es la salida que `EXTRACTOR.md` 5 escribe para este caso**: el encargo dice `2` remedios para la `ACTA 28` y su tabla tiene `4` (`X.2.c`), y dice `2` aristas en cola cuando hay `4` escritas (`X.5.a`). **Las dos se resuelven midiendo, y en las dos gana mi instrumento y digo por que.** Las once cifras de apertura me salieron al digito | **NO ES PARADA** |
| una operacion cuyo texto no alcanza para ejecutarse sin decidir | **la `TAREA 2` estuvo cerca**, porque su caso positivo describe una tabla que no es la que nombra. **Pero su `2.b` es una sola frase sin dos lecturas** (*los que el acta ESCRIBE, no los que CITA*) **y su prueba acida es exacta** (*no las secciones `3.2` y `6.1`). Lo que falla es un puntero, no el encargo | **NO ES PARADA** |
| un pendiente de doctrina | **hay uno**: si la transcripcion de un INDICE cuenta como enumeracion para `D.29` (discutible `1`). **`EXTRACTOR.md` 7 dice que un pendiente de doctrina NO detiene**: queda marcado y la vuelta sigue | **NO ES PARADA** |
| una guarda en rojo al sellar | **las seis en verde al cerrar** (`X.8.a`), corridas al cierre y no al empezar, y el arbol queda limpio | **NO ES PARADA** |
| una caida de dato | **ninguna.** `11` inserciones, `11` incrementos consecutivos del censo de `256` a `267`, **el cerrojo sin avisar una sola vez**, las `14` lineas `no_consumada` intactas, y **las dos caidas mias de esta vuelta las cace yo y las declare en el acto**: la cifra `0.477` tecleada de memoria dentro de una razon (corregida con `forja.py anotar` en la linea `384`) y el instrumento de la tanda que contaba `18` aristas por filtrar por fecha en vez de por linea | **NO ES PARADA** |

**NINGUNA DE LAS SEIS SE CUMPLE. LA VUELTA 31 CIERRA SIN PARADA Y SIN CAIDA DE DATO DECLARADA.**

### X.8.f. **LO QUE ME CARGO A MI MISMO ANTES DE QUE LO HAGA EL AUDITOR**

*Una vuelta que solo encuentra aciertos propios no esta midiendo.*

| # | lo mio | especie | como salio a la luz |
|---:|---|---|---|
| **1** | **publique `paso_contra_nodo 0.477` dentro de una razon y el instrumento imprimio `0.419`** | **cifra tecleada de memoria** con la salida delante (`EXTRACTOR.md` 5) | **la vi yo al releer la salida**, y la corregi con `forja.py anotar` sobre la linea `384` **antes del commit**, sin tocar la clase. El numero equivocado era el del par que declare tres aristas antes |
| **2** | **mi primer instrumento de la tanda conto `18` aristas declaradas y eran `9`** | **cifra mal filtrada**: use la fecha, y **la vuelta 30 corrio el mismo dia** | **lo vi al cuadrar contra las lineas nuevas de la bitacora**, que no daban. El instrumento lleva el motivo escrito dentro y filtra por linea |
| **3** | **mi primer instrumento de orden dio `0` candidatos de `cap_11`** | **regla copiada sin comprobar**: `cap_11` no escribe el rango como `cap_07` | **lo vi porque la tabla salio vacia**, que es lo que pasa cuando una tabla se genera en vez de teclearse |

**LAS TRES SON DE LA MISMA FAMILIA Y LO DIGO:** las tres son **cifras que habrian pasado si las
hubiera tecleado**, y las tres las caza el mismo metodo. **`D.41` dice que la diferencia no es el
cuidado sino el metodo, y hoy lo he comprobado tres veces en una vuelta.**

"""

for viejo, nuevo in (
        ("## X.6. LOS DISCUTIBLES, MARCADOS ANTES DE SABER SI ACIERTO (`EXTRACTOR.md` 8)\n\nPENDIENTE\n\n", x6),
        ("## X.7. LAS PROPUESTAS\n\nPENDIENTE\n\n", x7),
        ("## X.8. EL CIERRE DE LA VUELTA 31\n\nPENDIENTE\n", x8)):
    assert s.count(viejo) == 1, viejo[:50]
    s = s.replace(viejo, nuevo)

io.open(RUTA, "w", encoding="utf-8", newline="").write(s)
print("ok")
