# MANUAL DEL SISTEMA DE CONOCIMIENTO
## Como construir un grafo de conocimiento procedimental desde cero, sin retrabajo
Version 1.0, 12 de agosto de 2026. Destilado de la campaña de saneo de My Idea
(3.388 pares auditados, 69 operaciones de reparacion planificadas, 30 reglas de
doctrina). Este documento existe para que el proximo grafo nazca limpio: todo lo
que aqui se manda, esta casa lo aprendio pagandolo.

## 1. Los diez principios
1. UN CONCEPTO, UN NODO. La duplicacion no es un accidente estetico: cada copia
   divide las aristas, las busquedas y las correcciones futuras.
2. LA JERARQUIA SE CABLEA, NO SE COPIA. Cuando una linea de un nodo se despliega
   en otro nodo, eso es madre e hijo y pide arista, jamas un segundo nodo que
   repita a la madre. El 40 por ciento del daño de esta casa fue jerarquia sin
   cablear.
3. TODO ID PASA POR EL RESOLUTOR. Ningun conteo, guarda o busqueda compara ids
   literales: se resuelve primero (alias incluidos) y se compara despues. Un
   chequeo literal inventa salud (auto-aristas invisibles) e inventa enfermedad
   (aristas a deprecados que si resuelven).
4. LAS SEÑALES DE SUPERFICIE ORDENAN, NUNCA DECIDEN. Vocabulario compartido
   (3 por ciento de precision medida), familia de id (50,8 por ciento), titulo
   espejo, subcadena y sinonimo traducido: las cinco sirven para priorizar una
   cola, ninguna para emitir veredicto. Decide la lectura.
5. TODA CIFRA LLEVA SU FECHA DE CORTE, y toda glosa lleva el corte de la cifra
   que interpreta. Una tasa parcial no es la tasa de un dominio; toda tasa
   publicada lleva su banda al lado o es media cifra.
6. LAS CORRECCIONES NO BORRAN: DECLARAN. El texto viejo queda en pie, tachado
   por la correccion. Una correccion que tapa lo que corrige no se puede
   auditar.
7. UNA BUSQUEDA NEGATIVA NO SE PUEDE CITAR. Un estado se comprueba abriendo el
   archivo; una ausencia solo se afirma con el universo leido entero. Toda
   perdida de catalogo declarada se re-verifica, sin importar quien la declare.
8. LA FUENTE ES UN CAMPO SAGRADO. Se escribe canonica (una sola grafia por
   libro), con el orden significativo (la fuente añadida va en segundo lugar),
   y toda atribucion es una afirmacion que se verifica: una cita que admite lo
   que el citado prohibe es una cita falsa.
9. EL VEREDICTO NO ES EL RIESGO: LA FUSION LO ES. Detectar duplicados es
   barato; fundirlos mal pierde nombres, puertas, destinos, variantes, sentidos
   y salvaguardas. Por eso el reparto de perdidas es la mitad del trabajo.
10. EL QUE MIDE NO ADJUDICA. Dos roles siempre: uno ejecuta y mide, otro
    verifica clonando, relee a ciegas y decide criterios. Los errores de ambos
    se declaran con nombre.

## 2. Fase cero: antes del primer nodo
Nada de contenido hasta que exista esta maquinaria (un dia de trabajo que ahorra
meses):
- ESQUEMA DEL NODO fijado por escrito: id canonico, titulo, resumen teorico,
  pasos accionables (imperativos, un procedimiento real por nodo), condiciones
  de activacion, entregable esperado, fuente(s) canonicas en orden, ids_alias,
  nodos_previos y nodos_siguientes CON SEMANTICA DECLARADA (aqui: secuencia
  dirigida; en una escalera, la vuelta no es redundante: es falsa).
- REGLAS DE ID escritas: un solo idioma, sin sufijos numericos (_2, _3), sin
  variantes por preposicion o articulo, sin traducciones paralelas. Si dos
  cosas merecen ids parecidos, merecen revision antes de existir.
- RESOLUTOR de ids desde el dia uno, usado por TODO el codigo (runtime,
  scripts, guardas). Los accesos que resuelven a pelo fallan en silencio el dia
  que un id muere.
- GATE DE INTEGRIDAD (se corre en cada commit): cero huecos, cero auto-aristas
  TRAS RESOLVER, cero aristas duplicadas tras resolver, cero vueltas en
  escaleras, ids validos, esquema completo. Toda guarda con caso positivo: una
  prueba que no puede fallar no guarda nada.
