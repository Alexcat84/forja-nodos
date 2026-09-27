# -*- coding: utf-8 -*-
"""LA FRONTERA DE cap_14, PUBLICADA ANTES DE CORTAR (EXTRACTOR.md 10).

Cuenta las palabras de cada pieza directamente del fichero y comprueba que las
piezas mas los residuos suman el cuerpo entero. Si no suma, hay tramo del
capitulo que no aparece en ninguna pieza, que es exactamente la caida que la
vuelta 7 pago.
"""
import io

RUTA = 'fuentes/scott_radical_candor/cap_14.md'
CUERPO_DESDE = 8

PIEZAS = [
    ('R1', 9, 19, 'residuo: rotulo y el alegato de separar desarrollo de gestion del desempenio'),
    ('P1', 21, 33, 'arrancar la revision del sistema, con sus seis rotulos'),
    ('P2', 35, 63, 'la cabeza: los trece elementos del proceso, nombrados uno a uno'),
    ('P3', 65, 71, 'elemento 1, poner nota o no'),
    ('P4', 73, 93, 'elemento 2, las categorias de la nota'),
    ('P5', 95, 97, 'elemento 3, las escaleras de puesto'),
    ('P6', 99, 115, 'elemento 4, cuantas notas'),
    ('P7', 117, 123, 'elemento 5, el lenguaje de la nota'),
    ('P8', 125, 141, 'elemento 6, las consecuencias de la nota'),
    ('P9', 143, 151, 'elemento 7, el reparto de notas'),
    ('P10', 153, 169, 'elemento 8, curva forzada o no'),
    ('P11', 171, 185, 'elemento 9, la calibracion'),
    ('P12', 187, 195, 'elemento 10, la frecuencia'),
    ('P13', 197, 203, 'elemento 11, proceso de 360 grados o juicio unilateral'),
    ('P14', 205, 219, 'elemento 12, transparente o confidencial'),
    ('P15', 221, 239, 'elemento 13, ligero o pesado'),
    ('R2', 241, 243, 'residuo: la conclusion y la direccion de correo'),
]

lineas = io.open(RUTA, encoding='utf-8').read().splitlines()


def palabras(desde, hasta):
    return sum(len(l.split()) for l in lineas[desde - 1:hasta])


cuerpo = palabras(CUERPO_DESDE, len(lineas))

print('| pieza | lineas | palabras | que es |')
print('|---|---|---:|---|')
suma = 0
for nombre, desde, hasta, que in PIEZAS:
    n = palabras(desde, hasta)
    suma += n
    print('| `%s` | L%d a L%d | **%d** | %s |' % (nombre, desde, hasta, n, que))
print('| **el cuerpo entero** | **L%d a L%d** | **%d** | **suma de las piezas: %d, residuo sin asignar: %d** |'
      % (CUERPO_DESDE, len(lineas), cuerpo, suma, cuerpo - suma))
