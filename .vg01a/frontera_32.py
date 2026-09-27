import subprocess, sys
def sh(c): return subprocess.run(c,shell=True,capture_output=True,text=True).stdout
print("INSTRUMENTO .vg01a/frontera_32.py  CONSTANTE TECLEADA DENTRO: SI, los DOS HASHES de apertura y cierre de la vuelta 32, que salen del propio reporte (Y.8.c). Todo lo demas lo lee git.")
for h,q in (("56a0df6","apertura vuelta 32"),("4ca7c58","cierre vuelta 32"),("HEAD","hoy")):
    n=len([x for x in sh("git show %s:dataset/nodos.jsonl"%h).splitlines() if x.strip()])
    v=len([x for x in sh("git show %s:bitacora/VEREDICTOS.jsonl"%h).splitlines() if x.strip()])
    t=sh("git show %s:tests/test_aceptacion.py"%h)
    print("  %-8s %-20s nodos=%3d veredictos=%3d bytes_test=%6d"%(h,q,n,v,len(t)))
