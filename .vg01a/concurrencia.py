import os,glob,subprocess,sys
print("INSTRUMENTO .vg01a/concurrencia.py  SIN CONSTANTES TECLEADAS: lee mtime del disco y el indice de git")
def sh(c): return subprocess.run(c,shell=True,capture_output=True,text=True).stdout.strip()
print("$ date")
print("  "+sh("date"))
print("$ tail -1 docs/loop/loop.log   (el arnes abrio MI turno aqui)")
print("  "+sh("tail -1 docs/loop/loop.log"))
print("$ ls --time-style=full-iso de lo que aparecio DESPUES de esa linea")
for p in sorted(glob.glob('cuarentena/grove_high_output/*.json'))+sorted(glob.glob('.v1g/*')):
    print("  %-22s %s"%(__import__('datetime').datetime.fromtimestamp(os.path.getmtime(p)).strftime('%H:%M:%S'),p))
print("$ git diff --cached --name-only   (lo que OTRO proceso tiene ya en el indice)")
for l in sh("git diff --cached --name-only").splitlines(): print("  "+l)
print("$ git status --short cuarentena/grove_high_output/ | wc -l")
print("  "+sh("git status --short cuarentena/grove_high_output/ | wc -l"))
