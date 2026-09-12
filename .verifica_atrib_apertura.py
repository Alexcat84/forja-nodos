import json, subprocess

r = subprocess.run(['git', 'ls-tree', '--name-only', '5367adf',
                    'cuarentena/scott_radical_candor/'],
                   capture_output=True, text=True)
ficheros = [x for x in r.stdout.splitlines() if x.endswith('.json')]
print('ficheros en la bandeja en 5367adf (apertura de la vuelta 16):', len(ficheros))
total = 0
for p in ficheros:
    d = json.loads(subprocess.run(['git', 'show', '5367adf:%s' % p],
                                  capture_output=True, text=True).stdout)
    n = len(d.get('atribuciones') or [])
    total += n
    print('   %-50s atribuciones=%d' % (p.split('/')[-1][:-5], n))
print('TOTAL atribuciones al abrir la vuelta 16:', total)
