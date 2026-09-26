# -*- coding: utf-8 -*-
"""Fase ciega de la 71, D.37 (copia de .v68aud/d37_partes.py con las partes cambiadas): para los titulos de la tanda que
dicen cuantas partes tienen y las nombran, busca en GRAFO MAS BANDEJAS (D.38.4, la poblacion de aduana.poblacion_de_bandejas)
los ids cuyo id o titulo contiene la palabra de cada parte. Imprime id y libro, nunca claves de relacion (R6). No escribe nada."""
import io, json, re, sys
sys.path.insert(0, '.')
sys.stdout.reconfigure(encoding="utf-8")
from src import aduana, comun
nodos = list(comun.leer_jsonl(comun.RUTA_DATASET))
bandejas = list(aduana.poblacion_de_bandejas(fecha=aduana._hoy()))
print('poblacion: %d' % (len(nodos) + len(bandejas)))
partes = [
    ('planificar tres pasos: 1 la demanda del entorno', r'demanda'),
    ('planificar tres pasos: 2 el estado presente', r'estado_presente|estado presente'),
    ('planificar tres pasos: 3 cerrar la brecha', r'brecha'),
    ('examinar entorno cuatro objetos: expectativas del cliente', r'expectativa'),
    ('examinar entorno cuatro objetos: tecnologia', r'tecnolog'),
    ('examinar entorno cuatro objetos: proveedores', r'proveedor'),
    ('examinar entorno cuatro objetos: otros grupos de la organizacion', r'otros_grupos|otros grupos|grupos de tu organizacion'),
    ('direccion por objetivos dos preguntas: el objetivo', r'objetivo'),
    ('direccion por objetivos dos preguntas: los resultados clave', r'resultado_clave|resultados_clave|resultado clave|resultados clave|hito'),
    ('cerrar brecha dos preguntas: que necesitas y que puedes hacer', r'necesitas_hacer|puedes_hacer|necesitas hacer|puedes hacer'),
    ('evaluacion tres claves: franqueza', r'franc|franqueza'),
    ('evaluacion tres claves: escucha total', r'escucha'),
    ('evaluacion tres claves: dejarse fuera', r'emocion|dejar fuera|dejarte fuera'),
]
for nombre, pat in partes:
    hs = []
    for d in nodos + bandejas:
        t = (d.get('id', '') + ' | ' + (d.get('titulo') or '')).lower()
        if re.search(pat, t):
            hs.append((d.get('id'), [f.get('clave') for f in d.get('fuentes', [])][:1]))
    print('%s: %d' % (nombre, len(hs)))
    for h in hs: print('    %-66s %s' % h)