- HOOK DE ESTILO de la casa (aqui: prohibicion de guiones largos y medios) y
  BANCO DE REGLAS versionado en el repo: las doctrinas se citan por numero, se
  corrigen con fecha, y nadie inventa reglas en caliente.
- BITACORA DE VEREDICTOS en formato fijo (jsonl: par, clase, razon, fecha):
  la razon escrita es el activo mas reutilizable del sistema entero.

## 3. La aduana de insercion (el paso a paso de cada nodo nuevo)
La aduana no juzga: obliga a juzgar. Ningun nodo entra sin pasar por aqui.
1. NORMALIZA: id segun las reglas, fuente canonica, denominaciones detectadas
   (nombre largo, sigla, termino en otro idioma: son TRES denominaciones
   aparte y cada una se registra).
2. BLOQUEA (busca vecinos) con VARIAS señales a la vez, porque se solapan poco
   (aqui, similitud semantica y barrido paso-contra-nodo compartian solo un 3 a
   6 por ciento): indice semantico contra su dominio y el nucleo, familia de
   id, y paso-contra-nodo (el texto de un paso contra los nodos existentes).
3. SI ALGUN VECINO SUPERA EL UMBRAL: la insercion se bloquea hasta que quien
   inserta escriba el veredicto continua-o-repite citando el id del vecino
   (seccion 4). Continua: se cablea la arista madre-hijo en el acto. Repite:
   el nodo NO entra: su material propio viaja al existente como perdidas
   repartidas (seccion 6).
4. SI ES SERIE NUMERADA de un libro: un nodo por paso mas UNA cabeza, jamas
   dos compresiones de la misma numeracion.
5. SI ES UN CASO O ESTUDIO: el caso no es la casa. La doctrina vive en su nodo
   y el caso entra como ejemplo nombrado dentro de ella (señal barata: el
   entregable del caso lleva un dato del caso).
6. SI CABLEA MARCO LEGAL DE UN PAIS, norma con version, herramienta con URL o
   cifra del autor: se registra en su censo (marco, vigencia, herramientas,
   atribuciones) al entrar, no en una auditoria posterior.

## 4. La vara: el criterio unico de duplicacion
La pregunta es una: ¿el candidato CONTINUA el trabajo del existente o lo
REPITE? Reglas medidas:
- TIENE DIRECCION: se pregunta que añade el HIJO a la MADRE, nunca al reves.
  Una linea que tarda siete pasos en ejecutarse es un procedimiento nombrado en
  una linea, y la prueba de que es procedimiento es que existe quien lo ejecuta.
- NO TIENE BASCULA: el tamaño del solape no decide; decide si lo que queda
  fuera es procedimiento en los dos lados.
- UNA ADVERTENCIA ES LINEA, no procedimiento. Una postura no ejecuta una
  busqueda. Un mapa sin sentidos no es medio mapa.
- LA ARISTA NO EXCULPA: una de cada nueve duplicaciones de esta casa tenia la
  arista puesta. El cable dice que alguien vio la relacion, no que los nodos
  hagan cosas distintas.
- DOS DOCTRINAS LEGITIMAS NO SON DUPLICADO: son FRONTERA DECLARADA (se
  escribe, con las dos posiciones y sus fuentes; una frontera se pierde por
  poda, no por fusion). Una contradiccion dentro de una misma fuente es un
  defecto de instruccion (falta una condicion), no una frontera.

## 5. Fusiones: como se repara sin perder nada
- EL ACTO SE COMPUTA: el conjunto a fundir es el cierre transitivo de los
  pares REPITE (solo los A construyen el acto; un par sano saca al nodo, no
  añade contendiente). El cierre convoca, la lectura decide: el acto se lee
  ENTERO despues de destejer y antes de fundir, porque la transitividad puede
  fallar y una vez fundido la pregunta es irrespondible.
- SUPERVIVIENTE: el contenido decide (quien contiene y aporta); el cableado
  desempata SOLO a contenido empatado (prelacion, no desprecio). El
  superviviente es final cuando ninguna lectura restante puede cambiarlo; si
  la nomina crece, se re-mide tambien al superviviente.
