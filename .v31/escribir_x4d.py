# -*- coding: utf-8 -*-
import io

RUTA = "docs/loop/REPORTE.md"
s = io.open(RUTA, encoding="utf-8").read()


def pegar(ruta, desde=None, hasta=None):
    lineas = io.open(ruta, encoding="utf-8").read().rstrip().split("\n")
    if desde is not None:
        for numero, linea in enumerate(lineas):
            if linea.startswith(desde):
                lineas = lineas[numero:]
                break
    if hasta is not None:
        for numero, linea in enumerate(lineas):
            if numero and linea.startswith(hasta):
                lineas = lineas[:numero]
                break
    return "\n".join(lineas).strip()


def sangrado(ruta):
    texto = io.open(ruta, encoding="utf-8").read().rstrip()
    return "\n".join(("    " + l) if l.strip() else "" for l in texto.split("\n"))


tanda = pegar(".v31/tanda_cap11.txt", "| # |", "| | |")
cuadre = pegar(".v31/tanda_cap11.txt", "| | |")
cabeza_tabla = pegar(".v31/cabeza_cap11.txt", "| # |", "| | |")
cabeza_cuadre = pegar(".v31/cabeza_cap11.txt", "| | |")

nuevo = """### X.4.d. **LA TANDA, UNO POR VEZ, CON SU VEREDICTO ESCRITO POR VECINO**

**ONCE CORRIDAS DE `forja.py insertar`, NINGUNA CARGA MASIVA**, y cada candidato archivado en
`cuarentena/_insertados/scott_radical_candor/` **en el mismo acto** (`D.31`). La tabla la cuenta el
instrumento del dato, no yo de memoria:

<!-- TALLADO: script=.v31/tanda.py salida=.v31/tanda_cap11.txt -->

""" + tanda + """

""" + cuadre + """

**Y LAS `16` LINEAS NUEVAS DE LA BITACORA CUADRAN AL DIGITO:** `7` vecinos juzgados mas `9` aristas
declaradas por lectura. **La bitacora tenia `375` al abrir** (`X.0`) **y tiene `391` al cerrar la
tanda.**

> **Y AQUI ME CORRIJO A MI MISMO EN EL INSTRUMENTO, porque la primera version de esta tabla me daba
> `18` aristas y son `9`.** Filtre las lineas de la bitacora **por fecha**, y **la vuelta 30 corrio
> el mismo dia**: nueve aristas suyas entraron en mi cuenta. **Lo que separa las dos vueltas no es la
> fecha sino la LINEA**, y la linea la publique yo mismo en `X.0` (`375` al abrir). El instrumento
> lleva el motivo escrito dentro. **Es la misma especie que `D.15` ya conocia: una cifra que no se
> puede recontar por su sede no es una cifra.**

#### **LOS SIETE VECINOS, CON LA LECTURA QUE LOS DECIDIO** (`EXTRACTOR.md` 2: si la aduana bloquea, lees a los vecinos ANTES de escribir el veredicto)

| par | senial que lo levanta | la lectura, en una linea |
|---|---|---|
| `decidir_quien_comunica_cada_cuanto` contra `construir_confianza_equipo_tiempo_solas` | `paso_contra_nodo` `0,625` | **`SANO`.** El vecino es de `cap_08`, bajo `RESPECT BOUNDARIES`, y usa la reunion a solas como **un medio entre seis** para construir confianza. El solape es de vocabulario: los dos dicen *cada persona que te reporta directamente* |
| `preguntar_seguimiento_hallar_huecos` contra `calibrar_normalidad_preguntas_jefe` | `paso_contra_nodo` `0,673` | **`SANO`, y la direccion es la contraria.** Mi paso `5` pregunta *que es lo que te desvela por la noche* **a quien me reporta**; su paso `6` pregunta lo mismo **a mi propio jefe**. Es la misma linea con el emisor invertido, y `A.4` llama a eso **solape con firma de enlace mutuo**, no `MUTUO` |
| `nutrir_ideas_nuevas_reunion_solas` contra `crear_espacio_seguro_madurar_ideas_nuevas` | `paso_contra_nodo` `0,650` | **`CONTINUA`, y CIERRA LA ARISTA EN COLA de la linea `279`**, escrita cuando entro la madre y que esperaba al hijo. Lo releo con los dos nodos delante y sostengo clase y direccion |
| `montar_reunion_gran_debate` contra `montar_reunion_gran_decision` | `familia_id` `0,600`, `paso_contra_nodo` `0,726` | **`SANO`, hermanos.** El solape es **del libro**: `L201` dice literalmente que las logisticas y normas de la gran decision **son las mismas** que las de la gran debate. **Una remision hacia atras no es una cabeza** (`ACTA 27` `2.2`, linea `24700` del acta) |
| `montar_reunion_gran_decision` contra `montar_reunion_gran_debate` | las mismas | **`SANO`**, el mismo par visto desde el otro extremo. **Lo juzgo dos veces porque la aduana lo levanta dos veces**, y las dos razones dicen quien remite a quien |
| `montar_reunion_gran_decision` contra `nutrir_ideas_nuevas_reunion_solas` | `similitud_texto` `0,354` | **`SANO`, y es RUIDO medido.** `0,354` contra un umbral de `0,35`: **cuatro milesimas.** `EXTRACTOR.md` 11: la banda alta empieza en `0,4` y en la media conviven `745` pares de jerarquia y `1.878` ajenos. **Este es de los `1.878`** |
| `montar_reunion_gran_decision` contra `dirigir_reunion_decision` | `familia_id` `0,400` | **`SANO`, dos libros.** El mio dice **donde encaja** la reunion en el sistema (va tras la de debate, decisor nombrado, decisiones finales, veto); el suyo (`zhuo_manager`) dice **como se delibera dentro**. `similitud_texto` `0,177`: **lejisimos de la banda de gemelo** |

### X.4.e. **LO QUE ESTA TANDA DESTAPA Y NADIE ME ENCARGO: `cap_11` TIENE CABEZA, Y SUS DIEZ PARTES ESTAN ESCRITAS**

*Lo traigo porque `EXTRACTOR.md` 11 me obliga: **un candidato que entra con la cola vacia esta
certificado como SIN GEMELO, no como SIN MADRE**, y **la jerarquia la busca la lectura, no la senial**.
Cinco de los once entraron con la cola vacia.*

**EL PASO `6` DEL PRIMER CANDIDATO DEL CAPITULO ENUMERA LAS DIEZ HERRAMIENTAS UNA A UNA**, porque el
libro las lista en `L17` a `L35`, **un rotulo por linea**. Comprobar cuales existen como nodo es mirar
una lista, que es lo que `EXTRACTOR.md` 15.6 dice de este juicio:

<!-- TALLADO: script=.v31/cabeza.py salida=.v31/cabeza_cap11.txt -->

""" + cabeza_tabla + """

""" + cabeza_cuadre + """

**SEIS ARISTAS CABEZA A PARTE DECLARADAS EN ESTA MISMA VUELTA**, que es lo que `15.6` manda: *declaras
esas aristas en la misma vuelta en que insertas las partes. No en la siguiente, no cuando alguien las
eche de menos.*

> ### **ES `D.29` Y NO `D.37`, Y LA DIFERENCIA LA PAGO EN RAZONES ESCRITAS**
>
> **El paso `6` enumera y NO dice cuantas son.** `EXTRACTOR.md` 15.6, con la correccion del titular
> del 11 sep: *la cuenta es condicion, no un adorno del ejemplo. Si el texto solo enumera sin decir
> cuantas, esto NO es `D.37`: es `D.29`*, y la arista se declara igual **pero con razon escrita que la
> sostenga**. **Las seis la llevan, y cada una nombra que anade el hijo que la cabeza no tiene.**
>
> **Y LA UNICA `D.37` DE VERDAD DE LA TANDA ES OTRA:** `conducir_reunion_equipo_agenda_tres_bloques`
> **dice TRES en su titulo y en su paso `5`**, y nombra los tres bloques (aprender, escuchar,
> aclarar). **De los tres, solo `escribir_apuntes_sala_estudio_equipo` existe como nodo**; los otros
> dos viven dentro de los pasos `8` a `15` y `16` a `22` de la propia madre. **Lo digo en vez de
> callarlo**, porque una serie de tres con una sola arista invita a pensar que faltan dos.

> ### **EL ROTULO `7` NO SE CABLEA, Y ES LA PARTE DONDE ME PARO A PROPOSITO**
>
> El indice dice `Meeting-Free Zones` (`L29`) y **el cuerpo del libro titula esa seccion
> `EXECUTION TIME` / `Fight meeting proliferation`** (`L223`). El nodo que sale de ahi es
> `pelear_proliferacion_reuniones_bloquear_ejecucion`, **que entro hoy**.
>
> **Y AUN ASI NO DECLARO LA ARISTA, porque `15.6` dice que la parte tiene que ser LA QUE ESE PASO
> NOMBRA**, y el paso `6` nombra *las zonas libres de reuniones*. **Que ese rotulo y esa seccion sean
> el mismo hueco de la lista es una inferencia MIA por posicion**, no algo que el texto diga. **La
> enumeracion tiene que estar escrita**, y esta no lo esta. Va a mis discutibles (`X.6`).

### X.4.f. **LA ARISTA CON FECHA DE CADUCIDAD DE `4.d`, DECLARADA EN EL ACTO EN QUE EL HIJO PASO LA PUERTA**

**La aduana dejo entrar a `pelear_proliferacion_reuniones_bloquear_ejecucion` SIN MANDAR LEER NADA**,
exactamente como el auditor midio (`.v30c/informe_pelear.txt`). **Cola vacia, cero vecinos.** Asi que
la declaracion fue el acto siguiente, sin commit de por medio:

<!-- TALLADO: parcial salida=.v31/arista_4d.txt -->

""" + sangrado(".v31/arista_4d.txt") + """

**Y LAS TRES SEÑALES LO DAN POR DESCONOCIDO EN LAS DOS DIRECCIONES:** `familia_id 0.0`,
`paso_contra_nodo 0.454`, `similitud_texto 0.207`, **las tres por debajo de su umbral**. **Si hubiera
entrado sin la declaracion, no habria habido ninguna corrida que volviera a poner a estos dos
juntos**, que es la frase con la que el encargo lo puso como no aplazable.

> **Y LO QUE NO HAGO, que digo para que no se cuente como olvido:** `censos/series_y_cabezas.md`
> **sigue vacio**, con `0` filas bajo su cabecera, **y hoy han entrado una cabeza de diez partes y una
> serie de tres**. `EXTRACTOR.md` 9 manda registrar la serie al entrar, y el censo **lo escribe la
> aduana** (`--censo serie=...`), **no yo a mano**: el propio fichero dice *no se edita a mano salvo
> para corregir*. **Los once ya entraron, y volver a insertarlos no se puede.** Va como propuesta a
> `X.7` con su cifra, no como deuda callada.

"""

viejo = """### X.4.d."""
assert viejo not in s
marca = """## X.5. **TAREA 5**: la cola entera, recontada fila a fila contra el dato"""
assert s.count(marca) == 1
io.open(RUTA, "w", encoding="utf-8", newline="").write(s.replace(marca, nuevo + marca))
print("ok")
