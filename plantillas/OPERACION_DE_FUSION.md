# OPERACION DE FUSION

Anclaje: MANUAL_SISTEMA_DE_CONOCIMIENTO seccion 5, y principio 9: EL VEREDICTO
NO ES EL RIESGO, LA FUSION LO ES. Detectar duplicados es barato; fundirlos mal
pierde nombres, puertas, destinos, variantes, sentidos y salvaguardas. Por eso
el reparto de perdidas es la mitad del trabajo.

Se copia esta plantilla por cada operacion y se rellena ENTERA antes de tocar
un solo nodo. Un motivo en blanco no es un motivo sin contenido: es una perdida
que nadie miro.

---

## 1. Identificacion

- operacion: OP-____
- fecha: ____
- quien ejecuta: ____
- quien verifica: ____ (EL QUE MIDE NO ADJUDICA, principio 10)
- pares REPITE que construyen el acto: ____
- acto completo (cierre transitivo de los pares REPITE): ____

Recuerda: solo los pares REPITE construyen el acto. Un par SANO saca al nodo,
no añade contendiente. El cierre convoca, la lectura decide: el acto se lee
ENTERO despues de destejer y antes de fundir, porque la transitividad puede
fallar y una vez fundido la pregunta es irrespondible.

## 2. Superviviente

- superviviente: ____
- absorbidos: ____
- razon: el CONTENIDO decide (quien contiene y aporta). El cableado desempata
  SOLO a contenido empatado: prelacion, no desprecio.
- [ ] El superviviente es final: ninguna lectura restante puede cambiarlo.
- [ ] Si la nomina crecio durante la lectura, se re-midio TAMBIEN al
      superviviente.

## 3. Reparto de las seis perdidas

Los seis motivos son invisibles para la vara: son valor SIN procedimiento
nuevo. Por eso la vara dice REPITE y aun asi hay material que salvar. Escribe
en cada fila QUE se pierde y A DONDE viaja, o escribe "nada" con su razon.

| motivo | que se pierde del absorbido | a donde viaja en el superviviente | hecho |
|---|---|---|---|
| NOMBRE: la palabra por la que se llega |  | denominacion DENTRO del texto |  |
| ALCANCE: las puertas de otro rubro |  | a la enumeracion |  |
| DESTINO: a quien va el entregable |  | paso final |  |
| METODO ALTERNATIVO: la variante para otra restriccion |  | variante condicional dentro del paso |  |
| DIRECCION: el sentido de los flujos |  | dentro del paso |  |
| SALVAGUARDA: la advertencia contra un sesgo por defecto |  | adosada al paso de decision que protege |  |

Y ademas, porque tambien son contenido:

| motivo | que se pierde | a donde viaja | hecho |
|---|---|---|---|
| PERSUASION: benchmarks, casos, cifras del autor |  | al texto, con su atribucion y su fecha de corte |  |
| ESCALA: la version ejecutable a escala minima |  | quien la conserva, escrito |  |

## 4. Control de denominacion (se comprueba POR SEPARADO)

El alias cubre el id, NO la busqueda del lector. Nombre largo, sigla y termino
en otro idioma son TRES denominaciones aparte y cada una se comprueba y se
registra por separado. Marcar las tres casillas de un tiron es el error que
esta seccion existe para impedir.

| denominacion | valor en el absorbido | ¿esta en el texto del superviviente? | ¿registrada en censos/denominaciones.md? |
|---|---|---|---|
| nombre largo |  |  |  |
| sigla |  |  |  |
| termino en otro idioma (uno por fila) |  |  |  |

- [ ] El id del absorbido queda como `ids_alias` del superviviente.
- [ ] Comprobado que ninguna denominacion se perdio por asumir que el alias la
      cubria.

## 5. Simulacion obligatoria (sobre copia en memoria, ANTES de escribir)

Manual seccion 5. Se simula y se lee el resultado; no se escribe y luego se
mira.

- [ ] entradas redirigidas: quien apuntaba al absorbido y ahora apunta al
      superviviente. Lista: ____
- [ ] duplicadas nuevas: aristas que la redireccion fabrica por duplicado.
      Lista: ____
- [ ] auto-aristas nacientes: aristas que tras la fusion apuntan al propio
      superviviente. Lista: ____
- [ ] toda arista nueva se escribe RESUELTA al dia de su escritura. El
      resolutor es una red de seguridad, NO una licencia.
- [ ] `python forja.py gate` en verde sobre la copia antes de escribir.

## 6. Caso positivo (sin esto la operacion no se ejecuta)

Una guarda que no puede fallar no guarda nada. Escribe aqui la prueba que
FALLA si esta fusion se hace mal, y comprueba que falla antes de arreglarla.

- prueba: ____
- que rompe si la fusion pierde una denominacion: ____
- que rompe si la fusion deja una auto-arista: ____
- [ ] la prueba se corrio EN ROJO antes de la operacion (comprobado que puede
      fallar) y en VERDE despues.

## 7. Orden de ejecucion (manual seccion 5, no se altera)

1. [ ] fuentes
2. [ ] destejidos
3. [ ] fusiones
4. [ ] enlaces que apuntan a nodos que mueren
5. [ ] limpieza de aristas duplicadas AL FINAL (cada fusion fabrica la suya)

## 8. Cierre

- [ ] gate verde: `python forja.py gate`
- [ ] barrido de guiones verde: `python forja.py guiones`
- [ ] prueba de aceptacion verde: `python tests/test_aceptacion.py`
- [ ] veredictos y razones en bitacora/VEREDICTOS.jsonl
- [ ] hallazgos urgentes en el mensaje del commit
- [ ] correccion declarada si esta operacion corrige una anterior: el texto
      viejo queda en pie, tachado por la correccion. Una correccion que tapa lo
      que corrige no se puede auditar (principio 6).

---

## Nota sobre lo que NO es una fusion

Dos doctrinas legitimas no son un duplicado: son FRONTERA DECLARADA. Se
escriben las dos posiciones con sus fuentes y se dejan vivir. Una frontera se
pierde por poda, no por fusion. Y una contradiccion DENTRO de una misma fuente
no es una frontera: es un defecto de instruccion (falta una condicion).
