# CUARENTENA: la bandeja de los candidatos ya extraidos

**Aqui se deposita lo que YA es un candidato con forma de nodo y todavia no ha
pasado por la aduana.** Es la bandeja (b) de las dos que
`docs/FLUJO_DE_EXTRACCION.md` fase 0 declara. La bandeja (a), la de los libros
crudos, es `fuentes/<clave>/`.

## Que va aqui y que no

| va aqui | no va aqui |
|---|---|
| un JSON por candidato, con el esquema de `esquema/nodo.schema.json` | el libro crudo, que va a `fuentes/<clave>/` por capitulos |
| material ya extraido por una persona o por una sesion de extraccion | nodos ya insertados, que viven en `dataset/nodos.jsonl` |
| lotes enteros de un mundo o de un libro | el veredicto de nada: eso lo escribe la aduana en `bitacora/VEREDICTOS.jsonl` |

## La convencion de nombre

    cuarentena/<lote>/<id_propuesto>.json

- **`<lote>`** nombra la tanda: `mundo_11`, `hugos_cadena_suministro`,
  `horowitz_cap_3`. Una carpeta por tanda, porque el informe y la insercion
  trabajan por tanda.
- **`<id_propuesto>`** es el `id` que el candidato trae dentro, en snake_case y
  segun `docs/REGLAS_DE_ID.md`. **El nombre del fichero y el campo `id` dicen lo
  mismo**: si no coinciden, manda el campo, y el informe lo dice.

Ejemplo:

    cuarentena/mundo_11/registrar_fuente_canonica.json

## Como se usa, en dos comandos

**1. EL INFORME, primero y siempre.** La aduana en seco, cero inserciones:

    python forja.py informe --carpeta cuarentena/mundo_11

Dice cuantos entrarian, cuantos bloquearian esperando veredicto, cuantos caerian
y por que guarda, con la lista completa. **Ese informe es lo que se lee ANTES de
autorizar la primera insercion.**

**2. LA INSERCION, uno por vez y nunca en masa:**

    python forja.py insertar cuarentena/mundo_11/<id>.json

No existe la carga masiva. Una carga masiva es un veredicto que nadie escribio.

## Por que esta carpeta esta ignorada por git

Los candidatos son **material de entrada, no producto**. Lo que entra queda en
`dataset/nodos.jsonl` con su razon en `bitacora/VEREDICTOS.jsonl`, y esas son
las sedes de verdad. Un candidato que cae por REPITE deja su rastro en la
bitacora y en la operacion de fusion que reparte sus seis perdidas, no en su
fichero.

`.gitignore` ignora `cuarentena/*/` y rescata este LEEME, que si es doctrina.

## El barrido de guiones NO entra aqui, y es a proposito

**Un candidato puede llegar con guiones largos, y no pasa nada:** es
material ajeno esperando juicio. El barrido de estilo cubre lo que esta
casa escribe, no lo que espera en la puerta (D.20). **NO LIMPIES UN
CANDIDATO PARA QUE EL BARRIDO CALLE**: un candidato retocado antes de la
medida es un candidato del que ya no se sabe como llego.

La guarda `guiones` del gate lo mira igual cuando pide entrar, y ahi si
lo tumba. Esa es la sede correcta: la puerta, no la bandeja.

> **DECISION ABIERTA PARA EL FUNDADOR:** si prefiere que los lotes SI viajen en
> el repo (para que un informe que cita un fichero pueda comprobarse contra el
> arbol, que es el espiritu de *la ruta que promete prueba es cifra*), se quita
> una linea del `.gitignore` y ya esta. Se deja ignorada por defecto porque un
> lote son cientos de ficheros de material en bruto.
