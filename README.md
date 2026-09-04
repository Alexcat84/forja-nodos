# forja-nodos

La forja es la maquinaria que convierte un libro en nodos de conocimiento
procedimental SIN fabricar duplicados. No es un editor ni un almacen: es una
ADUANA. Un nodo no entra porque alguien lo escriba, entra porque paso las
guardas y porque una persona escribio un veredicto con su razon.

Su constitucion es docs/MANUAL_SISTEMA_DE_CONOCIMIENTO.md (copia literal,
version 1.0). Toda decision de diseño de este repo se ancla a una seccion suya,
y donde el codigo y el manual choquen, manda el manual.

## El flujo, en cinco lineas

1. Registras la fuente canonica del libro ANTES del primer nodo.
2. Escribes un candidato en JSON y lo pasas por la aduana, uno a uno.
3. La aduana busca vecinos con tres señales a la vez y BLOQUEA si alguno pasa
   el umbral: las señales ordenan la cola, nunca deciden.
4. Escribes un veredicto por vecino (CONTINUA, REPITE o SANO) con su razon;
   CONTINUA cablea la arista madre-hijo en el acto y REPITE deja al nodo fuera.
5. Solo con el gate verde sobre una simulacion en memoria el nodo se escribe.

## Como se corre cada comando

    python forja.py insertar candidato.json

La aduana (manual seccion 3). Normaliza, valida contra el esquema, busca
vecinos y bloquea. Sin vecinos, el nodo entra. Con vecinos, exige un veredicto
por vecino:

    python forja.py insertar candidato.json \
        --veredicto "id_vecino|CONTINUA|madre=id_vecino|que añade el hijo a la madre" \
        --veredicto "otro_vecino|SANO|por que no son el mismo trabajo"

Las cuatro clases y lo que hace cada una:

- `CONTINUA`: exige declarar cual de los dos es la MADRE. La arista se escribe
  en los dos extremos y RESUELTA (con el id canonico, aunque la declares por un
  alias).
- `REPITE`: el nodo NO entra. El comando imprime la plantilla de reparto de las
  seis perdidas y sale con codigo 3.
- `SANO`: el nodo entra, con la razon escrita en la bitacora.
- `MUTUO`: el UNICO enlace bidireccional legitimo (adjudicaciones A.1 y A.4).
  Exige que cada sentido **CITE SU LINEA**, y que las dos sean DISTINTAS:

        --veredicto "id_vecino|MUTUO|ida=<n>:<razon>|vuelta=<m>:<razon>"

  donde `n` es el paso DEL CANDIDATO que el vecino despliega y `m` el paso DEL
  VECINO que el candidato despliega. Si los dos sentidos apuntan a la misma
  linea, eso es un solape disfrazado y se rechaza nombrando el paso. Se cablea
  en los dos sentidos y queda en el REGISTRO DE CITAS
  `config/pares_mutuos.jsonl`, cuya cita el gate verifica entera.

Opciones: `--censo clave=valor` responde el censo sin preguntar (claves: serie,
caso, marco_pais, vigencia, herramienta; `no` si no aplica), `--sin-preguntas`
lo da todo por no aplicable, `--preguntar` fuerza el modo interactivo.

Codigos de salida: 0 entro, 1 rechazado, 2 bloqueado esperando veredicto,
3 REPITE (no entra).

    python forja.py gate

El gate de integridad (manual seccion 2). Verifica el dataset entero: esquema,
reglas de id, fuentes contra la tabla canonica, orden de las fuentes por fecha
en un nodo con mas de una, cero auto-aristas TRAS RESOLVER, cero aristas
duplicadas tras resolver, cero vueltas salvo el enlace mutuo cuya CITA se
sostenga entera, ningun nodo vivo nombrando a un DEPRECADO, aristas solo hacia
ids que existen o resuelven, y cero guiones largos o medios. Sale en verde o
con la lista exacta de fallos.

    python forja.py guiones [ruta ...]

El barrido de estilo de la casa: cero guiones largos y cero guiones medios en
todo el repo. Sin rutas, barre el arbol entero.

    python forja.py rancios

El bloque de vigencia (D.15). Recomputa la huella del texto de hoy contra la
que cada veredicto y cada cita guardaron el dia que se emitieron, y clasifica:
VIGENTE, RANCIO (el texto cambio debajo), SIN HUELLA (incomprobable) y NODO
IDO. Un rancio NO se cita como vigente: se relee o se declara. No pone el gate
en rojo, porque esa salida la decide una persona.

    python forja.py resolutor [id ...]

