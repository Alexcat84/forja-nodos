# -*- coding: utf-8 -*-
"""LA DEUDA DE ARISTAS AL CERRAR LA VUELTA 24.

QUE CUENTA ESTE GUION Y QUE NO, y va antes de la tabla porque decide como se lee.
CUENTA las filas numeradas de las secciones que las publican en tabla uniforme,
que son las tandas de la 36 en adelante. NO CUENTA las 35 primeras: viven en
secciones de las vueltas 21 y 22 con formatos distintos, sin numeracion corrida,
y un intento de contarlas por patron dio 10 donde hay 35. Esa cifra va CITADA de
donde se publico, marcada como cita y no como medicion de hoy (EXTRACTOR.md 5).
"""
import io
import re

REPORTE = 'docs/loop/REPORTE.md'
FILA = re.compile(r'^\| \*{0,2}(\d+)\*{0,2} \|')

# (rotulo, marcador de inicio, marcador de fin, rango, medible)
TANDAS = [
    ('las 12 `D.29` heredadas hasta la vuelta 21', None, None, (1, 12), False),
    ('las 3 `D.37` de `facilitar_despido_tres_cosas`', None, None, (13, 15), False),
    ('el par de lectura adjudicado', None, None, (16, 16), False),
    ('las 3 `D.37` de `desplegar_tres_conversaciones_carrera`', None, None, (17, 19), False),
    ('las 16 de la vuelta 22', None, None, (20, 35), False),
    ('las 2 de la correccion 6 de la vuelta 23', '### Q.2.e. CORRECCION 6', '### Q.2.f', (36, 37), True),
    ('las 16 de la vuelta 23', '### Q.7.c. LAS ~~**QUINCE**~~', '## Q.8', (38, 53), True),
    ('las 4 de la TAREA 3 de hoy', '### R.4.c. LAS CUATRO, MEDIDAS Y DECLARADAS',
     '**Y LA RAZON DE CADA UNA', (54, 57), True),
    ('las 13 de la serie de `cap_14` mas la 1 que no es de la serie, de hoy',
     '### R.5.f. LAS TRECE ARISTAS', '**POR QUE LAS TRECE SON', (58, 71), True),
]

texto = io.open(REPORTE, encoding='utf-8').read()

print('| tanda | numeros | cuantas | de donde sale la cifra |')
print('|---|---|---:|---|')
medidas = citadas = 0
for rotulo, inicio, fin, (a, b), medible in TANDAS:
    if medible:
        i = texto.find(inicio)
        j = texto.find(fin, i + 1) if i >= 0 else -1
        trozo = texto[i:j] if i >= 0 and j > i else ''
        numeros = set(int(m.group(1)) for m in
                      (FILA.match(l) for l in trozo.split('\n')) if m and a <= int(m.group(1)) <= b)
        medidas += len(numeros)
        print('| %s | %d a %d | **%d** | **CONTADA HOY** de las filas de su seccion |'
              % (rotulo, a, b, len(numeros)))
    else:
        citadas += b - a + 1
        print('| %s | %d a %d | **%d** | CITADA de la vuelta que la publico, no remedida |'
              % (rotulo, a, b, b - a + 1))

print('| **la deuda entera al cerrar la vuelta 24** | **1 a 71** | **%d** | **%d contadas hoy mas %d citadas** |'
      % (medidas + citadas, medidas, citadas))
