# PRIMERA LINEA (HEREDADO 4): CERO IDS TECLEADOS. Lee la salida de .v33a/barrido.sh, que a su
# vez saco los ids de .v33a/tanda_ids.txt, generado del git diff del dataset.
import io, re
t = io.open('.v33a/barrido.txt', encoding='utf-8', errors='replace').read()
bloques = t.split('===== BARRIDO DE ')[1:]
print("RESUMEN DEL BARRIDO DE VECINOS, GRAFO MAS BANDEJAS (D.38.4 con el metodo de D.38.5)")
print("  poblacion de cada corrida: dataset/nodos.jsonl de 282 nodos MENOS el propio candidato,")
print("  mas las bandejas de cuarentena/, que las pone la aduana sola. Arbol 1ae327e.")
print()
print("  %-46s %-9s %-9s %-9s %s" % ('candidato','poblacion','ENTRARIA','BLOQUEA','CAE'))
tot = 0
for b in bloques:
    ident = b.split('\n')[0].replace(' =====','').strip()
    pob = re.search(r'poblacion del barrido\s*:\s*(\d+)\s*\(([^)]*)\)', b)
    ent = re.search(r'ENTRARIAN sin leer nada\s*:\s*(\d+)', b)
    blo = re.search(r'BLOQUEARIAN esperando veredicto\s*:\s*(\d+)', b)
    cae = re.search(r'CAERIAN por una guarda\s*:\s*(\d+)', b)
    tot += int(blo.group(1)) if blo else 0
    print("  %-46s %-9s %-9s %-9s %s" % (ident[:46], pob.group(1) if pob else '?',
          ent.group(1) if ent else '?', blo.group(1) if blo else '?', cae.group(1) if cae else '?'))
print()
p = re.search(r'poblacion del barrido\s*:\s*(\d+)\s*\(([^)]*)\)', t)
print("  poblacion, literal de la aduana: %s  (%s)" % (p.group(1), p.group(2)))
print("  corridas: %d   vecinos que la aduana levanta en TODA la tanda: %d" % (len(bloques), tot))
