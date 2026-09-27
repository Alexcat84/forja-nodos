# -*- coding: utf-8 -*-
"""PRUEBA DE CAUSA de los 4 rojos, SIN RECUPERAR NINGUN FICHERO RETIRADO.
No abro CREDITO_serial.jsonl ni REPORTE.md ni los saco de git. Lo que hago es
fabricar un registro de credito INVENTADO POR MI en un directorio de usar y tirar
y apuntar credito.DIR_LOOP ahi, que es lo que hace el propio banco de pruebas
(test_en_un_arbol_donde_el_credito_NO_SE_USA..., linea 4739). Si los rojos se
vuelven verdes con eso, la causa es la retirada y no el arbol."""
import os, sys, io, json, tempfile
sys.path.insert(0, '.')
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
from src import credito, herencia

print('=== ANTES: como esta el arbol AHORA, en mi fase ciega ===')
print('credito.lineas_con_registro() :', credito.lineas_con_registro())
print('credito.nacida(LINEA_SERIAL)  :', credito.nacida(credito.LINEA_SERIAL))

tmp = tempfile.mkdtemp(prefix='v47aud_')
# Una tanda INVENTADA por mi, con valores obviamente de juguete.
with io.open(os.path.join(tmp, 'CREDITO_%s.jsonl' % credito.LINEA_SERIAL), 'w',
             encoding='utf-8') as f:
    f.write(json.dumps({"tipo": "tanda", "linea": credito.LINEA_SERIAL, "vuelta": 0,
                        "tanda": "TANDA DE JUGUETE DEL AUDITOR",
                        "especie": "REPORTE", "racha": "0 de 3",
                        "cae": False, "cita": "no es una cita"},
                       ensure_ascii=False) + chr(10))
anterior = credito.DIR_LOOP
credito.DIR_LOOP = tmp
print()
print('=== DESPUES: con un registro de JUGUETE escrito por mi ===')
print('credito.lineas_con_registro() :', credito.lineas_con_registro())
print('credito.nacida(LINEA_SERIAL)  :', credito.nacida(credito.LINEA_SERIAL))

acta = os.path.join(tmp, 'ACTA_AUDITOR.md')
with io.open(acta, 'w', encoding='utf-8') as f:
    f.write(chr(10).join([
        "# ACTA 31. VUELTA 32, la de la linea de la que sale el frente", "",
        "## 9.3. MIS REMEDIOS PARA EL SIGUIENTE", "",
        "| # | **REMEDIO** | como se comprueba |", "|---:|---|---|",
        "| **1** | **UNA COSA DE LA LINEA SERIAL** | mirandola |",
        "| **2** | **OTRA COSA DE LA LINEA SERIAL** | mirandola |", ""]))
os.environ['FORJA_LINEA'] = 'libro_que_nunca_dicto_nada'
r = herencia.extraer(ruta_acta=acta)
print('items para una linea RECIEN NACIDA :', len(r['items']), '(el banco espera 0)')
print('avisos dicen RECIEN NACIDA         :', any('RECIEN NACIDA' in a for a in r['avisos']))
print('el aviso nombra la linea           :', any('libro_que_nunca_dicto_nada' in a for a in r['avisos']))
credito.DIR_LOOP = anterior
