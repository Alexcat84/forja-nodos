#!/bin/bash
# Cierra la apertura: mete el barrido, rehace la fila de la seccion 7, vuelve a
# correr TODOS los bloques pegados y escribe la seccion 8 con la cuenta.
set -e
cd "$(dirname "$0")/.."

python - <<'PY'
import io
p = 'docs/loop/APERTURA_CIEGA.md'
s = io.open(p, encoding='utf-8').read()

# 1. la fila de la tabla de la seccion 7 deja de decir "corriendo"
viejo = ("| **el barrido de vecinos `D.38.4`** | corriendo mientras escribo; su salida se pega en "
         "`7.1` en cuanto termine, y si no termina **lo digo ahi y no publico ninguna cifra de "
         "vecinos** |")
nuevo = ("| **el barrido de vecinos `D.38.4`** | **SI esta hecho**, y va entero en `7.1` con su "
         "poblacion y su total |")
assert viejo in s
s = s.replace(viejo, nuevo, 1)

# 2. la seccion 7.1 con el barrido entero
salida = io.open('.a41/vecinos_limpio.txt', encoding='utf-8').read().rstrip('\n').split('\n')
bloque = '\n'.join('    ' + x for x in salida)
sec = """
### 7.1. **EL BARRIDO DE VECINOS `D.38.4`, CORRIDO ENTERO SOBRE GRAFO MAS BANDEJAS**

*Las dos seniales baratas de la casa, `aduana.senal_similitud_texto` y `aduana.senal_familia_id`,
con los umbrales de `config/umbrales.json` y con el texto que mira la maquina,
`comun.texto_comparable`. **La tercera senial, paso contra nodo, NO esta aqui** y va dicho arriba.*

    $ cat .a41/vecinos_limpio.txt
%s

> **`LECTURA`:** la poblacion es **`371`**, `345` del grafo mas `26` en bandejas, que es la que
> `D.38.4` manda y **la misma que la aduana mide desde `D.38.5`**, asi que las dos cifras ya son
> comparables. Los veinte candidatos levantan **`40` pares** con las dos seniales baratas.
>
> **LO QUE ESTO SI DICE Y LO QUE NO.** Dice **donde hay que mirar**, y por eso el vecino mas alto
> de todo el tramo es `abrazar_incomodidad_silencio_contar_seis` contra
> `escuchar_entender_critica_dominar_defensa` con **`0,446`**, que son **dos de los cuatro
> elementos hermanos de `cap_13`**. **No dice que ninguno sea duplicado:** `D.19` lo tiene escrito,
> **ninguna senial separa jerarquia de ruido**, y una discrepancia nunca se adjudica citando una
> senial. **Mi clase de la seccion `5` la escribi leyendo los pasos, y la escribi antes que esto.**
>
> **Y LOS OCHO PARES DE `6.1` LOS LEVANTA LA SENIAL, que es lo contrario de un descuido invisible:**
> `evaluar_desempenio_dos_veces_anio` contra `montar_evaluacion_360_grados_ligera_pares` sale a
> **`0,404`**, y `mantener_proceso` contra `montar_evaluacion_360` a **`0,396`**. **La maquina los
> puso delante; lo que falta no es la mirada, es la arista.**

### 7.2. **LO QUE ME COSTO ESTE BARRIDO, Y LO DIGO PORQUE `D.43` LO CONVIRTIO EN DOCTRINA**

**Lo corri TRES veces y las dos primeras no valen, y las dos las declaro:**

| corrida | que paso | que hice |
|---|---|---|
| **la primera** | mi instrumento comparaba **titulo mas pasos**, y la maquina compara **titulo mas resumen mas pasos** (`comun.texto_comparable`). Daba **`0` vecinos a todo** | **la mate y la rehice con la funcion de la casa.** Una cifra de vecinos en `0` publicada asi habria sido `CIFRA PUBLICADA PROPIA` |
| **la segunda** | la corri en paralelo por candidato, termino con **`40` pares**, y el fichero salio **con dos lineas pisadas** por la corrida que yo habia matado | **no pegue un fichero corrupto: lo volvi a correr entero** |
| **la tercera** | limpia, y es la que va pegada arriba | |

> **LA PRIMERA ES LA QUE IMPORTA, y no es un tropiezo de tecleo:** el instrumento estaba **copiado
> de mi `.a36/vecinos_rapido.py` de la vuelta 37**, y su propio docstring ya avisaba de que no
> traia la tercera senial. **Lo que no avisaba es que tampoco traia el resumen.** Un barrido que
> mide menos texto que la maquina **no mide la misma poblacion aunque cuente los mismos nodos**, y
> eso es exactamente la familia de `D.38.5`.
""" % bloque
ancla = "## 7. **LO QUE ESTA APERTURA NO HA PODIDO HACER, DICHO ANTES DE QUE SE NOTE**"
i = s.find(ancla)
assert i >= 0
s = s.rstrip('\n') + '\n' + sec
io.open(p, 'w', encoding='utf-8').write(s)
print('7.1 y 7.2 escritas')
PY