- REPARTO DE PERDIDAS con la tabla de seis motivos, todos invisibles para la
  vara (valor sin procedimiento nuevo): NOMBRE (la palabra por la que se
  llega: viaja como denominacion en el texto; el alias cubre el id, no la
  busqueda del lector; sigla y termino traducido son denominaciones aparte),
  ALCANCE (las puertas de otro rubro: viajan a la enumeracion), DESTINO (a
  quien va el entregable: paso final), METODO ALTERNATIVO (la variante para
  otra restriccion: variante condicional dentro del paso), DIRECCION (el
  sentido de los flujos: dentro del paso), SALVAGUARDA (la advertencia contra
  un sesgo por defecto: se adosa al paso de decision que protege). Ademas: la
  persuasion es contenido (benchmarks, casos, cifras del autor con su
  atribucion) y la escala es contenido (quien conserva la version ejecutable
  a escala minima).
- SIMULACION OBLIGATORIA sobre copia en memoria antes de escribir la operacion
  (entradas redirigidas, duplicadas nuevas, auto-aristas nacientes), y toda
  arista nueva se escribe RESUELTA al dia de su escritura: el resolutor es una
  red de seguridad, no una licencia.
- ORDEN: fuentes antes que destejidos, destejidos antes que fusiones, fusiones
  antes que enlaces que apunten a nodos que mueren, y la limpieza de duplicadas
  al FINAL (cada fusion fabrica la suya).

## 6. Gobernanza y auditoria continua
- DOS CONTROLES SIEMPRE: relectura ciega de una muestra de los REPITE (nodos
  primero, razon tapada, empezando por los discutibles que el ejecutor marco
  ANTES de saber si acierta) y muestra pineada de los SANOS (el error de dejar
  pasar tiene tasa y banda, o no esta medido). METRICA DE CREDITO publica:
  caidas dentro contra fuera del marcado; una caida fuera mueve el credito de
  toda la tanda.
- Los pendientes de doctrina no detienen el trabajo (se marcan y siguen);
  las contradicciones con regla o cifra publicada SI detienen y se traen.
- Todo hallazgo urgente viaja en el mensaje del commit; los reportes, en
  checkpoints con marcador recomputado del archivo, nunca de memoria.

## 7. Crecimiento: la entrada de un libro o mundo nuevo (checklist)
1. Fuente canonica registrada antes del primer nodo.
2. Cada nodo entra por la aduana (seccion 3), uno a uno.
3. Al cerrar la extraccion: barrido posicional de fuente (injertos declaran la
   fuente en segundo lugar), censo de series y cabezas, censo de casos, censo
   de marco-pais y vigencias del mundo nuevo.
4. Los veredictos de aduana del mundo nuevo se auditan con la ciega de la
   seccion 6 antes de dar el mundo por integrado.

## 8. Escalado autonomo
Con las secciones 2 a 7 escritas, el sistema se opera con dos agentes en bucle
(ejecutor y auditor, modelos distintos, estado compartido en el repo, paradas
definidas: doctrina nueva, contradiccion, decision de dueño, campaña
consumada). El protocolo completo vive en docs/loop/ de esta casa y es
transplantable tal cual.

## 9. Estado del arte externo, y que añade esta casa
Lo que esta casa hizo tiene nombre en la industria: ENTITY RESOLUTION para
grafos de conocimiento. El pipeline estandar coincide pieza a pieza con el
nuestro: blocking por embeddings (nuestra cola por similitud), matching por
pares con LLM (nuestra vara), componentes conexas (nuestro cierre transitivo),
y fusion canonica con procedencia (nuestro superviviente con ids_alias). Las
lecciones publicadas confirman las nuestras: el blocking importa mas que el
matching y conviene multi-señal; separar el NOMBRE de la IDENTIDAD es lo que
evita que dos entidades distintas se fundan en silencio; y las fusiones mal
diseñadas pudren la confianza en el grafo entero. Lo que la literatura NO trae
y esta casa si: la vara con direccion y sin bascula para nodos PROCEDIMENTALES
(la industria funde entidades; nosotros distinguimos continua de repite, que
es mas fino), la tabla de perdidas de seis motivos, las fronteras declaradas,
el banco de doctrina con jurisprudencia fechada, y la capa de auditoria ciega
con metrica de credito. Veredicto: se conserva el metodo de la casa, se adopta
el vocabulario de la industria (este manual ya lo usa), y se adopta su enfasis
en blocking multi-señal, que nuestras mediciones (solape del 3 al 6 por ciento
entre señales) confirman por via propia.
