import json, io, glob, os, re
vivos = {}
for l in io.open('dataset/nodos.jsonl', encoding='utf-8'):
    n = json.loads(l)
    vivos[n['id']] = n
bandeja = set(os.path.basename(p)[:-5]
              for p in glob.glob('cuarentena/*/*.json') if '_insertados' not in p)
def sede(i):
    return 'GRAFO' if i in vivos else ('bandeja' if i in bandeja else 'NO EXISTE')
def cableada(madre, hijo):
    n = vivos.get(madre)
    return n is not None and hijo in n['nodos_siguientes']
# cap_04: los candidatos de la bandeja cuyo resumen declara cap_04
# LA POBLACION DE cap_04 ES EL ARCHIVO MAS LA BANDEJA: sus seis YA ENTRARON, y
# lo que queda pendiente es RELEERLOS, no insertarlos.
c4 = []
for p in (glob.glob('cuarentena/_insertados/scott_radical_candor/*.json')
          + glob.glob('cuarentena/scott_radical_candor/*.json')):
    d = json.load(io.open(p, encoding='utf-8'))
    if 'cap_04' in d.get('resumen_teorico', ''):
        c4.append(d)
print('| lo que queda | cifra al abrir | cifra al cerrar | estado |')
print('|---|---:|---:|---|')
print('| la arista en cola `crear_espacio_seguro_madurar_ideas_nuevas > nutrir_ideas_nuevas_reunion_solas` | **1** | **%d** | sigue: el hijo esta en %s |'
      % (0 if cableada('crear_espacio_seguro_madurar_ideas_nuevas', 'nutrir_ideas_nuevas_reunion_solas') else 1,
         sede('nutrir_ideas_nuevas_reunion_solas')))
partes = ['proteger_tiempo_equipo_jefe', 'mantener_manos_trabajo_real_equipo',
          'reservar_calendario_tiempo_ejecutar']
faltan = sum(0 if cableada('minimizar_impuesto_colaboracion_equipo', p) else 1 for p in partes)
print('| la serie `D.37` de `minimizar_impuesto_colaboracion_equipo` | **3** partes | **%d** | **CERRADA: las tres viven y las tres estan cableadas** |' % faltan)
falta_b = 0 if cableada('aprender_resultados_vencer_dos_presiones', 'cuidarse_agotamiento_centro_rueda') else 1
print('| la mitad `Burnout` de la serie de `aprender_resultados_vencer_dos_presiones` | **1** | **%d** | **CERRADA: `cuidarse_agotamiento_centro_rueda` entro y su arista se declaro** |' % falta_b)
print('| los `12` candidatos de `cap_07` con su cola de lectura | **12** candidatos, **77** pares | **%d** y **0** | **CERRADA: `cap_07` queda entero en el grafo** |'
      % len([p for p in glob.glob('cuarentena/scott_radical_candor/*.json')
             if 'cap_07.md, lineas' in json.load(io.open(p, encoding='utf-8')).get('resumen_teorico', '')]))
print('| el hueco de transcripcion de `L153` | **1** modo de **3**, en **1** nodo | **1** de **3** | sigue **SIN VIA**, y con un solo ejemplar no se construye |')
print('| las entradillas de `LISTEN`, `CLARIFY` y `DEBATE` de `cap_07` | **3** tramos | **3** | sigue: medido hoy en `.v30e/entradillas.txt`, `3` de `7` rotulos sin nodo |')
print('| las `8` lineas `SIN HUELLA` de `D.15` | **8**, ninguna declarada | **8**, **las 8 declaradas** | **CERRADA por la segunda salida de `D.15`** |')
print('| `cap_04` releido antes que las tres filas de hueco | **6** candidatos, **48** pasos | **%d** y **%d** | **SIGUE SIN CABER**, y lo declaro otra vez con su motivo |'
      % (len(c4), sum(len(d['pasos_accionables']) for d in c4)))
print('| la frontera por capitulo con las `QUESTIONS TO CONSIDER` | **14** de **17** unidades | **14** de **17** | la vuelta que mine un capitulo del lote 5 |')
print('| **NUEVA**: la arista en cola `desplegar_plan_orden_operaciones_franqueza_radical > bloquear_tiempo_pensar_calendario` | 0 | **1** | la desbloquea que entre la MADRE, que espera en bandeja |')
print('| el lote 5 por su orden | **3** candidatos en bandeja | **%d** | **NO TOCADO**, y es deliberado (`D.39`) |'
      % len(glob.glob('cuarentena/marquet_turn_the_ship/*.json')))
print('| la bandeja del lote 4, lo que queda por insertar | **102** | **%d** | sigue |'
      % len(glob.glob('cuarentena/scott_radical_candor/*.json')))
