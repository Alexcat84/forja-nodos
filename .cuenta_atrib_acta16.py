import json, subprocess, glob, os

def atrib_en(rev, path):
    r = subprocess.run(['git', 'show', '%s:%s' % (rev, path)],
                       capture_output=True, text=True)
    if r.returncode:
        return 0
    return len(json.loads(r.stdout).get('atribuciones') or [])

APERTURA = '5367adf'
CIERRE = 'da62e73'
tot_a = tot_c = 0
for p in sorted(glob.glob('cuarentena/scott_radical_candor/*.json')):
    p = p.replace(os.sep, '/')
    a = atrib_en(APERTURA, p)
    c = atrib_en(CIERRE, p)
    tot_a += a
    tot_c += c
    if a or c:
        print('%-48s apertura=%d cierre=%d' % (os.path.basename(p)[:-5][:47], a, c))
print('TOTAL bandeja: apertura %d -> cierre %d (nuevas en la vuelta 16: %d)'
      % (tot_a, tot_c, tot_c - tot_a))
