## 5.d. `PASOS INVENTADOS` de `cap_07` y `cap_08`

| capitulo | nodos | pasos escritos | PUENTE | PASOS INVENTADOS |
|---|---:|---:|---:|---:|
| `cap_07` | 1 | 3 | 0 | **0,00 por ciento** (0 / 3) |
| `cap_08` | 1 | 5 | 0 | **0,00 por ciento** (0 / 5) |

## 5.e. LA MUESTRA DE FIDELIDAD, CON LA SEMILLA DE ESTA VUELTA (`D.58`)

    $ python scripts/muestra_fidelidad.py --libro marquet_turn_the_ship --capitulos cap_07,cap_08 --semilla m3
    MUESTRA DE FIDELIDAD DEL REGIMEN LIGERO (D.58)
      libro    : marquet_turn_the_ship
      semilla  : m3
      capitulos: cap_07, cap_08

      RELEIDO ENTERO : cap_07
      POR MUESTRA    : cap_08, 15 pasos cada uno

      EL DISPARADOR: si la muestra de un capitulo pasa del 10 por ciento de
      pasos inventados, ESE CAPITULO SE RELEE ENTERO ANTES DE SEGUIR.

      --- cap_08: 5 paso(s) en la muestra
        resistir_dar_solucion_clasificar_decision_urge P1   Resiste el impulso de dar tu la solucion: date tiempo, aunqu
        resistir_dar_solucion_clasificar_decision_urge P2   Anticipa que decisiones se acercan y avisa a tu equipo con a
        resistir_dar_solucion_clasificar_decision_urge P3   Si la decision es urgente, tomala tu mismo y despues haz que
        resistir_dar_solucion_clasificar_decision_urge P4   Si la decision se puede tomar en un plazo razonablemente pro
        resistir_dar_solucion_clasificar_decision_urge P5   Si la decision se puede retrasar, obliga al equipo a dar sus

      --- cap_07: ENTERO, 3 paso(s), no hay muestra que elegir

Salida completa guardada en `.v3m/muestra_fidelidad_v3.txt`. **La semilla eligio releer `cap_07` entero
(tiene solo 3 pasos, bajo el umbral de la herramienta) y muestrear el 100 por ciento de `cap_08` (5 de 5
pasos, tambien bajo el umbral).** Los dos capitulos quedan con cobertura completa de sus pasos, y ambos
ya estan releidos linea a linea contra el libro en las secciones 5.a.3 y 5.b.3: **0 PUENTE en las dos
listas.**
---
