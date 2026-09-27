
## 50.14. **LA UNICA CIFRA DE ESTA ACTA QUE MI PROPIA ESCRITURA MUEVE, MEDIDA DESPUES DE ESCRIBIRLA** (`HEREDADO 3`)

**El censo barre `ACTA_AUDITOR.md`, asi que escribir esta acta cambia su cifra.** `50.1.b` publica la de **antes** con la operacion nombrada; esta es la de **despues**, con el acta ya dentro del fichero:

    $ python scripts/censar_rutas.py            (con la ACTA 50 ya anexada)
    rutas publicadas y censadas : 808
      pasan                     : 808
      CAEN                      : 0
    CENSO VERDE

    $ python .v51aud/40_censo_por_doc.py        (con la ACTA 50 ya anexada)
    docs/loop/REPORTE.md             censadas  626   pasan  626   caen 0
    docs/loop/ACTA_AUDITOR.md        censadas  182   pasan  182   caen 0
    docs/loop/APERTURA_CIEGA.md      censadas    0   pasan    0   caen 0

    $ python scripts/tallar_reporte.py          (con la ACTA 50 ya anexada)
    tablas que declaran instrumento : 240
      talladas, celda a celda       : 130
      que DIFIEREN de su instrumento: 0
    TALLADO VERDE

    $ python forja.py gate        GATE VERDE, 346 nodos
    $ python forja.py guiones     BARRIDO VERDE: cero guiones largos y cero guiones medios

Esas salidas miden el censo entero y su reparto por documento, el tallado, y las dos guardas de una linea, todo sobre el arbol **con esta acta ya escrita dentro**.

`LECTURA`: **el censo pasa de `805` a `808` y las tres rutas nuevas son mias**, de `ACTA_AUDITOR.md`, que sube de `179` a `182`. **La coincidencia con el `808` del reporte es una casualidad aritmetica y la digo en vez de aprovecharla**: el suyo era `626` mas `179` mas `3` de la apertura anterior, y el mio es `626` mas `182` mas `0`. **Los sumandos no son los mismos.** El tallado no se mueve (`240 / 130 / 110`), porque mis tablas no declaran instrumento, y `gate` y `guiones` siguen verdes con el acta dentro.

**FIN DE LA `ACTA 50`.**
