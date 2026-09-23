
## G8.5. TAREA 5: EL CIERRE, Y EL INVENTARIO QUE HEREDA LA VUELTA QUE INSERTE

### G8.5.a. `PASOS INVENTADOS POR CAPITULO`, una fila por capitulo (`AUDITOR_FORJA.md` 8)

Los tres capitulos de esta vuelta cerraron con **cero candidatos** (`G8.2`, `G8.3`, `G8.4.d`), asi que no
hay pasos escritos que medir: no es que la fidelidad haya fallado, es que no hay ficha de la que medirla.

<!-- TALLADO: parcial salida=.gerber_v8/muestra_fidelidad.txt -->

| capitulo | candidatos nuevos (esta vuelta) | pasos escritos | PUENTE | pasos inventados |
|---|---:|---:|---:|---:|
| `cap_20` | `0` | `0` | `0` | **sin poblacion que medir** |
| `cap_21` | `0` | `0` | `0` | **sin poblacion que medir** |
| `cap_22` | `0` | `0` | `0` | **sin poblacion que medir** |
| **el lote entero** | **`0`** | **`0`** | **`0`** | **sin poblacion que medir** |

**`8.2` de `AUDITOR_FORJA.md`: la escalada se decide sobre el peor capitulo, y aqui no hay ninguno que
escale: los tres estan en la misma poblacion vacia.** No es `0,00` por ciento (eso exigiria al menos un
paso escrito contra el cual medir): es ausencia de poblacion, y se declara como tal en vez de
disfrazarla de un cero que no midio nada.

### G8.5.b. La muestra de fidelidad con su semilla escrita (`D.58`, regimen ligero)

Salida de
`python scripts/muestra_fidelidad.py --libro gerber_emyth --capitulos cap_20,cap_21,cap_22 --semilla gerber_v8`,
guardada en `.gerber_v8/muestra_fidelidad.txt`:

<!-- TALLADO: salida=.gerber_v8/muestra_fidelidad.txt -->

    MUESTRA DE FIDELIDAD DEL REGIMEN LIGERO (D.58)
      libro    : gerber_emyth
      semilla  : gerber_v8
      capitulos: cap_20, cap_21, cap_22

      RELEIDO ENTERO : cap_21
      POR MUESTRA    : cap_20, cap_22, 15 pasos cada uno

      EL DISPARADOR: si la muestra de un capitulo pasa del 10 por ciento de
      pasos inventados, ESE CAPITULO SE RELEE ENTERO ANTES DE SEGUIR.

      --- cap_20: 0 paso(s) en la muestra

      --- cap_22: 0 paso(s) en la muestra

      --- cap_21: ENTERO, 0 paso(s), no hay muestra que elegir

**LA SEMILLA `gerber_v8` REPARTE IGUAL QUE SIEMPRE (`cap_21` ENTERO, `cap_20` y `cap_22` por muestra),
PERO LOS TRES DAN `0` PASOS: NO HAY CANDIDATOS DE LOS QUE MUESTREAR.** El disparador del `10` por ciento
no tiene sobre que dispararse (`0` de `0` no es una fraccion). **NO SE DISPARA NADA, PORQUE NO HAY NADA
QUE DISPARAR.**

### G8.5.c. Los punteros `D.37` que la bandeja deja abiertos, publicados para la vuelta que inserte

**NO LOS DECLARO YO** (`EXTRACTOR.md` `15.6`: esas aristas se declaran en la misma vuelta en que se
INSERTAN las partes, y esta vuelta no inserta, `MODO_INSERCION=cuarentena`). Los tres que ya trae el
encargo, sin tocar:

    d098   D.37, cap_05 L29, la terna sin cabeza
    d104   D.37, cap_12 L21, la terna sin cabeza
    d111   la serie de cap_13: el paso 8 de recorrer_siete_pasos_programa_desarrollo_negocio dice
           "Paso 5: Your People Strategy", que es el titulo de
           construir_estrategia_gente_cuatro_componentes. ARISTA DECLARABLE POR LECTURA.

**Y NINGUN PUNTERO NUEVO NACE DE ESTA VUELTA:** los tres capitulos minados hoy (`cap_20`, `cap_21`,
`cap_22`) cerraron con cero candidatos, asi que no hay hijo nuevo que emparejar con una cabeza de serie.
