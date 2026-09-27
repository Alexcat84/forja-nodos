# -*- coding: utf-8 -*-
"""Vuelta 64: arma el tramo 64.5 del reporte pegando las salidas guardadas de los instrumentos
(matriz, comprobador, aristas, citas y orden). No mide nada: solo pega."""
import io, collections, glob


def leer(p):
    return io.open(p, encoding='utf-8').read()


sec = collections.OrderedDict()
act = None
for l in leer('.v64ext/veredictos_listos.txt').split('\n'):
    if l.startswith('## '):
        act = l[3:].strip(); sec[act] = []
    elif l.strip() and not l.startswith('#'):
        sec[act].append(l)
MARCAS = ('VECINO NUEVO de la matriz', 'SALIA ENTRARIA', 'VECINO NUEVO por la correccion del vecino',
          'VECINO NUEVO: lo levanta la matriz')
nuevas = collections.OrderedDict()
for k, v in sec.items():
    x = [l for l in v if any(m in l for m in MARCAS)]
    if x:
        nuevas[k] = x
BLOQUES_NUEVOS = ('equilibrar_capacidad_personal_inventario_plazo', 'elegir_inspeccion_barrera_monitorizacion')
comp = [l for l in leer('.v64ext/comprobar_veredictos.txt').splitlines() if not l.startswith('  OK')]
fins = []
nlev = 0
for f in sorted(glob.glob('.v64ext/matriz22_*.txt')):
    for l in leer(f).splitlines():
        if l.startswith('FIN'):
            fins.append(l)
        if l.startswith('LEVANTA'):
            nlev += 1
o = []
o.append('''
## 64.5. TAREA 4: `d141`, LAS ARISTAS POR LECTURA Y EL ORDEN DE LOS `22`

### 64.5.a. LA MATRIZ DE LOS `22`, Y LO QUE `2.c` NO HABIA VISTO

**Para ordenar hace falta saber que par levanta y en que sentido**, y los informes de poblacion `462` son de
antes de mis correcciones. **Mido los `22` contra los `22` en los dos sentidos con `aduana.medir`**
(`.v64ext/matriz22.py`, las fichas de hoy, `462` pares ordenados). **Lo corri en cuatro trozos, uno en primer
plano y tres en paralelo en segundo plano, y recogi los tres dentro del turno**: sus avisos de fin llegaron
antes de seguir, y ningun proceso mio queda vivo.

<!-- TALLADO: parcial salida=.v64ext/matriz22_a.txt -->

    $ grep -h FIN .v64ext/matriz22_a.txt .v64ext/matriz22_b.txt .v64ext/matriz22_c.txt .v64ext/matriz22_d.txt
''')
for l in fins:
    o.append('    ' + l + '\n')
o.append('''    $ cat .v64ext/matriz22_a.txt .v64ext/matriz22_b.txt .v64ext/matriz22_c.txt .v64ext/matriz22_d.txt | grep -c LEVANTA
    %d

**Y AQUI ESTA LO QUE EL PAR A PAR DE `2.c` NO VEIA: nueve sentidos mas levantan hoy**, que ni los informes ni
el par a par listaban (`.v64ext/matriz_nuevos.txt`, que resta de la matriz lo que ya estaba en `pares_despues.txt`),
todos con una ficha corregida en un extremo, y **dos candidatos que salian `ENTRARIA` a poblacion `462` hoy
bloquean**: `equilibrar_capacidad...` contra `construir_indicador_tendencia...`, y `elegir_inspeccion_barrera...`
contra `emparejar...` y `construir_grafico...`. **La causa es la correccion misma**: la nota declarada que se
anade al `resumen_teorico` comparte vocabulario con sus vecinos de capitulo, y la senial `1` lee el resumen. Es
`d031` medida otra vez. **No lo arreglo encogiendo la nota**: la correccion declarada con el texto viejo dentro es
la regla, y la senial solo ordena.

**Sus veredictos, anadidos a la misma sede y comprobados con el mismo instrumento**, que ahora lee tambien la
matriz:

<!-- TALLADO: parcial salida=.v64ext/comprobar_veredictos.txt -->

    $ python .v64ext/comprobar_veredictos.py | grep -v '^  OK'
''' % nlev)
for l in comp:
    o.append('    ' + l + '\n')
o.append('''
**`17` bloques y `49` lineas, cero que falten y cero que sobren.** Los bloques de `64.3` siguen valiendo; lo que
se anade a cada uno, y los dos bloques nuevos, van aqui con el mismo titulo. **La sede completa, con las `49`,
es `.v64ext/veredictos_listos.txt`**, que es de donde la `65` copia cada `--veredicto`.

''')
for k, v in nuevas.items():
    o.append('### VEREDICTOS LISTOS DE %s (%s)\n\n' % (k, 'bloque nuevo' if k in BLOQUES_NUEVOS else 'lineas anadidas a `64.3`'))
    for l in v:
        o.append('    ' + l + '\n')
    o.append('\n')
