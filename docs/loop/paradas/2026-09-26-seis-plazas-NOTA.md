# NOTA, 26 SEP 2026: **EL PRESUPUESTO BAJA A 6 PLAZAS** (regla del fundador del 25 sep, punto 3)

*Aplicada con la linea parada en la frontera entre vueltas, como manda la decision
(`2026-09-25-presupuesto-unico-y-prioridad-baja-DECISION.md`).*

## LA REGLA, LITERAL

> Si la mediana pasa de 2 segundos mientras el fundador usa la maquina, en la pausa siguiente baja a 6
> plazas.

## LA MEDIDA QUE LA DISPARA

La observacion pasiva de las 07:13 del 26 sep 2026, durante el barrido de la vuelta 76 (Gerber): el
fundador usaba la maquina en 4 de las 5 muestras, y la **mediana del arranque de PowerShell en uso fue de
4,12 s**. Nucleos de eficiencia al 100%, 18 procesos python. Las cinco muestras de esa hora, literales (hora, plan, arranque, cola, cpu, uso de rendimiento, de
eficiencia, python, segundos sin entrada, en uso); en uso: 0,16, 0,27, 7,96 y 14,41 s, mediana 4,12 s:

```
07:09:07,Balanced,0.16,1,17,8,31,1,13,1
07:10:03,Balanced,0.27,2,13,9,19,1,69,1
07:10:59,Balanced,0.23,15,46,10,100,18,126,0
07:12:04,Balanced,7.96,71,74,56,100,18,6,1
07:13:14,Balanced,14.41,74,48,14,100,18,0,1
```

Resumen horario de la noche (hora, plan, muestras, mediana, maximo, en uso, mediana en uso, cola, uso de
nucleos de rendimiento, de eficiencia, python):

```
2026-09-25 21:12,Balanced,5,0.2,0.23,5,0.2,2,10,52,3
2026-09-25 22:12,Balanced,5,0.17,6.07,4,0.17,2,3,23,3
2026-09-25 23:12,Balanced,5,0.18,0.2,0,,1,6,18,3
2026-09-26 00:12,Balanced,5,0.19,0.19,0,,1,2,20,3
2026-09-26 01:13,Balanced,5,0.17,0.19,0,,1,5,20,3
2026-09-26 02:13,Balanced,5,0.25,14.57,0,,26,19,100,14
2026-09-26 03:13,Balanced,5,0.19,0.21,0,,1,10,29,2
2026-09-26 04:13,Balanced,5,0.17,0.19,0,,1,4,20,0
2026-09-26 05:13,Balanced,5,0.19,0.21,0,,1,4,23,3
2026-09-26 06:13,Balanced,5,0.22,0.27,0,,0,5,10,0
2026-09-26 07:13,Balanced,5,0.27,14.41,4,4.12,15,10,100,18
```

## COMO SE APLICA

Sin tocar codigo: la linea se relanza con `FORJA_PRESUPUESTO_PROCESOS=6` en sus variables
(`scripts/lanzar_linea.ps1 -Variables`), que `src/presupuesto.py` ya respeta como tope del total de plazas
de la maquina. Se sigue observando cada hora igual que antes.
