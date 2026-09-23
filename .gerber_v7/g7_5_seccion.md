
## G7.5. TAREA 5: EL CIERRE, `PASOS INVENTADOS POR CAPITULO` CON POBLACION DE VERDAD

### G7.5.a. `PASOS INVENTADOS POR CAPITULO`, una fila por capitulo (`AUDITOR_FORJA.md` 8)

<!-- TALLADO: parcial salida=.gerber_v7/informe_C1.txt,.gerber_v7/informe_C2.txt,.gerber_v7/informe_C3.txt,.gerber_v7/informe_D1.txt,.gerber_v7/informe_D2.txt,.gerber_v7/informe_D3.txt -->

| capitulo | candidatos nuevos (esta vuelta) | pasos escritos | PUENTE | pasos inventados |
|---|---:|---:|---:|---:|
| `cap_18` | `3` (`construir_estrategia_gente_cuatro_componentes`, `aplicar_ocho_reglas_juego_personas`, `aplicar_cinco_pasos_proceso_contratacion`) | `26` | `0` | **0,00 por ciento** |
| `cap_19` | `3` (`distinguir_tres_tipos_sistemas_negocio`, `aplicar_seis_pasos_sistema_venta`, `medir_sistema_venta_trece_indicadores_benchmark`) | `25` | `0` | **0,00 por ciento** |
| **el lote entero** | **`6`** | **`51`** | **`0`** | **0,00 por ciento** |

**`8.2` de `AUDITOR_FORJA.md`: la escalada se decide sobre el peor capitulo, y el peor capitulo de esta
vuelta esta en `0,00` por ciento, igual que el mejor.** El total del lote (`51` pasos, `0` PUENTE) sirve
para comparar con otros lotes, pero no decide el volumen del siguiente (`EXTRACTOR.md` `12`).

### G7.5.b. La muestra de fidelidad con su semilla escrita (`D.58`, regimen ligero)

Salida de
`python scripts/muestra_fidelidad.py --libro gerber_emyth --capitulos cap_18,cap_19 --semilla gerber_v7`,
guardada en `.gerber_v7/muestra_fidelidad.txt`:

<!-- TALLADO: salida=.gerber_v7/muestra_fidelidad.txt -->

    MUESTRA DE FIDELIDAD DEL REGIMEN LIGERO (D.58)
      libro    : gerber_emyth
      semilla  : gerber_v7
      capitulos: cap_18, cap_19

      RELEIDO ENTERO : cap_19
      POR MUESTRA    : cap_18, 15 pasos cada uno

      EL DISPARADOR: si la muestra de un capitulo pasa del 10 por ciento de
      pasos inventados, ESE CAPITULO SE RELEE ENTERO ANTES DE SEGUIR.

      --- cap_18: 15 paso(s) en la muestra
        aplicar_cinco_pasos_proceso_contratacion       P2   Reunete con cada aspirante de forma individual para hablar d
        aplicar_cinco_pasos_proceso_contratacion       P3   Notifica por telefono al candidato elegido, otra vez con una
        aplicar_cinco_pasos_proceso_contratacion       P4   Notifica a los aspirantes no elegidos agradeciendo su intere
        aplicar_cinco_pasos_proceso_contratacion       P5   Dedica el primer dia de entrenamiento a las siguientes activ
        aplicar_cinco_pasos_proceso_contratacion       P6   Revisa con el la idea del negocio.
        aplicar_cinco_pasos_proceso_contratacion       P9   Responde clara y completamente todas sus preguntas.
        aplicar_cinco_pasos_proceso_contratacion       P10  Entregale su uniforme y su Manual de Operaciones.
        aplicar_cinco_pasos_proceso_contratacion       P11  Revisa con el su Manual de Operaciones, incluyendo el Objeti
        aplicar_cinco_pasos_proceso_contratacion       P12  Completa con el los papeles de empleo.
        aplicar_ocho_reglas_juego_personas             P1   Reconoce que el juego de tu gente tiene reglas que hay que h
        aplicar_ocho_reglas_juego_personas             P7   Regla 6: haz que el juego tenga sentido, construido sobre ve
        aplicar_ocho_reglas_juego_personas             P9   Regla 8: si no se te ocurre un buen juego, robalo, pero apre
        construir_estrategia_gente_cuatro_componentes  P1   Entiende que tu Your People Strategy es la forma en que le c
        construir_estrategia_gente_cuatro_componentes  P3   Sigue con tu Strategic Objective.
        construir_estrategia_gente_cuatro_componentes  P4   Construye tu Organizational Strategy: tu Organization Chart 

      --- cap_19: ENTERO, 25 paso(s), no hay muestra que elegir

**LA SEMILLA `gerber_v7` REPARTE, NO YO: `cap_19` sale RELEIDO ENTERO (sus `25` pasos) y `cap_18` sale
POR MUESTRA (`15` de sus `26`).** Contra esa muestra: los `15` pasos de `cap_18` y los `25` de `cap_19`
(`40` de `51` pasos del lote) ya llevan su relectura de fidelidad `D.30` hecha en el acto de escribir
cada candidato (`G7.3.c`, `G7.4.d`): cada uno de los `51` pasos del lote entero quedo marcado
TRANSCRIPCION con su cita pegada (`.gerber_v7/cita_cap18_*.txt`, `.gerber_v7/cita_cap19_*.txt`), **`0`
PUENTE en los `51`.** Repasados de nuevo los `40` que esta muestra selecciona, uno a uno contra su
paragrafo de origen, **ninguno cambia de veredicto: los `40` siguen TRANSCRIPCION.**

**`0,00` POR CIENTO DE PASOS INVENTADOS EN LA MUESTRA. `0,00` por debajo del `10` por ciento que
dispara la relectura completa de `D.58`: NO SE DISPARA NADA.**
