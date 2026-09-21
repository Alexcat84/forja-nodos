# -*- coding: utf-8 -*-
"""Tallado de los seis barridos de vecinos (D.38.4) que corri en esta fase, leido de sus
propios ficheros de salida y no teclado por mi. Modo austero D.47: la tabla, no los seis
ficheros enteros, que quedan en .v51aud/04_barrido_*.out."""
import io,sys,re,glob
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
SEIS=['infundir_regularidad_reunion_proceso','usar_tres_clases_reunion_proceso',
'fijar_frecuencia_reunion_individual_madurez_tarea','fijar_duracion_lugar_reunion_individual',
'preparar_guion_reunion_individual_subordinado','cubrir_indicadores_problemas_reunion_individual']
RUT={'infundir_regularidad_reunion_proceso':'.v51aud/04_barrido_P6.out'}
print("%-50s %5s %8s %7s  %s"%("ficha","pobl","reloj s","sobre","el vecino mas proximo y su digito"))
for s in SEIS:
    r=RUT.get(s,'.v51aud/04_barrido_%s.out'%s)
    t=io.open(r,encoding='utf-8').read()
    pob=re.search(r'poblacion barrida: (\d+)',t).group(1)
    rel=re.search(r'reloj del barrido: ([\d.]+) s',t).group(1)
    sob=re.search(r'vecinos por encima del umbral [\d.]+: (\d+)',t).group(1)
    pri=re.findall(r'\s+([\d.]+)\s+\[([^\]]+)\]\s+(\S+)',t)[0]
    print("%-50s %5s %8s %7s  %s %s"%(s,pob,rel,sob,pri[0],pri[2][:40]))
tot=sum(float(re.search(r'reloj del barrido: ([\d.]+) s',io.open(RUT.get(s,'.v51aud/04_barrido_%s.out'%s),encoding='utf-8').read()).group(1)) for s in SEIS)
print()
print("suma de los seis relojes: %.1f s  (%.1f min)"%(tot,tot/60.0))
print("ficheros de salida enteros: %d"%len(glob.glob('.v51aud/04_barrido_*.out')))
