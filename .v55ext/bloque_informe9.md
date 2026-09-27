
### VV.9.a. **EL INFORME DE LOTE DE LOS `9` DE ESTA VUELTA, CON SU SALDO Y SU `CHOCAN`**

<!-- TALLADO: parcial salida=.v55ext/informe_lote_v55.txt -->

    $ python forja.py informe --carpeta .v55ext/lote_v55
    ============================================================================
    INFORME DE LA ADUANA EN SECO. CERO INSERCIONES.
    ============================================================================
    candidatos revisados        : 9
    poblacion del barrido       : 423   (346 del grafo mas 77 que esperan en bandejas)
    umbrales de esta corrida    : similitud 0.35 | familia 0.30 | paso contra nodo 0.60

    EL SALDO
      ENTRARIAN sin leer nada          : 1
      BLOQUEARIAN esperando veredicto  : 8   (no es rechazo: es cola de lectura)
      CAERIAN por una guarda           : 0
      CHOCAN entre si dentro del lote  : 0

    LA COLA DE LECTURA QUE ESTE LOTE ABRIRIA
      vecinos levantados en total      : 43
      por candidato bloqueado          : menor 1, mediana 6, mayor 11
      que señal levanta cada vecindad  : familia_id 2, paso_contra_nodo 5, similitud_texto 40


**Y SU RELOJ, que es la mitad de la cifra** (`.v55ext/informe_lote_v55.txt`):

    INICIO 2026-09-20T15:06:43-04:00
    real	31m29.389s
    FIN 2026-09-20T15:38:13-04:00

> **`CHOCAN entre si dentro del lote: 0`. Esa es la unica cifra que un informe de uno en uno
> no puede ver**, y por eso valia la pena correrlo aunque fuera sobre `9` y no sobre `74`:
> **mis nueve candidatos no se pisan entre ellos.**
>
> **Y EL SALDO COINCIDE AL DIGITO CON LAS NUEVE PASADAS SUELTAS DE `VV.5.b`**: `1 ENTRARIAN`,
> `8 BLOQUEARIAN`, `0 CAERIAN`. **Dos instrumentos distintos sobre el mismo material dan lo
> mismo**, y eso es la comprobacion que ninguno de los dos se da a si mismo.
>
> **LA COLA DE LECTURA QUE ESTO ABRE PARA EL DIA DE LA INSERCION: `43` vecindades**, con la
> mediana en `6` y el mayor en `11`. **No es rechazo, es trabajo**, y es trabajo que `D.39`
> pone donde toca: el dia que el lote cierre y entre, no hoy.
