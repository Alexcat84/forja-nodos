# LOTE 2 `smart_who`, PRIMERA TANDA: 44 CANDIDATOS INSERTADOS

**Archivados el 10 sep 2026.** Estos 44 ficheros **ya no son candidatos**: sus
nodos viven en `dataset/nodos.jsonl`. Se guardan porque **el fichero de cuarentena
es el registro de COMO entro cada uno** (`D.31`).

**Todos entraron en el mismo commit**, con la autorizacion del fundador del 10 sep
2026 y `MODO_INSERCION=insertar`. **El grafo paso de 8 a 52 nodos.**

## El orden, y por que no fue el alfabetico

**Se inserto en el orden del informe (alfabetico) con UNA excepcion medida**, que
es `D.36`, **EL ORDEN QUE LEE**:

    celebrar_aceptacion_primer_dia -> sostener_contacto_oferta_aceptacion : 0,613  LEVANTA
    sostener_contacto_oferta_aceptacion -> celebrar_aceptacion_primer_dia : 0,587  NO levanta

`difflib` no es simetrico, y aqui esa asimetria **no mueve un decimal: mueve si el
par llega a leerse.** Alfabeticamente `celebrar` va antes que `sostener`, y en ese
orden **el par no habria pedido veredicto nunca**. Se metio
`sostener_contacto_oferta_aceptacion` **justo delante** de
`celebrar_aceptacion_primer_dia`, y el par pidio su veredicto.

## Lo que la aduana levanto

| | |
|---|---:|
| candidatos insertados | **44** |
| que bloquearon pidiendo veredicto | **16** |
| **veredictos escritos** | **30** |
| de ellos `CONTINUA`, con arista cableada | **7** |
| de ellos `SANO` | **23** |
| `REPITE` | **0** |

**Las siete aristas, todas madre e hijo de una serie con cabeza declarada:**

    crear_tarjeta_puntuacion_puesto > alinear_comunicar_tarjeta_puntuacion
    crear_tarjeta_puntuacion_puesto > definir_resultados_tarjeta_puntuacion
    crear_tarjeta_puntuacion_puesto > identificar_competencias_tarjeta_puntuacion
    crear_tarjeta_puntuacion_puesto > redactar_mision_tarjeta_puntuacion
    abastecer_flujo_candidatos      > pedir_referencias_empleados
    seleccionar_jugador_cuatro_entrevistas > decidir_contratacion_final
    seleccionar_jugador_cuatro_entrevistas > calificar_tarjeta_puntuacion_habilidad_voluntad

**Cada una con su razon escrita en `bitacora/VEREDICTOS.jsonl`**, citando el paso
de la cabeza que el hijo despliega. Es el manual seccion 3.4 funcionando: **un
nodo por paso mas UNA cabeza.**

## Que se puede y que no

| se puede | no se puede |
|---|---|
| **comparar** el candidato archivado con el nodo vivo, para ver que le hizo la aduana al entrar | **reinsertarlos**: la aduana los rechaza por `el id ya vive en el grafo`, y hace bien |
| leer como estaban escritos, con `git log` sobre estos ficheros | **editarlos**: un registro que se retoca deja de ser un registro |

    python forja.py informe --carpeta cuarentena/_insertados/smart_who
      44 ficheros ARCHIVADOS en cuarentena/_insertados: ya viven en el grafo,
      y el informe no los cuenta (D.31).
