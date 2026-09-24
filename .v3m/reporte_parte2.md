# TAREA 2. BLOQUEANTE: PAGAR EL PUENTE VIVO DE `cap_06` (`D.30`, `D.55`)

## 2.a. La cita del puente, con su `sed` pegado

    $ sed -n '113p' fuentes/marquet_turn_the_ship/cap_06.md
    When I've conducted this exercise, I usually find that the worries fall into two broad
    categories: issues of competence and issues of clarity. People are worried that the next
    level down won't make good decisions, either because they lack the technical competence
    about the subject or because they don't understand what the organization is trying to
    accomplish. Both of these can be resolved.

    $ sed -n '111p' fuentes/marquet_turn_the_ship/cap_06.md
    Last, when the group reconvenes, sort and rank the worries and begin to attack them.

**EL LIBRO OBSERVA, EL PASO MANDA.** `L113` cuenta lo que al autor le sale cuando conduce el ejercicio;
no encarga al lector leer ni clasificar nada. La etapa de ordenar y clasificar ya esta escrita, y es el
paso `6`, que sale de `L111`. Adjudicado PUENTE por el auditor en `ACTA M3` `M3.7.2`, con el ejemplar
gemelo de la propia `ACTA M2` `4.2` delante (*separa lo que entra por sus clases*, tambien PUENTE sobre
una linea que describe, no manda).

## 2.b. La salida elegida: SE RETIRA, y no se reescribe

**De las dos salidas limpias que el encargo ofrece, elijo RETIRARLO.** El paso `7` no anade una etapa
nueva del ejercicio: es la observacion del autor sobre el resultado tipico de aplicarlo, y esa
observacion no encarga ninguna accion que el paso `6` (ordenar y clasificar) no encargue ya. Reescribirlo
sin imperativo lo dejaria como una frase descriptiva metida dentro de una lista de pasos accionables,
que es el sitio equivocado para una observacion; retirarlo es lo que deja el ejercicio con solo lo que
el libro manda hacer.

**LA OPERACION, SOBRE EL CANDIDATO EN CUARENTENA Y NO SOBRE EL DATASET:** `scripts/retirar_paso.py`
opera sobre `dataset/nodos.jsonl` (nodos ya insertados, `D.54`), y este candidato **nunca ha entrado al
grafo**: sigue en `cuarentena/marquet_turn_the_ship/aplicar_ejercicio_codigo_genetico_control.json`, que
es la sede propia del extractor para sus candidatos (`EXTRACTOR.md` 14 y 16). Por eso la retirada se
aplica editando el propio JSON de cuarentena, no con ese script, y queda declarada dentro de su
`resumen_teorico` con la cita completa, el motivo y el texto literal del paso retirado, para que no se
pierda lo que decia (el mismo principio de `D.54`, aplicado a donde este candidato realmente vive).

## 2.c. El resultado, verificado

    $ python -c "import json; d=json.load(open('cuarentena/marquet_turn_the_ship/aplicar_ejercicio_codigo_genetico_control.json', encoding='utf-8')); print(len(d['pasos_accionables']))"
    6

**Los pasos pasan de `7` a `6`.** Los seis que quedan son los seis TRANSCRIPCION que ni la vuelta 2 ni
el auditor cuestionaron (`ACTA M3` `M3.7.1`: las seis lineas enumeradas del libro, una a una y en su
orden, `L101`, `L103`, `L105`, `L107`, `L109`, `L111`). **RELECTURA DE FIDELIDAD `D.30` TRAS LA
CORRECCION: 6 pasos, 6 TRANSCRIPCION, 0 PUENTE.**

    $ python forja.py guiones cuarentena/marquet_turn_the_ship/aplicar_ejercicio_codigo_genetico_control.json
    BARRIDO DE GUIONES VERDE: cero guiones largos y cero guiones medios.
---
