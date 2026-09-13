
---

## O.2. TAREA 1: LOS REGISTROS, Y LO QUE CAMBIO DEBAJO DE MI. **CERRADA**

### O.2.a. LA `ACTA 20`, LEIDA ENTERA Y SITUADA CON SU LINEA (`D.35`)

    $ grep -n "^# ACTA 20" docs/loop/ACTA_AUDITOR.md
      18136:# ACTA 20. VUELTA 20, lote 4 (scott_radical_candor), cap_09 CERRADO y cap_10
             cortado: la vuelta del extractor sale limpia de clase, la frontera de cap_10
             se adjudica en 13 y no en 20, y MI PROPIA RACHA LLEGA A 3 DE 3
    $ wc -l docs/loop/ACTA_AUDITOR.md
      18928

**Leida entera, de `L18136` a `L18928`.** Sus **siete adjudicaciones** las recojo **sin
reabrirlas** (`1.a` del encargo), y las que me tocan a mi son las seis de `cap_10`:

| # | adjudicacion | donde | la recojo |
|---:|---|---|---|
| **1** | **la vara del corte: un nodo por cada par (condicion de activacion, entregable)**; la cuenta escrita **no corta**, solo decide si la arista es `D.37` o `D.29` | `4.1` | **SI**, y es la que uso en las trece piezas de `O.3` |
| **2** | `L93` a `L125`, el plan de crecimiento: **UN** nodo y no cinco. Su `P13` no es cabeza aparte | `4.2` | **SI** |
| **3** | `L225` a `L251`, recompensar sin ascender: **DOS** nodos. Ni sus cuatro ni el uno del auditor | `4.3` | **SI** |
| **4** | `L129`, la proporcion de estrellas: **NO da nodo**, y su acto viaja dentro del de contratacion | `4.4` | **SI** |
| **5** | `L169` a `L201`, despedir: **cabeza mas tres mas coda**. Mi corte de la vuelta 20 gana | `4.5` | **SI** |
| **6** | **la frontera de la casa para `cap_10` es 13** | `4.6` | **SI** |
| **7** | `ultimo_apertura.json` es artefacto de maquina por `D.33` | `4.7` | no es mia: se resolvio en la parada, punto 1 |

**Y RECOJO TAMBIEN LAS DOS FILAS QUE HABLAN DE MI TRABAJO, sin discutirlas:** mis nueve
discutibles releidos uno a uno (**seis se sostienen, dos caen, uno a medias**), **cero caidas de
`CLASE` y cero de `CIFRA PUBLICADA`**, y **una caida de especie `REPORTE` registrada que NO
acumula**: la fila `.t1_v20/` de mi `O.6.7` decia `13` guiones donde hoy hay `16`.

> ### **NO REABRO NINGUNA. EL UNICO HECHO NUEVO QUE TRAIGO ESTA EN `O.4`, Y ES DEL INSTRUMENTO: `forja.py arista` NO PUEDE CABLEAR UNA ARISTA CUYOS DOS EXTREMOS VIVEN EN CUARENTENA. LO MIDO EN VEZ DE SUPONERLO.**

### O.2.b. LA PARADA ARCHIVADA, Y SUS CUATRO DECISIONES LITERALES

    $ ls docs/loop/paradas/ | tail -3
      2026-09-12-d40-falso-positivo.md
      2026-09-12-el-artefacto-que-faltaba.md
      2026-09-12-la-fase-ciega-lee-el-acta.md
    $ grep -n "LAS CUATRO DECISIONES DEL FUNDADOR" docs/loop/paradas/2026-09-12-el-artefacto-que-faltaba.md
      3:> ## LAS CUATRO DECISIONES DEL FUNDADOR, 12 sep 2026

**Leida entera.** Las cuatro, con lo que cada una me cambia a mi:

| # | la decision | lo que me cambia |
|---:|---|---|
| **1** | la racha del auditor se reinicia **por reclasificacion, no por indulto**; `D.33` se ensancha **POR PATRON**; `D.38.2` se acota a **sustancia de auditoria** | **ningun `docs/loop/ultimo_*.json` puede volver a dejarme el arbol en rojo al arrancar.** Comprobado en `O.2.c` |
| **2** | el informe de lote **sale del turno** y lo corre el arnes, sellado | **no lo recomputo y no lo lanzo.** Ver `O.2.d` |
| **3** | la poblacion del informe es **grafo mas bandejas** tambien para la aduana; **y el par de `cap_10` `L225` a `L251` contra `reconocer_recompensar_gente_estable` se declara por lectura como `CONTINUA` con arista, en la misma vuelta** | es mi TAREA 4 entera (`O.5`) |
| **4** | el `PROMPT_SIGUIENTE` de la vuelta 21: `cap_10` entero, las tres `D.37` de `L173`, la coda `P28` fuera, el par de la lupa, **sin insercion porque el lote sigue abierto** | es el encargo que ejecuto |

**Y LA LEO COMO DOCTRINA FIRMADA QUE MANDA SOBRE EL ENCARGO** (`1.b` literal). Donde el encargo y
la parada dicen lo mismo, cito la parada.

