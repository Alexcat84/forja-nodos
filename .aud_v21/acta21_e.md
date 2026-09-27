
---

## 12. LO QUE ESTA ACTA PUBLICA, EN UNA TABLA (`5.3`)

**LAS GUARDAS DEL CIERRE, CORRIDAS DESPUES DE ESCRIBIR ESTA ACTA Y EL ENCARGO** (`9.2`, mi `orden 3`):

    $ python forja.py guiones
      BARRIDO DE GUIONES VERDE: cero guiones largos y cero guiones medios.
    $ python forja.py gate
      GATE VERDE.  nodos verificados: 203
    $ python tests/test_aceptacion.py | tail -1
      total: 98 pruebas, 0 fallos, 0 errores

**Y LAS RUTAS QUE YO PUBLICO COMO PRUEBA, CONTADAS AL FINAL DE TODO** (cosecha `7.B`, y con la
leccion de `4.7` aplicada a mi misma tabla):

| ruta mia | comando | salida |
|---|---|---:|
| `.aud_v21/barrido/*.txt`, un fichero por candidato | `ls .aud_v21/barrido/*.txt \| wc -l` | **13** |
| `.aud_v21/*.py`, mis dos guiones de barrido | `ls .aud_v21/*.py \| wc -l` | **2** |

**LAS DOS FILAS CUENTAN ARTEFACTOS CERRADOS Y NO EL FICHERO QUE ESTOY ESCRIBIENDO**, que es
exactamente la distincion que `4.7` adjudica. **Los fragmentos de esta acta no llevan fila**, a
proposito.

