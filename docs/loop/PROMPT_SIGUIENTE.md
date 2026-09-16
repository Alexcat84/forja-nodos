# ENCARGO DE LA VUELTA 26: **SEGUIR INSERTANDO EL LOTE 4, Y ABRIR EL LOTE 5 POR SU ORDEN**

*Escrito por el **auditor** al cerrar la **ACTA 25** y reescrito con la decision del
fundador del 15 sep 2026, archivada en
`docs/loop/paradas/2026-09-15-la-ruta-vacia-DECISION.md`. Sede del auditor por
`AUDITOR_FORJA.md` 5.6.*

**Commitea y pushea lo pendiente en la rama activa antes de tocar nada.**

---

## LO QUE LA PARADA DEJA DECIDIDO, EN CINCO LINEAS

- **TU RACHA `REPORTE` SE REINICIA A 0 DE 3**, con `D.42` instalada y corriendo en el
  hook. **No es un indulto: es una condicion mecanica encima**, como `D.40` y `D.41`.
- **LA CIFRA DE LA CAIDA YA ESTA CORREGIDA POR REGENERACION** (`2` pasa a `4`, del
  instrumento de hoy) con su correccion declarada en `S.3.e`. **No la rehagas.**
- **`D.42`, LA UNIDAD DE LA RUTA ES LA CELDA.** Toda ruta que publiques como sede de
  una cifra se comprueba **en cada commit**. Tres formas y solo tres, y estan en la
  TAREA 1.
- **EL CENSO DE LAS AUSENTES YA SE CORRIO Y SE PUBLICO** (punto 3 de la decision):
  **cero rutas de verdad perdidas.** Esta entero en la cabecera de la parada.
- **LA VUELTA 25 FUE LA MEJOR VERIFICADA DE LA CAMPANIA**, y lo dice tu auditor: todo
  lo que recomputo salio al digito, cero caidas de clase, 10 discutibles sostenidos.

---

## TAREA 1: **`D.42` ES COMO SE TRABAJA A PARTIR DE HOY**

*No es trabajo de la vuelta: es la condicion de tu reinicio. Va primera porque si la
rompes, el commit no pasa.*

> **TODA RUTA QUE PUBLIQUES COMO SEDE DE UNA CIFRA TIENE QUE SOSTENERLA. LA UNIDAD ES
> LA CELDA.**

| forma | que hace el censo |
|---|---|
| **(a)** la ruta tiene contenido | pasa |
| **(b)** la ruta esta vacia, o no esta | **TUMBA EL COMMIT**, salvo que escribas en la MISMA celda `VACIA A PROPOSITO: <motivo>` |
| **(c)** era un conjunto | escribela `PATRON: <glob>`, y tiene que tener **al menos una coincidencia con contenido** |

**LO QUE CASI SIEMPRE TOCA ES LA PRIMERA: guardar la salida del instrumento en su
fichero antes de citarlo.** La marca no es un comodin: **lleva motivo escrito, va al
lado del numero que sostiene, y cada corrida la cuenta y la publica.** Una marca puesta
sin mirar se ve en el recuento.

**Y NO CENSA TODA MENCION:** una frase que **habla** de un fichero no es una sede. Lo
que se cuenta es la celda que **es** la ruta (la columna *de donde sale*) o la que la
**ofrece como origen** (*salida de*, *guardada en*, *su testigo lo prueba*).

**Al cerrar la vuelta:** `python scripts/cerrar_reporte.py`, que corre el tallado
(`D.41`) en estricto, el censo (`D.42`) y las cinco guardas.

---

## TAREA 2: **SEGUIR INSERTANDO EL LOTE 4**

*La vuelta 25 abrio la insercion y entraron 8 nodos. Queda la mayor parte.*

| | |
|---|---:|
| candidatos del lote 4 en bandeja | **123** |
| ya insertados y archivados | **19** de 142 |
| nodos en el grafo | **222** |
| veredictos en bitacora | **203** |

**COMO SE INSERTA, y no ha cambiado:** `python forja.py insertar`, **un candidato por
vez**, en el orden que lee (`D.36`), **con su veredicto escrito por vecino antes de
insertar**, los veredictos a `bitacora/VEREDICTOS.jsonl` y los insertados a
`cuarentena/_insertados/scott_radical_candor/` en el mismo acto (`D.31`).

**LAS ARISTAS SE CABLEAN AL ENTRAR SUS NODOS** (`D.29`, `D.37`), que es lo que la
vuelta 25 estreno: **dos aristas entraron con su nodo en el mismo acto de la aduana**,
y esa es la forma buena. La deuda declarada y sin cablear era **79** al cerrar la 25.

> ### **LA COLA NO SE VACIA, SE REALIMENTA**, y lo descubriste tu en la vuelta 25
>
> Cada nodo que entra **cambia lo que mide el siguiente**, y levanta vecinos que antes
> no existian. **Una cifra de cola envejece dentro de su propia vuelta**, que es
> exactamente como nacio la caida que paro el bucle. **Publica la cola con su fichero
> al lado y regenerala antes de cerrar.**

**Y LA COLA HEREDADA QUE SE TE DEBE:** `decidir_momento_despedir_persona` tiene **4
pares por leer**, regenerados el 15 sep y guardados en `.v25/cola_lectura.txt`:
`despedir_persona_franqueza_radical`, `pedir_critica_equipo_premiarla`,
`despedir_persona_respeto_franqueza` y `elegir_recolocar_despedir_persona`. **Citalos
de ahi; no los recuentes de memoria.**

---

## TAREA 3: **ABRIR EL LOTE 5 POR EL ORDEN ESCRITO**

| | |
|---|---:|
| lote 5 | `marquet_turn_the_ship` |
| unidades | **17** |
| palabras | **33.702** |
| minadas ya | **2** (`cap_01` y `cap_02`, con sus dos fronteras cerradas al digito) |
| candidatos en bandeja | **3** |

**EL ORDEN LO FIJA `docs/loop/ORDEN_DE_LOTES.md` y no lo elige la vuelta** (`D.24`).

**EL VOLUMEN Y EL TECHO, los dos vigentes:**

- **el tramo del lote**, con el freno de `PASOS INVENTADOS` publicado fila por capitulo
  mas total, y la escalada decidida **sobre el peor capitulo** (mi `8.2`);
- **y el techo de candidatos por vuelta, que manda sobre el de capitulos**
  (`EXTRACTOR.md` 12.4): **si un capitulo lo pasa, la vuelta cierra ahi y lo declaras
  con su cifra.**

**LA FRONTERA SE CIERRA CONTRA EL CUERPO O NO SE PUBLICA CUENTA DE NODOS**, y su tabla
va **pegada de su instrumento** (`D.41`), con la salida guardada en un fichero (`D.42`).

---

## SON TRES TAREAS Y EL TOPE SON CINCO

**Si la insercion del lote 4 se come la vuelta, la vuelta se cierra ahi y lo declaras
con su cifra.** Abrir el lote 5 con medio lote 4 dentro no adelanta nada: **lo que
cierra un lote es insertarlo entero.**

## LAS PARADAS

**Las de `AUDITOR_FORJA.md` 3 estan enteras.** Lo nuevo es que **el hook aborta el
commit** si una tabla no coincide con su instrumento (`D.41`) o si una ruta publicada
como sede no sostiene nada (`D.42`). **Eso no es una parada del bucle**: es un commit
que no pasa, y se arregla en el acto.
