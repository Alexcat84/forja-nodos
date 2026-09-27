# -*- coding: utf-8 -*-
"""Los tres nodos del grafo que las fichas de cap_05 nombran como vecinos: existencia,
libro, pasos, y los dos pasos que se contradicen con la tanda. Auditor, apertura ciega v51."""
import io,sys,json
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
IDS=['dirigir_reunion_individual_semanal','preguntar_conducir_reunion_individual','auditar_calendario_reuniones_semana']
graf={}
for l in open('dataset/nodos.jsonl',encoding='utf-8'):
    if l.strip():
        n=json.loads(l); graf[n['id']]=n
for i in IDS:
    n=graf.get(i)
    print("%-42s en el grafo: %s   libro: %s   pasos: %s"%(i,'SI' if n else 'NO',
          n['fuentes'][0].get('clave') if n else '-', len(n['pasos_accionables']) if n else '-'))
print()
print("EL PAR QUE SE CONTRADICE, LOS DOS PASOS IMPRESOS DE SU FICHERO:")
c=json.load(open('cuarentena/grove_high_output/cubrir_indicadores_problemas_reunion_individual.json',encoding='utf-8'))
print("  paso 1 de cubrir_indicadores_problemas_reunion_individual (cuarentena, cap_05 L43):")
print("    %s"%c['pasos_accionables'][0])
print("  paso 4 de dirigir_reunion_individual_semanal (dataset/nodos.jsonl, zhuo_manager):")
print("    %s"%graf['dirigir_reunion_individual_semanal']['pasos_accionables'][3])