| | |
|---|---|
| **vuelta auditada** | **21**, lote 4 (`scott_radical_candor`), **`cap_10` (`Cap. 7`, `Team`) CERRADO ENTERO**. **Sin hueco de acta** (`0`) |
| **hash verificado** | `d1937b6` (cierre de la vuelta 21), sobre `f2afdeb` de apertura. Cuatro commits del extractor, revisados uno a uno por lo que tocan (`9`) |
| **sello de mi apertura ciega** | `47153396dc9369bb930421ae0c3fde2bdf22f7ea`, **intacto**, y **incompleta: le faltan sus secciones 6 a 9** (`0.3`, `8.2`) |
| **herencia `D.40`** | declarada en la fase ciega con la huella `2b3ce599...` remedida por mi. **Tres `CUMPLIDO`, y uno de los tres era falso** (`8.2`) |
| **las guardas** | `gate` **VERDE 203**, `guiones` **VERDE**, `test_aceptacion` **98 pruebas, 0 fallos**, **las tres corridas por mi al abrir y al cerrar**. **El arbol arranco limpio por primera vez**, que es `D.33` ensanchada funcionando |
| **mutaciones de guarda** (`5.5`, cosecha `7.C`) | **3 de 3 muerden**: `guiones` con un guion largo plantado, `reglas_id` con el id de `bajo`, y `forja.py arista` **cambiando de extremo** segun cual falte (`2`) |
| **relecturas hechas** | **9** discutibles marcados; **13** filas de candidato con sus pasos recontados; **9** filas de reparto del lote; **15** cuerpos de unidad remedidos; **9** cifras medidas del reporte reproducidas con mi medidor; **9** rutas de prueba corridas; **3.874** medidas de barrido `D.38.4`; **7** lecturas `SANO` releidas; **194** pasos leidos enteros en la fase ciega mas **22** sorteados con semilla (`2110` y `1209`) |
| **puestos releidos** | 9 de 9 marcados; 13 de 13 candidatos; 7 de 7 `SANO`; 13 de 13 barridos; 22 de 194 pasos por sorteo sobre los 194 ya leidos |
| **dentro contra fuera del marcado** | **la unica discrepancia de lectura de la tanda esta DENTRO del marcado** (su discutible 1), **y la caida es mia**. **Fuera del marcado: cero caidas de clase y cero cifras medidas que no reproduzcan** |
| **caidas por especie, extractor** | `CLASE` **0**, `CIFRA PUBLICADA` **0**, `REPORTE` **2 registradas y NINGUNA acumula** (`4.7`, `4.6`) |
| **caidas propias del auditor** | **2 que ACUMULAN en una sola racha**: `CIFRA PUBLICADA PROPIA` (la frontera de `13`, `8.1`) y `REMEDIO ROTO` (el barrido `D.38.4` declarado cumplido sin estarlo, `8.2`). **Mas 1 declarada que no acumula** (la negrita de mi encargo, `8.3`) |
| **rachas al cerrar** | `CLASE` **0 de 2**, `CIFRA PUBLICADA` **0 de 2**, `REPORTE` **2 de 3**, **la mia 1 de 3**. **NO HAY CREDITO ROTO** |
| **barrido `D.38.4`** | **corrido entero hoy**: poblacion **299 = 203 grafo mas 96 bandejas**, `3.874` medidas, `7.118,6` s. **9 filas, 6 pares distintos: reproduce el saldo de la aduana fila a fila** (`5`) |
| **muestra pineada de `SANO`** | **poblacion en sede `0`** (la vuelta no inserto). **Releidos los 7 que la vuelta emitio, que es mas que la muestra minima de 3**: **0 caen**, tasa **0,00**, banda **[0 ; 40,96]**. **`D.8` sobre los 69 en sede: 0 sin razon escrita** (`6`) |
| **`PASOS INVENTADOS`** | **criterio corregido** (`4.8`). `cap_10` # **8,76 (17 de 194)**, firmado por mi; con el decimoctavo candidato dentro seria `9,28`. `cap_09` corregido a **0,37 (1 de 272)**. Lote 4 **2,19 (23 de 1050)**, **declarado INCOMPLETO**: siete filas sin medir con el instrumento ancho. **Peor fila `cap_10` 8,76 contra tope 10: el freno NO se dispara y el tramo sigue en tres capitulos** (`7`) |
| **adjudicaciones** | **8**: la frontera de `cap_10` es **14** (`4.1`); los cinco cortes **confirmados** (`4.2`); las tres `D.37` **no son parada** (`4.3`); el entregable de `facilitar_despido` **se corrige** (`4.4`); los hermanos de serie son **`SANO`** por extension citada (`4.5`); el par de la lupa es **`CONTINUA`** y **su razon se corrige** (`4.6`); las filas de ruta auto referenciales **no acumulan y el remedio se acota** (`4.7`); **el numerador de `PASOS INVENTADOS` cuenta los puentes cazados** (`4.8`) |
| **correcciones declaradas** | **2, las dos MIAS y ninguna borra texto viejo**: la frontera de `13` de la `ACTA 20` `4.6`, y el criterio de la metrica de la `ACTA 20` `6.2` |
| **lo que va a Alexis sin detener el bucle** | **`D.38.5` promete *ya lo levanta* y la medida dice que no** (`11.1`), con su comando; y los ficheros de usar y tirar del arbol (`ACTA 19` `7.6`, mas `.aud_v21/`, `.sec78.tmp.md` y `.sec9.tmp.md`) |
| **volumen de la vuelta siguiente** | **la pieza 14 de `cap_10`** (bloqueante) **mas `cap_11` entero**, con `cap_12` solo si la cuenta real deja hueco bajo el techo de 15 (`10.1`) |
| **estado del bucle** | # **SIGUE. `PROMPT_SIGUIENTE.md` escrito entero, `PARA_ALEXIS.md` NO se escribe** |

> # **LA VUELTA 21 SE CIERRA CON `cap_10` ENTERO Y CON UNA DEUDA QUE ES MIA: LA PIEZA CATORCE.**
>
> **Y LA LECTURA QUE SACO DE LA TANDA, QUE ES LA QUE ME TOCA A MI Y NO A EL:** el extractor lleva
> tres vueltas sin una caida de `CLASE` ni de `CIFRA PUBLICADA`, y esta vuelta **se cazo el solo 22
> cuentas propias** con un instrumento que escribio para cazarse. **Las dos caidas de esta tanda son
> mias, y las dos son la misma enfermedad vista por dos sitios**: una frontera que publique sin
> volver a mirar las lineas que nadie reclamaba, y un `CUMPLIDO` que firme sobre un barrido que no
> habia terminado. **`D.38.2` junto las dos especies en una racha porque son la misma cosa, y esta
> tanda es el ejemplar.**
