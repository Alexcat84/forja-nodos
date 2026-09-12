# -*- coding: utf-8 -*-
"""Orden de insercion del lote 3: D.36 (el orden que lee) mas D.29 (la madre entra
primero). Topologico con prioridad al orden del libro. No escribe en ninguna sede."""
import glob, os, subprocess, heapq, io
from pathlib import Path
def sh(a): return subprocess.run(a, capture_output=True, text=True, encoding='utf-8')
COM = {'f2c7312':'cap_07','293f3bc':'cap_08','447bad2':'cap_09','a0734ab':'cap_10','b7aadb2':'cap_11'}
fs = sorted(glob.glob('cuarentena/zhuo_manager/*.json'))
cap={}
for f in fs:
    p=Path(f).as_posix()
    h = sh(['git','log','--diff-filter=A','--format=%h','--',p]).stdout.split()[0]
    cap[os.path.basename(f)[:-5]] = COM[h]
base = sorted(cap, key=lambda k: (cap[k], k))
pos = {k:i for i,k in enumerate(base)}

D36 = [
 ('reconocer_decision_dificil_valores','actuar_conducta_contraria_valores'),
 ('auditar_calendario_reuniones_semana','cerrar_reunion_pasos_siguientes'),
 ('auditar_calendario_reuniones_semana','examinar_trabajo_pasado_candidato'),
 ('repartir_responsabilidad_contratar_equipo','avisar_organizador_reunion_prescindible'),
 ('entregar_experiencia_entrevista_excelente','desarrollar_estrategia_busqueda_candidatos'),
 ('repartir_equipo_cartera_horizontes','involucrar_varios_entrevistadores'),
 ('mediar_tiempo_palabra_reunion','repartir_responsabilidad_contratar_equipo'),
 ('mostrar_candidato_cuanto_quieres','repartir_papeles_directivo_reclutador'),
]
D29 = [
 ('fijar_resultado_excelente_reunion','dirigir_reunion_decision'),
 ('fijar_resultado_excelente_reunion','dirigir_reunion_generar_ideas'),
 ('fijar_resultado_excelente_reunion','dirigir_reunion_informativa'),
 ('fijar_resultado_excelente_reunion','dirigir_reunion_reforzar_relaciones'),
 ('fijar_resultado_excelente_reunion','dirigir_reunion_revision_trabajo'),
 ('cambiar_formato_reunion_favorecer_participacion','abrir_discusion_notas_adhesivas'),
]
CONS = D36 + D29
succ={k:[] for k in base}; indeg={k:0 for k in base}
for a,b in CONS:
    succ[a].append(b); indeg[b]+=1
h=[(pos[k],k) for k in base if indeg[k]==0]; heapq.heapify(h)
orden=[]
while h:
    _,k=heapq.heappop(h); orden.append(k)
    for s in succ[k]:
        indeg[s]-=1
        if indeg[s]==0: heapq.heappush(h,(pos[s],s))
assert len(orden)==68, len(orden)
p2={k:i for i,k in enumerate(orden)}
print("todas las restricciones cumplidas:", all(p2[a]<p2[b] for a,b in CONS))
print("movimientos reales respecto al orden del libro:")
for a,b in CONS:
    if pos[a] > pos[b]:
        print("   por %-10s  %-44s (#%02d -> #%02d) baja detras de %s (#%02d)" % (
            'D.36' if (a,b) in D36 else 'D.29', b, pos[b]+1, p2[b]+1, a, p2[a]+1))
io.open('.orden_insercion_lote3.txt','w',encoding='utf-8').write(
    "\n".join("%02d %s %s"%(i+1,cap[k],k) for i,k in enumerate(orden))+"\n")
print()
print("\n".join("%02d %s %s"%(i+1,cap[k],k) for i,k in enumerate(orden)))
