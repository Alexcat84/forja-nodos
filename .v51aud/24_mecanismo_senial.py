# -*- coding: utf-8 -*-
"""POR QUE EL DIGITO QUE LAS FICHAS DECLARAN NO SE REPRODUCE HOY.
La senial come titulo mas resumen_teorico mas pasos (src/comun.py:190-194), y el resumen de
cada ficha crecio DESPUES de su pasada de aduana. Mido tres cosas por par: la senial de hoy en
las dos direcciones, y la senial con las colas recortadas. La columna 'ficha' es el digito que
la propia ficha declara, leido de su texto."""
import io,sys,json
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.path.insert(0,'.')
from src import aduana, comun
def carga(s): return json.load(open('cuarentena/grove_high_output/%s.json'%s,encoding='utf-8'))
def recorta(n,marca):
    m=dict(n); r=n['resumen_teorico']; i=r.find(marca)
    if i>=0: m['resumen_teorico']=r[:i]
    return m
PARES=[('preparar_guion_reunion_individual_subordinado','infundir_regularidad_reunion_proceso',0.416),
       ('fijar_frecuencia_reunion_individual_madurez_tarea','infundir_regularidad_reunion_proceso',0.385),
       ('cubrir_indicadores_problemas_reunion_individual','infundir_regularidad_reunion_proceso',0.391),
       ('cubrir_indicadores_problemas_reunion_individual','preparar_guion_reunion_individual_subordinado',0.432),
       ('fijar_duracion_lugar_reunion_individual','fijar_frecuencia_reunion_individual_madurez_tarea',0.445)]
print("%-38s %-38s %6s %7s %7s %9s"%("hijo (el que declara el digito)","vecino","ficha","hoy","invertido","recortado"))
for a,b,dec in PARES:
    na,nb=carga(a),carga(b)
    ta,tb=comun.texto_comparable(na),comun.texto_comparable(nb)
    print("%-38s %-38s %6.3f %7.4f %9.4f %9.4f"%(a[:38],b[:38],dec,
        aduana.senal_similitud_texto(ta,tb),
        aduana.senal_similitud_texto(tb,ta),
        aduana.senal_similitud_texto(comun.texto_comparable(recorta(na,'VEREDICTO ESCRITO POR LECTURA')),
                                     comun.texto_comparable(recorta(nb,'ARISTAS DECLARADAS POR LECTURA')))))
print()
print("umbral de la casa (config/umbrales.json): %s"%json.load(open('config/umbrales.json',encoding='utf-8'))['umbral_similitud_texto'])
