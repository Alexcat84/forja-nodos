import io, os, re, json
ORDEN = [
    ('01', 'parar_debate_emocion_agotamiento', '.v30e/ins_01_parar_debate.txt'),
    ('02', 'fijar_fecha_cierre_debate_equipo', '.v30e/ins_02_fijar_fecha.txt'),
    ('03', 'repartir_decision_cercanos_hechos', '.v30e/ins_03_repartir.txt'),
    ('04', 'pedir_hechos_decision_evitar_recomendaciones', '.v30e/ins_04_pedir_hechos.txt'),
    ('05', 'persuadir_emocion_oyente_no_propia', '.v30e/ins_05_persuadir.txt'),
    ('06', 'establecer_credibilidad_pericia_humildad', '.v30e/ins_06_credibilidad.txt'),
    ('07', 'compartir_logica_mostrar_razonamiento', '.v30e/ins_07_compartir.txt'),
    ('08', 'minimizar_impuesto_colaboracion_equipo', '.v30e/ins_08_minimizar.txt'),
    ('09', 'proteger_tiempo_equipo_jefe', '.v30e/ins_09_proteger.txt'),
    ('10', 'mantener_manos_trabajo_real_equipo', '.v30e/ins_10_mantener.txt'),
    ('11', 'reservar_calendario_tiempo_ejecutar', '.v30e/ins_11_reservar.txt'),
    ('12', 'cuidarse_agotamiento_centro_rueda', '.v30e/ins_12_cuidarse.txt'),
    ('13', 'bloquear_tiempo_pensar_calendario', '.v30e/ins_13_bloquear.txt'),
]
print('| # | nodo insertado | vecinos juzgados | declarados por lectura | nodos en el grafo tras el | veredictos escritos |')
print('|---:|---|---:|---:|---:|---:|')
tv = td = 0
for n, i, ruta in ORDEN:
    t = io.open(ruta, encoding='utf-8').read()
    vec = re.search(r'VECINOS POR ENCIMA DE UMBRAL: (\d+)', t)
    dec = re.search(r'DECLARADOS POR LECTURA: (\d+)', t)
    nod = re.search(r'nodos en el grafo: (\d+)', t)
    ver = re.search(r'veredictos en bitacora/VEREDICTOS\.jsonl: (\d+)', t)
    v = int(vec.group(1)) if vec else 0
    d = int(dec.group(1)) if dec else 0
    tv += v
    td += d
    print('| %s | `%s` | %d | %d | **%s** | %s |'
          % (n, i, v, d, nod.group(1), ver.group(1)))
print('| | **total** | **%d** | **%d** | | **%d** |' % (tv, td, tv + td))