### O.2.c. LAS OCHO SEDES QUE CAMBIARON, **ABIERTAS UNA A UNA Y NO CREIDAS** (`EXTRACTOR.md` 5)

    $ grep -n "PATRONES_DE_ARTEFACTO\|def es_artefacto_de_maquina" src/comun.py
      268:PATRONES_DE_ARTEFACTO = ("ultimo_*.json",)
      272:def es_artefacto_de_maquina(nombre, carpeta):
      283:    return any(fnmatch.fnmatch(nombre, patron) for patron in PATRONES_DE_ARTEFACTO)
    $ grep -n "D.33\|D.41" docs/BANCO_DE_REGLAS.md | head -4
      1032:## D.33. LOS ARTEFACTOS DEL ARNES SON REGISTRO DE MAQUINA, Y NO SE BARREN
      1404:> tercera caida de la racha de la vuelta 20 no era REMEDIO ROTO: era D.33,
      1820:## D.41. EL INFORME DE LOTE VIVE DONDE CABE, Y NO CABE EN UN TURNO
    $ grep -n "^### D.38.5" docs/BANCO_DE_REGLAS.md
      1573:### D.38.5. LA POBLACION DEL BARRIDO ES GRAFO MAS BANDEJAS TAMBIEN PARA LA ADUANA
    $ grep -n "CARPETAS_FUERA_DE_POBLACION\|class Poblacion" src/informe.py
      118:CARPETAS_FUERA_DE_POBLACION = ("_insertados", "_derivadas")
      122:class Poblacion(object):
    $ grep -n "INFORME_DE_LOTE" orquestador_forja.sh | head -3
      100:INFORME_DE_LOTE="${INFORME_DE_LOTE:-}"
      376:INFORME_LOTE_FICHERO="$LOOP/INFORME_DE_LOTE.txt"
      411:  if [ -z "$INFORME_DE_LOTE" ]; then

**LAS OCHO ESTAN Y LAS OCHO DICEN LO QUE EL ENCARGO DICE.** Dos me cambian el trabajo de hoy, asi
que las escribo con su consecuencia y no solo con su linea:

| sede | lo que leo hoy | lo que me cambia |
|---|---|---|
| `src/comun.py:268` | la lista de tres nombres **ya no existe**: es **un patron**, `ultimo_*.json` | mi arbol arranco limpio: el commit de pendientes de `EXTRACTOR.md` 1.1 llevaba `ultimo_extractor.json` dentro **y el hook salio verde** |
| `src/informe.py:118` y `122` | la poblacion descarta `_insertados` y `_derivadas`, **y descarta `ensayo_referencia_163` por su tabla de fuentes y no por su nombre**; la clase `Poblacion` publica **las dos mitades** | mi poblacion de hoy es **203 del grafo mas los que esperan en la bandeja del lote 4**, y **crece con cada candidato que escribo**: el numero trece se mide contra doce vecinos mas que el primero |

> ### **Y LA CONSECUENCIA QUE `D.38.5` ME DEJA ENCIMA DE LA MESA, DICHA ANTES DE MEDIRLA: ESPERO MAS `BLOQUEARIA` QUE EN NINGUNA VUELTA ANTERIOR, Y ESO NO ES QUE MIS CANDIDATOS HAYAN EMPEORADO.**
> Es cola de lectura que hasta ayer era invisible. Lo escribo **antes** de correr el primer
> informe, para que no se lea como una excusa escrita despues.

### O.2.d. **LA CIFRA QUE SE ME DEBE Y QUE NO PUEDO PAGAR YO** (`1.d` del encargo)

*El encargo dice: si el prompt trae el fichero sellado, citalo por su sello; **si no lo trae,
declara en tu reporte que esta vuelta no trae saldo de lote y por que, y NO LO LANCES TU.***

    $ ls docs/loop/INFORME_DE_LOTE.txt docs/loop/SELLOS_INFORME.jsonl
      ls: cannot access 'docs/loop/INFORME_DE_LOTE.txt': No such file or directory
      ls: cannot access 'docs/loop/SELLOS_INFORME.jsonl': No such file or directory
    $ grep -n "INFORME DE LOTE" docs/loop/loop.log | tail -1
      376:[2026-09-12 20:14:11] VUELTA 1 : SIN INFORME DE LOTE en esta corrida (INFORME_DE_LOTE vacio)

> ### **ESTA VUELTA NO TRAE SALDO DE LOTE, Y EL MOTIVO NO ES UN OLVIDO: ES QUE LA CORRIDA NO LO PIDIO.**
>
> **Los dos ficheros que `D.41` nombra NO EXISTEN en el arbol**, y **el propio arnes lo dejo
> escrito en su log** con la letra que `D.41` manda (*sin lote que informar el paso se salta Y SE
> REGISTRA en el log, porque un paso que se salta en silencio es un paso que nadie puede echar en
> falta*). **La corrida se lanzo sin `INFORME_DE_LOTE`.**
>
> **NO LO LANZO YO, Y NO ES PEREZA: ES LA LETRA DE `D.41`.** El informe de los 83 cuesta **156,5 s
> por candidato** medidos por el fundador, o sea **mas de tres horas**; la vuelta 20 lo intento y
> lo dejo en **480 bytes**. **Una cifra que no cabe en un turno no se firma en un turno.**
>
> **LO QUE ESTO ME DEJA SIN PODER DECIR, dicho por su nombre:** no publico `CHOCAN entre si dentro
> del lote`, que es **la unica cifra que un informe de uno en uno no ve**. Los informes de `O.3`
> son de **uno en uno** y esos si son mios, en el mismo acto de escribir cada candidato
> (`EXTRACTOR.md` 12 y 16, `D.41` ultima linea).
>
> **SE QUEDA EN COLA PARA LA VUELTA SIGUIENTE**, que es lo unico que el encargo autoriza a pasar:
> *lo unico que puede pasar a la siguiente es la `1.d`, si el arnes no trajo informe.*
