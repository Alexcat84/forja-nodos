# -*- coding: utf-8 -*-
"""CIERRA LAS FILAS DE LAS TAREAS 2 Y 3 DEL ESQUELETO Y COMPLETA EL INDICE DE DISCUTIBLES.

El esqueleto se abrio al empezar con las filas vacias (EXTRACTOR.md 3) y cada tarea
anexa la suya al cerrarse. Esto cierra las dos que quedaban y lleva el indice de
discutibles de 3 a 12, que es el que el auditor lee primero.
"""
import io, sys

P = 'docs/loop/REPORTE.md'
t = io.open(P, encoding='utf-8').read()

PARES = [
 ('| 2 | minar con el techo por delante, aduana en seco por candidato | **ABIERTA** | |',
  '| 2 | minar con el techo por delante, aduana en seco por candidato | **CERRADA** | '
  '**6 candidatos** de `cap_03`, uno por vez y en el orden del libro, cada uno con su informe en el '
  'acto: **`0 CAERIA`, `0 ENTRARIA`, `6 BLOQUEARIA`** de cola de lectura. **3 aristas declaradas por '
  'lectura** (`2.d`) y **14 pares con veredicto escrito por vecino** (`2.e`). Tres caidas de puerta '
  'corregidas en el acto (`2.c`) |'),
 ('| 3 | `PASOS INVENTADOS POR CAPITULO` (`D.30`), fila por unidad mas total | **ABIERTA** | |',
  '| 3 | `PASOS INVENTADOS POR CAPITULO` (`D.30`), fila por unidad mas total | **CERRADA** | '
  'tres filas, **las tres releidas y firmadas por mi en esta vuelta**: `0,00` por ciento sobre '
  '**70** pasos, y el freno **NO SE ACTIVA**. Y con el saldo va lo que un `0,00` no dice: **8 '
  'puentes escritos y retirados en el acto** (`3.c`) y **2 fronteras incompletas declaradas** '
  '(`3.d`), una de ellas cazada por el auditor ciego y no por mi |'),
]

INDICE_VIEJO = """| 1 | `R5` (L35) fuera: nombra el sintoma y su techo, y lo tumbo por no poner medio ninguno de deteccion | 1.d |
| 2 | `R7` (L61) fuera **teniendo inventario propio de seis nombrados uno a uno**, por la restriccion 1 de `D.27`: son fines | 1.d |
| 3 | la vuelta mina **UNA** unidad cuando el tramo vigente del lote eran **DOS**, y el motivo es el coste de la aduana, no la cosecha | 1.a y 1.c |
"""

INDICE_NUEVO = """| 1 | `R5` (L35) fuera: nombra el sintoma y su techo, y lo tumbo por no poner medio ninguno de deteccion | 1.d |
| 2 | `R7` (L61) fuera **teniendo inventario propio de seis nombrados uno a uno**, por la restriccion 1 de `D.27`: son fines | 1.d |
| 3 | la vuelta mina **UNA** unidad cuando el tramo vigente del lote eran **DOS**, y el motivo es el coste de la aduana, no la cosecha | 1.a y 1.c |
| 4 | `recorrer_organizacion_escuchar_plantilla` paso `1`: convierto en paso la **pregunta retorica** que el libro dirige al lector | resumen del candidato |
| 5 | `recorrer_organizacion_escuchar_plantilla` paso `7`: lleva pegada una **consecuencia observada** y no una instruccion | resumen del candidato |
| 6 | `observar_reunion_rutinaria_senales_plantilla`: la **activacion sale de `R3`**, pieza que yo mismo clasifique `RESIDUO` | resumen del candidato |
| 7 | `seguir_frustrado_preguntar_implantacion_ideas` paso `2`: *sin pregunta y sin acusacion* es **mi glosa de la forma** de la frase citada | resumen del candidato |
| 8 | `contar_firmas_cadena_tramite_parado` paso `5`: `department chief` y `department head` transcritos como **dos puestos** que en castellano se dicen igual | resumen del candidato |
| 9 | `inspeccionar_reparto_informacion_notas_jefe` pasos `7` y `8`: son *quedate con*, o sea **lectura y no acto** | resumen del candidato |
| 10 | `auditar_formacion_premios_ultima_fila` paso `9`: arrastra **la valoracion del autor** pegada al objeto | resumen del candidato |
| 11 | la arista `C`: **la madre no enumera al hijo** y el libro no dice cuantas rutinas hay | 2.d |
| 12 | la deuda de `D.37` de `cap_01`: **la cuenta de cuatro es del libro, el desdoble de los dos pilares lo hago yo** | 2.d.2 |

**DOCE, y el detalle de cada uno esta en `C.4`.**
"""

for viejo, nuevo in PARES:
    if t.count(viejo) != 1:
        sys.exit('NO ENCONTRADA (o repetida) la fila: %s' % viejo[:60])
    t = t.replace(viejo, nuevo)

if t.count(INDICE_VIEJO) != 1:
    sys.exit('NO ENCONTRADO el indice de discutibles de la apertura')
t = t.replace(INDICE_VIEJO, INDICE_NUEVO)

io.open(P, 'w', encoding='utf-8', newline='\n').write(t)
print('FILAS CERRADAS: tarea 2, tarea 3, e indice de discutibles de 3 a 12')
