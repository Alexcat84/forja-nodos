# EL GRAFO DE REFERENCIA

**La campaña de My-idea esta CONSUMADA Y FUNDIDA.** Su catalogo limpio es, desde
el 9 sep 2026, el corpus contra el que esta forja calibra sus señales. Este
documento declara cual es, como se recrea, que trae dentro y que NO es.

## 1. EL CORTE, leido de git

| | |
|---|---|
| repo | `Alexcat84/My-idea` |
| tag | `catalogo-limpio-v1` |
| commit | `1b12832392469afd2ac42775d606e4dfd443ab43` |
| fecha del commit | 2026-09-09 |
| mensaje | *MERGE DE REGISTRO: pasada-unica absorbe la historia de main con su arbol intacto* |
| clon de lectura | `../my-idea-lectura` (carpeta hermana, fuera de este repo) |
| fichero que se lee | `dataset/metadata/master_graph.json`, y nada mas |

**SOLO LECTURA.** Ningun instrumento de esta forja escribe en ese clon. El corte
se comprueba en cada corrida: `calibracion/referencia.py` lee el commit con
`git rev-parse` y lo compara con el declarado, e imprime si coincide.

### Como se recrea

    cd ..
    git clone --branch catalogo-limpio-v1 --depth 1 \
        https://github.com/Alexcat84/My-idea.git my-idea-lectura

Si vive en otro sitio, `FORJA_REFERENCIA` apunta a el.

## 2. EL CENSO, contado del fichero

Medido por `python calibracion/referencia.py`, salida en
`calibracion/SALIDA_REFERENCIA.txt`. **Ninguna celda esta tecleada.**

| | |
|---|---:|
| `total_nodos` que declara el grafo | 3.853 |
| nodos contados por el instrumento | **3.853** |
| vivos | **3.169** |
| deprecados (archivo) | **684** |
| libros distintos | 53 |

El declarado y el contado coinciden: el grafo no miente sobre su propio tamaño.

## 3. LA VERDAD CONOCIDA QUE EL CATALOGO TRAE DENTRO

Esto es lo que hace al catalogo un corpus de calibracion y no solo un corpus
grande. **Viene adjudicado**, y trae las dos clases que el 9.19 separa:

| clase | que es | cuantos |
|---|---|---:|
| **GEMELOS** | pares (superviviente, absorbido) donde el vivo nombra al absorbido en `ids_alias` o `merged_originals`. **Una persona los leyo y adjudico REPITE**, y la fusion se ejecuto | **671** |
| **JERARQUIA** | pares con arista declarada entre dos vivos: **alguien los cableo en vez de fundirlos** | **7.282** |
| **AJENOS** | dos vivos sin arista y sin absorcion. El catalogo esta auditado par a par, asi que son dos procedimientos distintos | muestra azarosa con su semilla |

**POR QUE IMPORTA:** un gemelo plantado por quien calibra mide lo que quien
calibra cree. Un gemelo que la casa leyo, adjudico y fundio mide lo que de
verdad pasa. La banda del 9.19 (*la similitud alta caza duplicados, la media
caza jerarquias*) se puede MEDIR con estas tres clases, y sin ellas seria una
frase.

## 4. EL MAPEO DE CAMPOS, en un solo sitio

My-idea y la forja nombran los mismos campos de otra manera. El mapeo vive en
`calibracion/referencia.py` (`CAMPOS`) y se declara aqui:

| My-idea | forja |
|---|---|
| `node_id` | `id` |
| `titulo_concepto` | `titulo` |
| `resumen_teorico` | `resumen_teorico` |
| `pasos_accionables` | `pasos_accionables` |
| `condiciones_activacion` | `condiciones_activacion` |
| `entregable_esperado` | `entregable_esperado` |
| `dominio` | `dominio` |
| `nodos_previos`, `nodos_siguientes` | igual |
| `deprecado: true` | `estado: "deprecado"` |
| `fuente` (titulo del libro, texto libre) | `fuentes: [{clave, fecha}]`, clave derivada del titulo |

**LO QUE EL MAPEO NO HACE, y se dice para que nadie lo lea como una conversion:**
no arregla ids, no parte fuentes y no inventa denominaciones. Traduce nombres de
campo y nada mas. **Si un id del catalogo rompe `docs/REGLAS_DE_ID.md`, llega
roto a proposito**: esa diferencia entre las dos casas es una de las cosas que
la calibracion tiene que MEDIR, no tapar.

## 5. LO QUE ESTE GRAFO NO ES

- **No es el dataset de la forja.** `dataset/nodos.jsonl` sigue teniendo sus dos
  nodos semilla. Nada del catalogo de referencia se inserta aqui por el hecho de
  estar ahi: lo que entre, entra por la aduana, uno a uno, con su veredicto.
- **No es la tabla canonica de fuentes.** `calibracion/referencia.py` sabe
  derivar una tabla de sus 53 libros para poder correr la aduana sobre el, pero
  esa tabla se le pasa por `FORJA_FUENTES` y **no se escribe en
  `fuentes/FUENTES_CANONICAS.json`**: la tabla de verdad la escribe una persona
  antes del primer nodo de cada libro (manual seccion 7.1).
- **No es una autoridad doctrinal.** La constitucion sigue siendo
  `docs/MANUAL_SISTEMA_DE_CONOCIMIENTO.md`, y las reglas de esta casa
  `docs/BANCO_DE_REGLAS.md`. Este grafo es un CORPUS, no un banco.
