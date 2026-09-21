
### VV.5.b. **EL SALDO, CANDIDATO A CANDIDATO, LEIDO DE LA SALIDA DE CADA PASADA**

<!-- TALLADO: script=.v55ext/saldo_uno_a_uno.py salida=.v55ext/saldo_uno_a_uno.txt -->
| capitulo | pieza | candidato | pasos | veredicto en seco | poblacion | vecinos | reloj |
|---|---|---|---:|---|---:|---:|---:|
| `cap_07` | `P5` | `planificar_tres_pasos_demanda_estado_brecha` | 6 | escrito y pasado por la VUELTA 53, no por esta | | | |
| `cap_07` | `P8` | `definir_entorno_grupo_clientes_proveedores_competidores` | 6 | **BLOQUEARIA** | 415 (346 mas 69) | 2 | 169,9 s |
| `cap_07` | `P9` | `examinar_entorno_expectativas_tecnologia_proveedores_grupos` | 5 | **BLOQUEARIA** | 420 (346 mas 74) | 4 | 189,1 s |
| `cap_07` | `P10` | `examinar_demanda_entorno_dos_marcos_temporales` | 7 | **BLOQUEARIA** | 422 (346 mas 76) | 4 | 204,5 s |
| `cap_07` | `P12` | `determinar_estado_presente_capacidades_proyectos_merma` | 7 | **BLOQUEARIA** | 423 (346 mas 77) | 5 | 205,1 s |
| `cap_07` | `P14` | `cerrar_brecha_dos_preguntas_estrategia` | 7 | **BLOQUEARIA** | 423 (346 mas 77) | 11 | 175,3 s |
| `cap_07` | `P22` | `fijar_horizonte_ventana_replanificacion` | 5 | **BLOQUEARIA** | 423 (346 mas 77) | 3 | 212,3 s |
| `cap_07` | `P27` | `contestar_dos_preguntas_direccion_objetivos` | 5 | **BLOQUEARIA** | 423 (346 mas 77) | 7 | 139,7 s |
| `cap_07` | `P29` | `fijar_periodo_direccion_objetivos_retroalimentacion` | 5 | **BLOQUEARIA** | 423 (346 mas 77) | 1 | 201,6 s |
| `cap_10` | `P17` | `repartir_supervision_puesto_funcional_mision` | 8 | **ENTRARIA** | 423 (346 mas 77) | 0 | 273,6 s |

<!-- TALLADO: parcial script=.v55ext/saldo_uno_a_uno.py salida=.v55ext/saldo_uno_a_uno.txt -->

    PASADAS DE ADUANA CORRIDAS EN ESTA VUELTA, una por candidato nuevo : 9
    CANDIDATOS QUE CAERIAN POR UNA GUARDA                              : 0
    CANDIDATOS QUE BLOQUEARIAN (cola de lectura, no rechazo)           : 8
    RELOJ SUMADO DE LAS PASADAS                                        : 1771,1 s
    RELOJ MEDIO POR PASADA                                             : 196,8 s

> **CERO `CAERIAN` EN LOS NUEVE.** Y `BLOQUEARIA` **no es rechazo**: es cola de lectura, y
> `D.38.5` ya avisa de que la poblacion es **grafo mas bandejas**, asi que un par cuyos dos
> extremos viven en cuarentena **se levanta igual**. Lo que la tabla dice es que **hay
> vecindades que leer el dia de la insercion**, no que mis candidatos sean peores.

**EL UNICO `ENTRARIA` ES EL DE `cap_10`, y es la fila que mas me interesa de todas**: el nodo
que mas me juego (discutible `2`) es tambien **el unico que ninguna senial empareja con nada**.
Es literalmente el aviso de `EXTRACTOR.md` 11: **un candidato con la cola vacia esta
certificado como SIN GEMELO, no como SIN MADRE.** Su madre, si la tiene, la tiene que
encontrar la lectura, y en `VV.5.a` digo cual creo que NO es.
