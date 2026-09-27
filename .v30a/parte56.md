
---

## 5. EL BARRIDO DE VECINOS DE LOS TRECE, UNO POR VEZ

**Metodo:** un candidato por corrida, con su propio id fuera de la poblacion (`ACTA 18`), y
con la correccion de la seccion 2 puesta. **Trece corridas, la misma poblacion en las trece.**

| candidato | vecinos que levanta | que señal los levanta |
|---|---|---|
| `bloquear_tiempo_pensar_calendario` | 5 | familia_id 1, paso_contra_nodo 3, similitud_texto 1 |
| `compartir_logica_mostrar_razonamiento` | 10 | similitud_texto 10 |
| `cuidarse_agotamiento_centro_rueda` | 5 | similitud_texto 5 |
| `establecer_credibilidad_pericia_humildad` | 3 | similitud_texto 3 |
| `fijar_fecha_cierre_debate_equipo` | 4 | paso_contra_nodo 1, similitud_texto 3 |
| `mantener_manos_trabajo_real_equipo` | 8 | similitud_texto 8 |
| `minimizar_impuesto_colaboracion_equipo` | 10 | similitud_texto 10 |
| `parar_debate_emocion_agotamiento` | 9 | similitud_texto 9 |
| `pedir_hechos_decision_evitar_recomendaciones` | 7 | similitud_texto 7 |
| `persuadir_emocion_oyente_no_propia` | 3 | similitud_texto 3 |
| `proteger_tiempo_equipo_jefe` | 10 | paso_contra_nodo 1, similitud_texto 9 |
| `repartir_decision_cercanos_hechos` | 1 | similitud_texto 1 |
| `reservar_calendario_tiempo_ejecutar` | 7 | familia_id 2, similitud_texto 5 |

    $ cat .v30a/barrido2/*.txt | grep -c '^    vecino '
      82

### 5.1. El cruce contra lo que la vuelta escribio, con los ids y sin una sola razon

    $ (cruce de mi barrido ciego contra los pares que la vuelta escribio en la bitacora)
      pares distintos que levanto YO      : 82
      pares distintos que escribio ELLA   : 86
      en los dos                          : 82
      SOLO mios                           : 0
      SOLO suyos                          : 4

      bloquear_tiempo_pensar_calendario       solo suyo: agendar_cuidados_propios_cumplirlos
      cuidarse_agotamiento_centro_rueda       solo suyo: aprender_resultados_vencer_dos_presiones
      mantener_manos_trabajo_real_equipo      solo suyo: minimizar_impuesto_colaboracion_equipo
      reservar_calendario_tiempo_ejecutar     solo suyo: minimizar_impuesto_colaboracion_equipo

> **LECTURA:** **los ochenta y dos pares que levanta mi barrido estan los ochenta y dos entre
> los suyos, y no hay ni uno que solo vea yo.** Los cuatro que solo tiene ella **no los
> levanta ninguna señal**: son los que se ponen leyendo, y tres de los cuatro son la serie que
> yo lei sola en `L373` antes de mirar nada suyo (seccion 4). **Eso es exactamente el reparto
> que `D.19` describe: la señal dice donde mirar, y ahi acaba su trabajo.**
>
> **Y DIGO EL LIMITE DE MI PROPIA MEDIDA:** yo barro contra el grafo **ya terminado**, con
> los trece dentro; ella barrio contra un grafo que crecia nodo a nodo. **Que los dos
> conjuntos coincidan en 82 sin que sobre ninguno por mi lado significa que el orden de
> insercion no le escondio ningun par**, y eso es lo que yo podia comprobar y ella no.

---

## 6. MI DISCUTIBLE 3, QUE ES EL QUE TIENE CONSECUENCIA: **UN PAR CON UN EXTREMO EN LA BANDEJA**

**El par:** `reservar_calendario_tiempo_ejecutar` (entro en esta vuelta, `cap_07` `L385-387`,
rotulo `Block time to execute`) contra `pelear_proliferacion_reuniones_bloquear_ejecucion`
(**sigue en la bandeja**, `cap_11` `L223-233`, rotulo `Fight meeting proliferation`).

**Los dos mandan el mismo acto, y lo mando el mismo libro:**

    cap_07 L385  (rotulo)  Block time to execute
    cap_11 L233            For the same reason I blocked off think-time in calendar; I also
                           found it necessary to block off time in my calendar to be alone
                           and execute. I encouraged others to do the same.

**MI ADJUDICACION, hecha con la vara y sin bascula:** **no son duplicado, son CONTINUA**, y la
direccion es `cap_07` madre y `cap_11` hija. Lo que queda fuera es procedimiento en los dos
lados: la hija trae **los tres remedios que el libro prueba y descarta** (quitar las sillas,
el dia sin reuniones, terminar antes la cuarta parte) y el encargo al equipo; la madre trae
**la causa de por que ese tiempo no aparece nunca en el calendario** (que lo usamos para lo
colaborativo) y lo ata al plan ya decidido y aceptado. **Pero la arista es obligatoria**, y
sin ella el grafo dice dos veces lo mismo sin decir que lo dice dos veces.

### 6.1. Y AQUI ESTA LA CONSECUENCIA, MEDIDA: **NADIE VA A LEVANTAR ESE PAR**

    $ grep "^    vecino " .v30a/barrido2/reservar_calendario_tiempo_ejecutar.txt
      vecino bloquear_tiempo_pensar_calendario      [familia_id]
      vecino proteger_tiempo_equipo_jefe            [similitud_texto]
      vecino cambiar_posicion_hechos_explicar_cambio [similitud_texto]
      vecino mantener_manos_trabajo_real_equipo     [similitud_texto]
      vecino parar_debate_emocion_agotamiento       [similitud_texto]
      vecino reservar_tiempo_reflexion_metas        [familia_id]
      vecino crear_obligacion_disentir_equipo       [similitud_texto]

**Siete vecinos, y `pelear_proliferacion_reuniones_bloquear_ejecucion` no esta**, aunque los
92 de la bandeja estaban dentro de la poblacion. **Asi que lo probe por el otro lado, que es
lo que decide:**

    $ python forja.py informe --carpeta <solo pelear_proliferacion...>
      poblacion del barrido       : 348   (256 del grafo mas 92 que esperan en bandejas)
      EL SALDO
        ENTRARIAN sin leer nada          : 1
        BLOQUEARIAN esperando veredicto  : 0
      vecinos levantados en total      : 0

> **LECTURA, Y ES LA MAS SERIA QUE TRAIGO:** el dia que ese candidato llegue a la puerta,
> **la aduana lo dejara pasar SIN MANDAR LEER NADA**, con el nodo que dice su mismo acto ya
> dentro del grafo. **Las tres señales lo dan por desconocido en las dos direcciones.** No es
> un fallo de esta vuelta: la vuelta 30 no tenia ese candidato delante. **Es un agujero que
> se cierra ahora, con una lectura, o no se cierra nunca**, porque despues de entrar ya no
> habra ninguna corrida que los ponga juntos.
>
> **Y es justo el caso que `D.38.4` puso por escrito:** *un vecino que esta en la bandeja es
> vecino*. Aqui la bandeja estaba en la poblacion **y aun asi la señal no llego**. `D.38.4`
> puso la poblacion correcta; **lo que este par enseña es que la poblacion correcta no basta
> cuando las tres señales no se tocan.**

### 6.2. La otra arista que echo de menos, y esta si tenia los dos extremos dentro

    $ (paso 7 de cuidarse_agotamiento_centro_rueda, que entro a las 14:12)
      Bloquea en tu calendario tiempo de pensar todos los dias. El texto dice que buena parte
      de esa dureza mental venia de hacer cosas como bloquear dos horas de tiempo de pensar al dia.

    $ (entregable de bloquear_tiempo_pensar_calendario, que entro a las 14:18)
      El tiempo para pensar bloqueado en tu calendario y mantenido, con tu equipo avisado de
      que ahi no se agenda y animado a bloquear el suyo.

    $ (aristas de los dos nodos en el grafo)
      cuidarse_agotamiento_centro_rueda  previos=['aprender_resultados_vencer_dos_presiones'] siguientes=[]
      bloquear_tiempo_pensar_calendario  previos=[] siguientes=[]

> **LECTURA:** el paso 7 de uno **nombra el acto que el otro despliega entero**, que es
> palabra por palabra la figura que esta misma vuelta uso para cablear
> `bloquear_tiempo_pensar_calendario` contra el paso 30 del plan de `cap_12`. **La tenia en la
> mano y la aplico en una direccion y no en esta.** Los dos nodos entraron el mismo dia con
> seis minutos de diferencia y el segundo entro **despues**, asi que el primero ya vivia en el
> grafo cuando el segundo paso por la puerta. **Lo marco como par a adjudicar, no como caida:
> puede que haya una razon escrita, y esa razon la destapare en mi turno, de una en una.**
