
---

## P.6. TAREA 5: **LAS FILAS DE RUTA QUE NO PODIAN SER VERDAD, Y LA FILA DE ALCANCE DE `_insertados`**. **CERRADA**

### P.6.a. LO QUE RECOJO DEL DIAGNOSTICO, SIN DISCUTIRLO (`ACTA 21` `1.5` y `4.7`)

**El auditor midio con la hora de cada fichero que mi remedio de la vuelta 20 se ejecuto a la
letra** (las nueve filas con su comando y su salida, la tabla contada la ultima) **y que aun asi dos
filas salieron falsas, porque contaban el fichero que el propio acto de publicar creaba.**
`.t1_v21/*.txt` decia `13` y hoy hay `14`; `.v21/*.md` decia `14` y hoy hay `16`. **Las dos eran
ciertas en el segundo en que se contaron.**

> **NO LO REABRO Y NO ME DEFIENDO.** La frase que me llevo es suya y es la que aplico: **un remedio
> es una promesa que se puede cumplir leyendo y midiendo mejor, y estas dos filas no se arreglaban
> midiendo mejor.** Lo que cambia no es mi cuidado: es **el alcance de lo que la fila cuenta**.

### P.6.b. **EL REMEDIO, ESCRITO EN UN GUION Y NO EN UNA INTENCION** (`D.35`: los dos remedios que han funcionado obligan a teclear algo)

**`.t1_v22/rutas_cierre.py` construye la tabla, y cada fila declara DOS cosas que antes no
declaraba: su ALCANCE (que comando exacto la cuenta) y su ESPECIE (cerrada o auto referencial).**
En las auto referenciales **el guion excluye por nombre los ficheros que van a nacer despues de que
la tabla se cuente, y los imprime**, para que quien audite pueda sumarlos y volver a contar.

**POR QUE VA EN UN GUION Y NO EN UNA REGLA QUE YO ME ACUERDE DE CUMPLIR:** porque el remedio de la
vuelta 20 **era una regla que yo cumpli** y aun asi fallo. **La lista `NACEN_DESPUES` esta escrita en
el fichero**, asi que la exclusion no depende de que yo me acuerde al publicar: depende de que la
lista este bien, y la lista se puede auditar.

    $ python .t1_v22/rutas_cierre.py

EOF_TABLA_RUTAS

**LAS DOS FILAS AUTO REFERENCIALES, CON SUS EXCLUIDOS NOMBRADOS UNO A UNO** (salida del guion):

      .t1_v22/*.txt    excluye 4: salida_rutas_cierre.txt, salida_gate_cierre.txt,
                                  salida_guiones_cierre.txt, salida_aceptacion_cierre.txt
      .v22/*.md        excluye 2: frag_t5.md, frag_cierre.md

> ### **LAS DOS FILAS QUE FALLARON DOS VUELTAS SEGUIDAS SON EXACTAMENTE ESTAS DOS, Y HOY SE PUBLICAN CON SU EXCLUSION DICHA.** Quien las audite suma los seis nombres de arriba y vuelve a contar: `10 + 4 = 14` en `.t1_v22/*.txt` y `4 + 2 = 6` en `.v22/*.md`. **La cuenta publicada no caduca, porque dice de que esta hecha.**

### P.6.c. **LA FILA DE ALCANCE DE `cuarentena/_insertados/`, RECONCILIADA** (`ACTA 21` `1.2`)

*El auditor lo dijo asi y lo recojo: **ninguna de las dos salidas es falsa y ninguna es caida**,
pero una carpeta con dos numeros y sin reconciliar invita a sospechar. **El encargo pide el alcance
del comando en la misma fila**, y va con la reconciliacion entera detras.*

| comando | alcance | cuenta |
|---|---|---:|
| `ls cuarentena/_insertados/*.json \| wc -l` | **glob PLANO**: solo la raiz de la carpeta | **0** |
| `find cuarentena/_insertados -name "*.json" \| wc -l` | **RECURSIVO**: raiz mas subcarpetas | **201** |

**LA RECONCILIACION, IMPRESA DEL ARBOL Y NO TECLEADA:**

       cuarentena/_insertados/onu_consumidor/             6
       cuarentena/_insertados/smart_who/                 59
       cuarentena/_insertados/zhuo_manager/             136
       SUMA DE LAS SUBCARPETAS                          201
       SUELTOS EN LA RAIZ                                 0

> ### **`0` Y `201` SON LA MISMA CARPETA MEDIDA DE DOS MANERAS, Y LA DIFERENCIA ES ENTERA: EN LA RAIZ NO HAY NI UN JSON SUELTO. LOS 201 VIVEN EN TRES SUBCARPETAS POR LIBRO, Y LAS TRES SUMAN 201.**
>
> **Y LA CUARTA SUBCARPETA QUE NO EXISTE ES LA QUE CUENTA LA HISTORIA:** no hay
> `cuarentena/_insertados/scott_radical_candor/`, **porque el lote 4 no ha insertado ni un nodo
> todavia**. Es la misma cifra que `P.0.1` mide por otro lado.
>
> **DESDE AHORA LAS DOS FILAS VIAJAN JUNTAS O NO VIAJA NINGUNA.** La fila que publico en `P.0` de
> esta vuelta ya llevaba su alcance pegado, antes de escribir esta tarea.
