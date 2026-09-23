

## TAREA 2. `d098`: el paso 1 de `ceder_control_reforzar_competencia_claridad`

**El remedio `4` de la `ACTA M2`, leido entero**
(`docs/loop/archivo/marquet_turn_the_ship/ACTA_AUDITOR_frente_hasta_M2.md`, seccion `10`, punto `4`): *el
paso `1` de `ceder_control_reforzar_competencia_claridad` se reescribe o se retira antes de que ese nodo
entre al grafo (adjudicacion `3` de la `ACTA M1`, que sostengo)*. La adjudicacion `3` de la `ACTA M1`
(misma acta, seccion `6`) dice el porque: el paso describe **como reparte el libro sus Partes**, no es
`PUENTE` (la linea si lo dice), **pero no es procedimiento del lector**: las cuatro fases se nombran por
su numero y lo que se enumera son las Partes del libro, no medios, etapas u objetos de trabajo del lector
(`EXTRACTOR.md` `9.1`, restriccion `1`).

**LA LINEA, CON SU CITA PEGADA** (`D.35`):

    $ sed -n '97p' fuentes/marquet_turn_the_ship/cap_01.md
    97: "Turn the Ship Around! is the story of that journey and the men aboard Santa Fe who lived it with
         me. It describes essentially four phases in my struggle to change the way we interacted for the
         better. I describe how I needed to let go of old ideas to make room for new ones in Part I. In
         Parts II, III, and IV, I describe the bridge to leader-leader and supporting pillars. [...]"

**El paso `1` antiguo** decia: *"Cuenta con las cuatro fases que el texto dice que describe en su lucha
por cambiar la forma de relacionarse, y con como reparte sus partes: la primera en la Parte I, y el puente
y los pilares en las Partes II, III y IV."* Es fiel a la linea (no inventa nada de ella), pero su unico
contenido es la estructura editorial del libro (Parte I, Partes II a IV), que no es algo que el lector
ejecute: no hay verbo de accion propio, solo *"cuenta con"* la division del texto. **NO SUPERA LA VARA DE
`9`**: nombrar la organizacion de un libro no es procedentar.

**RETIRADO, NO REESCRITO**: reescribirlo en clave de accion obligaria a inventar un mandato que la linea no
trae (ponerse a "contar fases" no es algo que alguien haga en su organizacion), lo que seria fabricar un
`PUENTE` nuevo para tapar el que se retira. Ademas, **el contenido accionable de "Parte I" ya lo ejecuta el
paso siguiente**, hoy paso `1`: *"Empieza soltando las ideas viejas para hacer sitio a las nuevas, que es
lo que el texto pone en su primera parte."* Retirar el antiguo paso `1` no pierde ningun mandato del libro:
el nodo pasa de `7` a `6` pasos, los `6` `TRANSCRIPCION` y `0` `PUENTE` (antes `7` `TRANSCRIPCION`, `0`
`PUENTE`; la relectura de fidelidad `D.30` no cambia de numerador, solo de denominador).

**CORRECCION DECLARADA DENTRO DEL PROPIO `resumen_teorico`**, sin borrar el razonamiento anterior, con el
motivo y la cita.

**LA ADUANA, EN EL MISMO ACTO** (`EXTRACTOR.md` `16`), guardada en
`.v7m/aduana/ceder_control_reforzar_competencia_claridad.txt`:

    $ python forja.py informe cuarentena/marquet_turn_the_ship/ceder_control_reforzar_competencia_claridad.json
    ============================================================================
    INFORME DE LA ADUANA EN SECO. CERO INSERCIONES.
    ============================================================================
    candidatos revisados        : 1
    poblacion del barrido       : 479   (346 del grafo mas 133 que esperan en bandejas)
    umbrales de esta corrida    : similitud 0.35 | familia 0.30 | paso contra nodo 0.60

    EL SALDO
      ENTRARIAN sin leer nada          : 0
      BLOQUEARIAN esperando veredicto  : 1   (no es rechazo: es cola de lectura)
      CAERIAN por una guarda           : 0
      CHOCAN entre si dentro del lote  : 0

    LA COLA DE LECTURA QUE ESTE LOTE ABRIRIA
      vecinos levantados en total      : 1
      por candidato bloqueado          : menor 1, mediana 1, mayor 1
      que señal levanta cada vecindad  : similitud_texto 1

    [BLOQUEARIA] ceder_control_reforzar_competencia_claridad   (ceder_control_reforzar_competencia_claridad.json)
        vecino encargar_meta_especifica_dejar_libre_metodo  [levantada por: similitud_texto]
          similitud_texto 0.372 | familia_id 0.000 | paso_contra_nodo 0.486
          paso 4 del candidato contra paso 4 de encargar_meta_especifica_dejar_libre_metodo

**`0` CAERIAN: LA CORRECCION NO ROMPIO NINGUNA GUARDA.** `BLOQUEARIA` por un vecino en
`similitud_texto 0.372`, **por debajo de la banda alta de `0,4`** (`EXTRACTOR.md` `11`), asi que no es de
lectura obligada por esa regla; queda anotado igual porque es la unica vecindad que este candidato levanta.
**NO HAY ADUANA PREVIA DE ESTA FICHA SUELTA QUE COMPARAR** (ni en `.vm01/`, `.m2/`, `.m4aud/` a `.m6aud/`,
ni en `.v3m/` a `.v6m/`): es la primera vez que `ceder_control_reforzar_competencia_claridad` se corre
sola en vez de dentro de un informe de lote, asi que no hay "cual era" que citar, solo "cual es".

**PAGO**: `python scripts/deuda.py --pagar d098 --vuelta 7 --como "paso 1 retirado (meta-estructura del
libro, no procedimiento del lector); nodo queda en 6 pasos, 6 TRANSCRIPCION 0 PUENTE; aduana individual
CERO CAERIAN, BLOQUEARIA por 1 vecino bajo banda alta"`.
