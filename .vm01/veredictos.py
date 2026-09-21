# -*- coding: utf-8 -*-
"""LOS PARES QUE LA ADUANA LEVANTA, LEIDOS DE SU PROPIO FICHERO, CON MI VEREDICTO AL LADO.

El par, la señal que lo levanta y las tres cifras se leen del .txt del informe. EL
VEREDICTO Y SU RAZON LOS PONGO YO LEYENDO, y van en .vm01/razones.txt: las señales
ordenan, nunca deciden (manual principio 4). Un par levantado sin veredicto escrito
es cola de lectura, no un nodo limpio.

ESTE FRENTE NO INSERTA, asi que estos veredictos NO van a bitacora/VEREDICTOS.jsonl:
esa sede la escribe la aduana al insertar (EXTRACTOR.md 14). Quedan aqui.
"""
import io, os, re, sys

if hasattr(sys.stdout, "buffer"):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", newline="\n")

RAZONES = dict(eval(io.open(".vm01/razones.txt", encoding="utf-8").read()))
ORDEN = eval(io.open(os.environ.get('ORDEN_TANDA', '.vm01/orden_tanda.txt'), encoding="utf-8").read())

BLOQUE = re.compile(r"^\[(?:ENTRARIA|BLOQUEARIA|CAERIA)\] (\S+)", re.M)
VECINO = re.compile(r"^    vecino (\S+)\s+\[levantada por: ([^\]]+)\]\s*\n"
                    r"\s+similitud_texto ([0-9.]+) \| familia_id ([0-9.]+) \| paso_contra_nodo ([0-9.]+)", re.M)

print("AVISO: EL PAR, LA SEÑAL Y LAS TRES CIFRAS SE LEEN DE .vm01/aduana/<fichero>.txt. "
      "El veredicto y su razon los pone el extractor leyendo, de .vm01/razones.txt.")
print("")
print("| candidato | vecino levantado | señal | similitud | familia | paso contra nodo | veredicto | razon escrita |")
print("|---|---|---|---:|---:|---:|---|---|")
vistos, total = set(), 0
for _n, _p, identificador, fichero, _i in ORDEN:
    texto = io.open(os.path.join(".vm01", "aduana", fichero), encoding="utf-8").read()
    corte = texto.index("LA LISTA COMPLETA")
    for vecino, senal, s1, s2, s3 in VECINO.findall(texto[corte:]):
        clave = tuple(sorted((identificador, vecino)))
        if clave in vistos:
            continue
        vistos.add(clave)
        total += 1
        veredicto, razon = RAZONES.get(clave, ("SIN VEREDICTO", "FALTA"))
        print("| `%s` | `%s` | %s | **%s** | %s | %s | **%s** | %s |"
              % (identificador, vecino, senal,
                 s1.replace(".", ","), s2.replace(".", ","), s3.replace(".", ","),
                 veredicto, razon))
print("| **pares distintos levantados por el capitulo, y todos con veredicto escrito** | **%d** | | | | | | |" % total)