ar = [l for l in leer('.v64ext/aristas_lectura.txt').splitlines() if l.startswith('SOSTENGO') or l.startswith('NO SOSTENGO')]
o.append('''### 64.5.b. ARISTAS POR LECTURA (D.29)

**Madre, hijo, la linea del libro y la razon, las que sostengo y las que no.** Sede: `.v64ext/aristas_lectura.txt`.
**La senial no levanta ninguna de las `SOSTENGO` en ningun sentido** (matriz de los `22` y `.v64ext/pares_despues.txt`),
salvo la segunda, que hoy si levanta y por eso va ademas en los bloques de veredicto. **Se cablean al insertar el
hijo, con la madre ya en el grafo**, con `python forja.py arista --madre --hijo --paso --razon` (`D.29`, `D.53`).
**Ninguna es serie de `D.37`**: ningun texto de los `22` dice cuantas partes tiene con las partes viviendo como
nodo, y en eso coincido con la apertura sellada (`64.4`).

| | madre | hijo | pasos | linea | razon |
|---|---|---|---|---|---|
''')
for l in ar:
    p = [c.strip() for c in l.split('|')]
    o.append('| **%s** | `%s` | `%s` | %s | %s | %s |\n' % (p[0], p[1], p[2], p[3], p[4], p[5]))
o.append('''
**Las lineas de la tabla, pegadas** (`D.35`), cortadas en el propio `grep -o`:

<!-- TALLADO: parcial salida=.v64ext/citas_t4.txt -->

''')
for l in leer('.v64ext/citas_t4.txt').splitlines():
    o.append('    ' + l + '\n')
o.append('''
> **DISCUTIBLES DE ARISTA, MARCADOS AL ESCRIBIRLAS**
>
> - **`D64.6`**: `construir_grafico_escalonado...` madre de `casar_flujo...` la sostengo **sin rebajarla**, y la
>   apertura sellada la daba con confianza baja por *nombrar no es procedimentar*. Mi motivo: esa vara decide si
>   una linea cuenta como despliegue de otro nodo (continua o repite), no si un hijo usa a una madre; el ejemplar
>   de `D.29` es exactamente un hijo que nombra a su madre en un paso y la usa.
> - **`D64.7`**: `representar_actividad_caja_negra...` madre de `construir_indicador_tendencia...` (L89, *another
>   window in our black box*) es mia y no de la apertura sellada, que solo daba la de la linealidad.

### 64.5.c. EL ORDEN DE LOS `22`, MADRE ANTES QUE HIJO, Y LA TANDA QUE PROPONGO PARA LA `65`

**La tabla la imprime `.v64ext/orden.py`**: lo unico que escribo a mano es la lista del orden; las madres las lee
de los veredictos y de las aristas, el informe vigente y su poblacion de su fichero, los vecinos de la matriz y de
`pares_despues.txt`, y *listos* es que cada vecino que levanta tenga su linea. **Y comprueba las tres reglas**:
ningun hijo delante de su madre, `D.36` (un par que levanta en un solo sentido se inserta con el que lo levanta
despues), y ningun hijo dentro del tope con la madre fuera. La columna *dijo(462)* es lo que dijo su informe
archivado, no lo que diria hoy: `equilibrar` y `elegir_inspeccion` bloquearian (`64.5.a`).

<!-- TALLADO: parcial salida=.v64ext/orden.txt -->

    $ python .v64ext/orden.py
''')
for l in leer('.v64ext/orden.txt').splitlines():
    o.append('    ' + l + '\n')
o.append('''
**LO QUE EL ORDEN CAMBIA RESPECTO AL DEL LIBRO, y por que**: en `cap_02`, `detectar` (`P11`) y
`dimensionar_inventario` (`P10`) suben delante de `rehacer` (`P6`). `detectar` es madre de `dimensionar_inventario`,
y `rehacer` levanta a `dimensionar_inventario` y no al reves (`0,357` contra `0,329`, `.v64ext/pares_despues.txt`),
asi que **`D.36` pide que `rehacer` entre despues para que su informe lea el par**. `cap_03` entra en el orden del
libro, que ya pone cada madre delante.

**LA TANDA QUE PROPONGO PARA LA `65`: LAS FILAS `1` A `20`**, `cap_02` entero y `13` de `cap_03`, con
`variar_frecuencia...` y `simplificar_trabajo...` para la siguiente. Ninguno de los dos es madre de nadie, y los
dos leen a sus vecinos desde el grafo cuando entren. **Proponer no es fijar**: el orden lo fija quien autoriza
(`D.36`), y lo recoge el encargo de la `65`.

**Y EL RELOJ, MEDIDO HOY Y NO PROMETIDO**: `aduana.medir` me costo unos `3,9` s por par con las fichas de Grove en
primer plano (`486` s para `126` pares) y `4,6` s con tres trozos en paralelo (`576` s para `126`), y el barrido de
una sola ficha contra `462` no cupo en `590` s. **Veinte `insertar` son varias horas de aduana**, en primer plano y
uno por vez. **Si no caben en el turno de la `65`, que la tanda sea mas corta, no que alguno quede en vuelo.**
''')
io.open('.v64ext/reporte_t4.md', 'w', encoding='utf-8', newline='\n').write(''.join(o))
print(nlev, list(nuevas))
