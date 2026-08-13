# BANCO DE REGLAS de forja-nodos

Anclaje: MANUAL_SISTEMA_DE_CONOCIMIENTO seccion 2: "BANCO DE REGLAS versionado
en el repo: las doctrinas se citan por numero, se corrigen con fecha, y nadie
inventa reglas en caliente".

Aqui viven las reglas de ESTA forja: las que el manual manda y las que esta
casa tuvo que decidir para poder ejecutarlo. Se citan por numero (D.1, D.2) en
los veredictos, en los commits y en las actas del bucle.

Como se corrige una regla: se añade la correccion DEBAJO, con su fecha, y el
texto viejo queda en pie. Una correccion que tapa lo que corrige no se puede
auditar (manual principio 6). Nadie inventa reglas en caliente: si un caso pide
una regla que no existe, se marca PENDIENTE DE DOCTRINA en la razon del
veredicto y se sigue (docs/loop/EJECUTOR.md regla 3).

## D.1. Semantica de las aristas (12 ago 2026)
`nodos_previos` y `nodos_siguientes` son SECUENCIA DIRIGIDA de madre a hijo. La
arista existe en los DOS extremos (la madre declara al hijo en
`nodos_siguientes` y el hijo declara a la madre en `nodos_previos`); un extremo
sin el otro es un hueco y el gate lo declara.
La vuelta (el mismo par declarado en los dos sentidos) es un fallo, no una
redundancia. Vale para TODO par, no solo para las series numeradas.

## D.2. Toda comparacion de ids pasa por el resolutor (12 ago 2026)
Manual principio 3. Ninguna comparacion literal de ids fuera de
src/resolutor.py. El gate resuelve antes de contar auto-aristas, duplicadas,
vueltas y aristas rotas. La prueba D de tests/test_aceptacion.py es el caso
positivo de esta regla.

## D.3. Las señales ordenan, nunca deciden (12 ago 2026)
Manual principio 4. Las tres señales de la aduana (similitud de texto, familia
de id, paso contra nodo) construyen una cola de lectura. Ningun umbral de
config/umbrales.json puede insertar ni bloquear un nodo por si solo: la
insercion se bloquea hasta que una PERSONA escriba un veredicto con su razon.

## D.4. Calibracion de los umbrales (12 ago 2026)
Valores de arranque: similitud de texto 0,45; familia de id 0,50; paso contra
nodo 0,55. Estan medidos sobre cinco casos plantados (gemelo, hijo, familia
parecida, vecino legitimo y nodo ajeno), NO sobre un corpus real. Se recalibran
con el primer libro de verdad, y el recalibrado se declara aqui con su fecha y
con los casos que lo movieron.

## D.5. La familia de id no conjuga verbos (12 ago 2026)
La clave de familia normaliza sufijos numericos, preposiciones, articulos,
plurales y orden de palabras. NO normaliza formas verbales:
`registrar_fuentes` y `registro_fuentes` son familias distintas para el codigo.
Limite aceptado a sabiendas: un normalizador de verbos fusionaria ids legitimos
en silencio, que es peor que el fallo que evita. Detalle y ejemplos en
docs/REGLAS_DE_ID.md.

## D.6. A los alias se les exige forma, no doctrina (12 ago 2026)
Un `ids_alias` cumple snake_case y nada mas. Un alias existe porque alguna vez
se escribio un id que hoy no se aceptaria: exigirle doctrina borraria la
memoria de los errores y romperia las cadenas del resolutor. Al id canonico se
le exige todo.

## D.7. La aduana normaliza forma, nunca doctrina (12 ago 2026)
La aduana baja el id a minusculas, le quita acentos y convierte espacios y
rayas en guion bajo. Si despues de eso el id sigue rompiendo una regla, se
rechaza. Un id maquillado hasta pasar es una decision tomada por una maquina.

## D.8. Ningun veredicto sin razon escrita (12 ago 2026)
CONTINUA, REPITE y SANO exigen razon. La razon escrita es el activo mas
reutilizable del sistema entero (manual seccion 2). Un SANO sin razon es un
nodo que entro por cansancio, y la aduana lo rechaza.

## D.9. REPITE no escribe nada (12 ago 2026)
Cuando un veredicto es REPITE, el nodo NO entra y el comando imprime la
plantilla de reparto de las seis perdidas. La aduana NO ejecuta la fusion: la
fusion se planifica en plantillas/OPERACION_DE_FUSION.md, con simulacion previa
y caso positivo, porque el veredicto no es el riesgo, la fusion lo es (manual
principio 9).

## D.10. El orden de las fuentes se comprueba a mano (12 ago 2026)
El manual pide que la fuente añadida por injerto vaya en SEGUNDO lugar
(principio 8) y manda un barrido posicional al cerrar cada libro (seccion 7.3).
El gate NO puede comprobarlo solo: no sabe cual de las fuentes de un nodo llego
por injerto. Queda como paso de mano en docs/FLUJO_DE_EXTRACCION.md fase 3.
PENDIENTE: si en el futuro el nodo registra la fecha en que cada fuente se
añadio, esta regla pasa a ser automatica y se declara aqui.

## D.11. Alcance del blocking (12 ago 2026)
Por defecto el candidato se mide contra TODO el dataset. El manual habla de
medir "contra su dominio y el nucleo" (seccion 3.2), pero el nucleo de esta
forja todavia no existe. Cuando el grafo crezca y el coste lo pida, se activa
`solo_dominio_y_nucleo` en config/umbrales.json y se declaran aqui, con fecha,
que dominios forman el nucleo. Hasta entonces, medir de mas es mas barato que
dejar pasar un gemelo.

## D.12. Cero guiones largos y cero guiones medios (12 ago 2026)
Hook de estilo de la casa (manual seccion 2). Vale para TODO el repo, codigo
incluido. Los archivos que tienen que nombrar esos caracteres los escriben con
escape unicode: una guarda que se perdona a si misma deja de ser una guarda.
El hook no se salta. Si falla, se corrige y se reintenta.
