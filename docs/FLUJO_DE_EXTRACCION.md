# FLUJO DE EXTRACCION: la entrada de un libro completo

Anclaje: MANUAL_SISTEMA_DE_CONOCIMIENTO seccion 7 (crecimiento). Este documento
es ese checklist convertido en comandos de esta forja. Se sigue en orden y no
se salta ningun paso: cada uno existe porque saltarselo costo retrabajo en la
campaña que destilo el manual.

## Fase 0. Antes de tocar el libro
- [ ] El gate esta verde en la rama donde vas a trabajar:
      `python forja.py gate`
- [ ] El hook esta instalado: `bash hooks/install_hooks.sh`
- [ ] Lees docs/REGLAS_DE_ID.md entero. Un id mal puesto se paga en aristas.

## Fase 1. La fuente canonica, antes del primer nodo
Manual seccion 7.1: "Fuente canonica registrada antes del primer nodo."

- [ ] Elige UNA sola grafia de clave para el libro (procedimiento completo en el
      nodo `elegir_grafia_clave` del propio dataset).
- [ ] Añade la entrada a fuentes/FUENTES_CANONICAS.json con clave, titulo
      completo, autor y año.
- [ ] Comprueba que no colisiona con una clave viva:
      `python forja.py gate`

Ningun nodo del libro puede entrar antes de esto: la aduana rechaza toda fuente
que no este en la tabla, y ese rechazo es deliberado.

## Fase 2. Cada nodo entra por la aduana, uno a uno
Manual seccion 7.2. No hay carga masiva. No la habra: una carga masiva es un
veredicto que nadie escribio.

Por cada procedimiento que el libro nombra:

1. [ ] Escribe el candidato en un JSON con el esquema de esquema/nodo.schema.json.
       Los pasos van en imperativo y describen UN procedimiento real. Recuerda
       la vara: una advertencia es linea, no procedimiento; una postura no
       ejecuta una busqueda.
2. [ ] Corre la aduana:
       `python forja.py insertar candidato.json`
3. [ ] Si levanta vecinos, LEE los vecinos. No mires solo el numero: las señales
       ordenan, nunca deciden (manual principio 4).
4. [ ] Escribe un veredicto por vecino, con su razon:
       - CONTINUA: se cablea la arista madre-hijo en el acto. Pregunta con
         direccion: que añade el HIJO a la MADRE, nunca al reves.
       - REPITE: el nodo NO entra. Rellena plantillas/OPERACION_DE_FUSION.md y
         reparte las seis perdidas hacia el nodo que sobrevive.
       - SANO: escribe POR QUE no son el mismo trabajo. Esa razon es el activo
         mas reutilizable del sistema entero.
5. [ ] Contesta el censo cuando la aduana pregunte (serie, caso, marco de pais,
       vigencia, herramienta con URL). Se registra AL ENTRAR, no en una
       auditoria posterior.
6. [ ] Confirma el verde: la aduana solo escribe con el gate verde sobre la
       copia en memoria.

Casos especiales que el manual nombra por su nombre:
- SERIE NUMERADA (seccion 3.4): un nodo por paso mas UNA cabeza. Jamas dos
  compresiones de la misma numeracion. Queda en censos/series_y_cabezas.md.
- CASO O ESTUDIO (seccion 3.5): el caso no es la casa. La doctrina vive en su
  nodo y el caso entra como ejemplo nombrado dentro de ella. Señal barata de
  que lo hiciste mal: el entregable del caso lleva un dato del caso.
- CIFRA DEL AUTOR (principio 5 y 8): va en `atribuciones`, con autor, fuente y
  fecha de corte. Una tasa sin banda es media cifra.

## Fase 3. Al cerrar la extraccion del libro
Manual seccion 7.3. Cuatro barridos, ninguno opcional:

- [ ] BARRIDO POSICIONAL DE FUENTE: los nodos injertados declaran la fuente
      nueva en SEGUNDO lugar. El orden del campo `fuentes` es significativo.
- [ ] CENSO DE SERIES Y CABEZAS: censos/series_y_cabezas.md. Comprueba que cada
      serie del libro tiene exactamente una cabeza.
- [ ] CENSO DE CASOS: censos/casos.md. Comprueba que ningun caso se quedo
      viviendo como doctrina.
- [ ] CENSO DE MARCO PAIS Y VIGENCIAS: censos/marco_pais.md y censos/vigencia.md
      del mundo nuevo, con su fecha de corte.

Y el estado tecnico:
- [ ] `python forja.py gate` en verde.
- [ ] `python forja.py guiones` en verde.
- [ ] `python tests/test_aceptacion.py` en verde.

## Fase 4. Auditoria ciega antes de dar el libro por integrado
Manual seccion 7.4 y seccion 6. El libro NO esta integrado hasta esto:

- [ ] Toma una muestra de los veredictos del libro en bitacora/VEREDICTOS.jsonl.
- [ ] Relectura CIEGA: imprime primero los PASOS de los dos nodos, adjudica tu
      clase, y SOLO DESPUES destapa la razon escrita.
- [ ] Empieza por los discutibles que el extractor marco ANTES de saber si
      acertaba.
- [ ] Muestra pineada de los SANOS: el error de dejar pasar tiene tasa y banda,
      o no esta medido.
- [ ] METRICA DE CREDITO publica: caidas dentro contra fuera del marcado. Una
      caida FUERA del marcado baja el credito de toda la tanda, y esa tanda se
      relee al doble.

El protocolo de los dos roles (uno ejecuta y mide, otro verifica y adjudica)
esta en docs/loop/EJECUTOR.md y docs/loop/AUDITOR.md. EL QUE MIDE NO ADJUDICA
(manual principio 10).

## Lo que detiene la extraccion y lo que no
- Un pendiente de doctrina NO detiene: se marca en la razon y se sigue.
- Una contradiccion con una regla vigente o con una cifra publicada SI detiene,
  y se trae escrita. No se arregla en caliente.
- Todo hallazgo urgente viaja en el mensaje del commit.