El resolutor (manual principio 3). Sin argumentos, informa de nodos vivos,
DEPRECADOS, alias y cadenas. Con ids, dice a que resuelve cada uno y por que
camino. Un id deprecado resuelve al superviviente que lo lleva en `ids_alias`.

    python forja.py censos

Crea las plantillas de censo que falten en censos/.

    bash hooks/install_hooks.sh

Instala el pre-commit, que corre el gate y el barrido en cada commit y aborta
el commit en rojo. El hook no se salta: si falla, se corrige y se reintenta.

    python tests/test_aceptacion.py

La prueba de aceptacion. El repo no esta terminado sin ella en verde.

## El arbol

    forja.py                    la unica puerta de entrada
    docs/
      MANUAL_SISTEMA_DE_CONOCIMIENTO.md   la constitucion, copia literal
      REGLAS_DE_ID.md                     manual seccion 2, con ejemplos
      BANCO_DE_REGLAS.md                  las doctrinas, citadas por numero
      FLUJO_DE_EXTRACCION.md              manual seccion 7, el checklist
      loop/EJECUTOR.md, loop/AUDITOR.md   manual seccion 8, el bucle
    esquema/nodo.schema.json    el esquema del nodo, fijado por escrito
    fuentes/FUENTES_CANONICAS.json   clave a titulo completo del libro
    config/umbrales.json        los umbrales de las señales, editables
    config/pares_mutuos.jsonl   REGISTRO DE CITAS de los enlaces mutuos (D.14)
    src/
      comun.py       utilidades, huellas de texto y el barrido de guiones
      reglas_id.py   las reglas de id en codigo
      resolutor.py   TODO id pasa por aqui
      esquema.py     validador de JSON Schema con libreria estandar
      gate.py        el gate de integridad
      aduana.py      el corazon: normaliza, bloquea, exige veredicto
      censos.py      series, casos, marco pais, vigencia, herramientas
      config.py      carga de umbrales
      guiones.py     el hook de estilo
      vigencia.py    el bloque de vigencia: los veredictos rancios (D.15)
    dataset/nodos.jsonl         el grafo
    bitacora/VEREDICTOS.jsonl   fecha, candidato, vecino, señales, veredicto, razon
    censos/                     los censos, escritos al entrar
    plantillas/OPERACION_DE_FUSION.md   las seis perdidas, con simulacion
    ejemplos/                   nodos de ejemplo listos para insertar
    hooks/                      pre-commit e instalador
    orquestador_forja.sh        el arnes del bucle: extractor y auditor
    docs/loop/                  EXTRACTOR.md y AUDITOR_FORJA.md (en borrador)
    tests/                      la prueba de aceptacion, sus fixtures y la
                                prueba del arnes con un claude falso

## Las tres señales del blocking

Se corren SIEMPRE las tres, porque se solapan poco (la casa midio entre 3 y 6
por ciento de solape entre la primera y la tercera):

1. SIMILITUD DE TEXTO: titulo mas resumen mas pasos, con difflib. Caza al
   gemelo que cambio las palabras.
2. FAMILIA DE ID: normaliza sufijos numericos, preposiciones, articulos,
   plurales y orden de palabras. Caza la variante del mismo nombre.
3. PASO CONTRA NODO: cada paso del candidato contra el texto de cada nodo, y
   al reves. Caza al hijo, que despliega en siete pasos una linea que la madre
   nombra en una.

Ninguna decide. Los umbrales de config/umbrales.json mueven cuantos vecinos se
leen, y nada mas.

Y ninguna devuelve CERO SILENCIOSO (D.16): fuera de su dominio de aplicacion
una señal devuelve NO APLICA explicito, que revienta si alguien lo compara con
un umbral. Un cero de señal muerta se lee como salud, y esa confusion tiene
fecha y muertos en la campaña que destilo el manual.

## Lo que esta forja NO hace

- No carga en masa: una carga masiva es un veredicto que nadie escribio.
- No funde nodos sola: la fusion se planifica en
  plantillas/OPERACION_DE_FUSION.md, con las seis perdidas repartidas, la
  simulacion previa y su caso positivo.
- No decide por ti: bloquea y te obliga a escribir la razon.

Python 3 y libreria estandar. Nada que instalar.
