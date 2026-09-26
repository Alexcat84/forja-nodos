## 8. **`R8` MEDIDO SOBRE MI ENCARGO DE LA `76`, CON EL MISMO INSTRUMENTO** (`ACTA 74` `74.11` y `74.12`)

`R8` dice: *toda cifra de medida que escriba en `PROMPT_SIGUIENTE.md` (un reloj, una banda, una cuenta que solo se comprueba abriendo
un fichero, en digito o en letra) va DENTRO de un bloque `$` con su salida, o lleva EN SU MISMA LINEA la seccion del acta donde esta
pegada: ni la de la linea de al lado, ni una ruta de fichero*. El fichero es el encargo que escribi al cerrar la `ACTA 74`, y el
instrumento es el de la `74.12`, corrido sin copiarlo, con su salida de hoy contra la que guardo aquella acta:

@@RUN:0::head -1 docs/loop/PROMPT_SIGUIENTE.md | cut -c1-100; ls -l --time-style=full-iso docs/loop/PROMPT_SIGUIENTE.md | awk '{print $6, $7, $9}'@@
@@RUN:0::python .v75aud/normal/r8_encargo76.py | diff - .v75aud/normal/r8_encargo76.txt && echo "IDENTICO a .v75aud/normal/r8_encargo76.txt, la salida de la ACTA 74 74.12"; python .v75aud/normal/r8_encargo76.py | tail -1@@

(Cada linea con numero, con sus digitos y sus palabras de numero, en `.v75aud/normal/r8_encargo76.txt`.) **LECTURA, grupo a grupo,
que es mia y no del instrumento; las volvi a leer una a una y no copio la de la `74.12`, aunque llego al mismo reparto:**

- **Numeros de vuelta, de acta, de rama o de carpeta de la casa**: `L3`, `L18`, `L21`, `L50`, `L64`, `L69`, `L70`,
  `L74`, `L77`, `L78`, `L79`, `L85`, `L86`, `L88`, `L93`, `L95`, `L96`, `L109`, `L121`, `L124`, `L125`, `L128`.
- **Secciones, reglas, deudas y numeros de tarea o de punto**: `L4`, `L14`, `L17`, `L19`, `L46`, `L52`, `L62`, `L66`, `L68`, `L72`,
  `L76`, `L80`, `L81`, `L83`, `L90`, `L92`, `L94`, `L96`, `L99`, `L105`, `L108`, `L109`, `L112`, `L115`, `L123`, `L138`, `L140`.
- **Identificadores de capitulo, de linea del libro o de fecha**: `cap_22` en `L45`; `cap_14`, `L27` y `L117` en `L103`; `cap_05` y
  `L29` en `L104`; `cap_13`, `cap_18` y `cap_19` en `L111`; el `23` sep en `L24`.
- **Umbrales de la casa**: el `10` por ciento de `L80`, que es regla y no medida.
- **Palabras de numero sin seccion**: *cinco a la vez* (`L23` y `L86`, un tope de la casa), *cinco fichas a la vez* (`L27`, el
  parametro del barrido de la `73`, cuyo reloj va dentro del bloque de `L30` a `L34`), *tres asientos* (`L24`, la frase fija del arnes,
  que el prompt de este turno trae igual), *los dos delante* y *las dos delante* (`L93` y `L103`, los dos nodos de un par y las dos
  lineas del libro), *las tres fases* (`L104`, lo que dice `cap_05` `L29`, citada en la misma linea), *en cero* (`L109`, la meta) y
  *cero guiones* (`L145`, la frase fija). **Ninguna es una cuenta de fichero.**
- **Las cifras de medida** van dentro de un bloque `$` (el reloj de la `73`, la clase, el tablero) o llevan su seccion de la `ACTA 74`
  en la misma linea: `L1`, `L5`, `L16`, `L56` a `L60`, `L65`, `L75`, `L87` y `L118`.

**`R8` CUMPLIDO EN EL ENCARGO DE LA `76`, medido otra vez aqui.**

## 9. **LO QUE DEJO PARA MI TURNO NORMAL, ESCRITO ANTES DE VER EL REPORTE**

1. **`R5`** en su reporte, con `.v64ext/pegado64.py` y `.v64aud/normal/bloques_mudos.py` sacados otra vez de los originales y con la
   cabecera cambiada a la `76`; **y `R9`** en cada fila de su fidelidad y en cada cuenta de PUENTE, con su patron ensanchado contra
   el mio.
2. **El censo con su hash**: que la vuelta no movio el grafo, la bitacora, los censos ni la bandeja de Marquet, y que en la de Gerber
   solo cambiaron las `6` fichas corregidas, **con `git diff`**; **y quien escribio `src/tablero.py` y `tests/test_aceptacion.py` a
   las `06:45:09`** (seccion `2`, punto `3`), con la suite corrida por mi.
3. **Mi fidelidad contra la suya, paso a paso**: mis `176` filas contra las suyas; sus correcciones contra mi lectura de sus textos
   viejos (seccion `3`); **los `8` PUENTE que declaran las fichas contra los `9` de su asunto de commit**; y **el *despues del cambio*
   del paso `4` de `cuantificar_impacto_innovacion_6_pasos`**, que es mi duda y su misma figura del paso `6`. **Si el marca PUENTE un
   paso de hoy que yo lei `T` sin duda, y gana, la caida de lectura es mia.**
4. **Mi barrido contra el suyo, fila dirigida a fila dirigida**, y **mis clases contra sus lineas de veredicto, par a par**; mis
   aristas por lectura contra las suyas, **por par y no por cuenta** (secciones `4` a `6`), con **`d111`, `d108` y `d098`** y **la
   pregunta de regla de la seccion `6`** delante.
5. **Su orden contra mis restricciones** (seccion `7`).
6. **La huella de las `22` fichas** que su cierre dice sellar, contra las mias de `.v76aud/huellas_al_barrer.txt`, tomadas antes de
   barrer y comprobadas al recogerlo.
7. **La muestra pineada de los SANO**: esta vuelta no escribe en la bitacora; los `SANO` de las `22` se muestrean cuando entren.
8. **`R8` sobre el encargo de la `77`**, medido antes de cerrarlo, y **`R10`**: toda salida que pegue en el encargo, corrida despues de
   mi ultima escritura en el registro que mide, o vuelta a correr antes del commit y comparada.

## 10. **ESTA PAGINA CONTRA `R6`, `R7` Y LOS GUIONES, MEDIDA SOBRE ELLA MISMA**

El generador corre dos veces, y estos bloques de la segunda pasada leen la pagina que escribio la primera, identica salvo estos
bloques. El primero cuenta las lineas de bloque `$` que empiezan por una clave de relacion; el segundo, con la copia de
`.v73aud/r7_pagina.py`, cuenta las lineas de bloque que reparten una cifra en clases y cuantas traen su `suma`; el tercero cuenta
guiones largos y medios:

@@RUN:0::grep -c -E "^    +(previos|siguientes|nodos_previos|nodos_siguientes)" docs/loop/APERTURA_CIEGA.md@@
@@RUN:0::python .v76aud/r7_pagina.py@@
@@RUN:0::grep -c -P "\x{2014}|\x{2013}" docs/loop/APERTURA_CIEGA.md@@
