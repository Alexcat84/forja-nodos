import subprocess
def leer(rev):
    return subprocess.run(['git','show',f'{rev}:bitacora/VEREDICTOS.jsonl'],capture_output=True).stdout.decode('utf-8').split('\n')
viejo=[l for l in leer('b9f484a') if l.strip()]
nuevo=[l for l in open('bitacora/VEREDICTOS.jsonl',encoding='utf-8').read().split('\n') if l.strip()]
print("lineas al abrir la vuelta 30 (b9f484a):",len(viejo))
print("lineas hoy                          :",len(nuevo))
print("lineas nuevas                       :",len(nuevo)-len(viejo))
cambiadas=[i+1 for i in range(len(viejo)) if viejo[i]!=nuevo[i]]
print("de las",len(viejo),"viejas, CAMBIADAS:",len(cambiadas),"->",cambiadas)
print("de las",len(viejo),"viejas, INTACTAS :",len(viejo)-len(cambiadas))
print()
print("prefijo intacto: ninguna linea vieja se borro ni se reordeno:", all(viejo[i]==nuevo[i] for i in range(len(viejo)) if (i+1) not in cambiadas))
# y que el cambio es solo aniadir anotaciones
import json
for n in cambiadas:
    a=json.loads(viejo[n-1]); b=json.loads(nuevo[n-1])
    igual=all(a.get(k)==b.get(k) for k in ['veredicto','candidato','vecino','huella_candidato','huella_vecino','senales','levantada_por','fecha'])
    raz = b['razon'].startswith(a['razon'])
    print(f"  linea {n}: clase/huellas/senales intactas={igual} | la razon vieja sigue entera al principio={raz} | +{len(b['razon'])-len(a['razon'])} caracteres")
