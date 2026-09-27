# -*- coding: utf-8 -*-
"""Barrido de caracteres de control sobre los VALORES DECODIFICADOS del dato.

No mira el fichero crudo: un escape JSON de seis letras es texto legal dentro del
fichero y NO es un control dentro del valor. Lo que se caza es el control que vive
DENTRO del string una vez decodificado, que es lo que la TAREA 1.A denuncia.

Sedes barridas: dataset/nodos.jsonl, bitacora/VEREDICTOS.jsonl,
config/pares_mutuos.jsonl, censos/ y cuarentena/ (incluida cuarentena/_insertados/).
"""
import json
import os
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# control = C0 menos los tres que un texto puede llevar legitimamente
PERMITIDOS = ('\t', '\n', '\r')


def controles(s):
    return [(i, c) for i, c in enumerate(s)
            if (ord(c) < 32 and c not in PERMITIDOS) or ord(c) == 127]


def recorrer(valor, ruta):
    if isinstance(valor, dict):
        for k, v in valor.items():
            for r in recorrer(v, ruta + [str(k)]):
                yield r
    elif isinstance(valor, list):
        for i, v in enumerate(valor):
            for r in recorrer(v, ruta + ['[%d]' % i]):
                yield r
    elif isinstance(valor, str):
        for pos, c in controles(valor):
            yield (ruta, pos, c, valor)


SEDES_JSONL = [
    'dataset/nodos.jsonl',
    'bitacora/VEREDICTOS.jsonl',
    'config/pares_mutuos.jsonl',
]
CARPETAS = ['censos', 'cuarentena']

hallazgos = []
mirados = 0

for sede in SEDES_JSONL:
    ruta = os.path.join(RAIZ, sede)
    if not os.path.isfile(ruta):
        print('  %-42s: NO EXISTE' % sede)
        continue
    n = 0
    tocados = 0
    with io.open(ruta, encoding='utf-8') as f:
        for i, linea in enumerate(f, 1):
            linea = linea.strip()
            if not linea:
                continue
            n += 1
            mirados += 1
            d = json.loads(linea)
            for ruta_campo, pos, c, _v in recorrer(d, []):
                tocados += 1
                hallazgos.append((sede, 'linea %d' % i, '.'.join(ruta_campo),
                                  pos, c, d.get('id', '')))
    print('  %-42s: %5d registro(s), %d control(es)' % (sede, n, tocados))

for carpeta in CARPETAS:
    base = os.path.join(RAIZ, carpeta)
    n = 0
    tocados = 0
    for dirpath, _dirnames, nombres in os.walk(base):
        for nombre in sorted(nombres):
            p = os.path.join(dirpath, nombre)
            rel = os.path.relpath(p, RAIZ).replace(os.sep, '/')
            try:
                crudo = io.open(p, encoding='utf-8').read()
            except (UnicodeDecodeError, OSError):
                continue
            n += 1
            mirados += 1
            if nombre.endswith('.json'):
                try:
                    d = json.loads(crudo)
                except ValueError:
                    continue
                ident = d.get('id', '') if isinstance(d, dict) else ''
                for ruta_campo, pos, c, _v in recorrer(d, []):
                    tocados += 1
                    hallazgos.append((rel, 'fichero', '.'.join(ruta_campo),
                                      pos, c, ident))
            else:
                for pos, c in controles(crudo):
                    tocados += 1
                    hallazgos.append((rel, 'fichero', '(texto plano)', pos, c, ''))
    print('  %-42s: %5d fichero(s), %d control(es)' % (carpeta + '/', n, tocados))

print()
print('  ficheros y registros mirados: %d' % mirados)
print('  CONTROLES ENCONTRADOS       : %d' % len(hallazgos))
print()
if hallazgos:
    for sede, donde, campo, pos, c, ident in hallazgos:
        print('  U+%04X  en %s  campo %s  posicion %d' % (ord(c), donde, campo, pos))
        print('          sede: %s' % sede)
        if ident:
            print('          id  : %s' % ident)
else:
    print('  BARRIDO LIMPIO: ni un caracter de control en los valores decodificados.')
