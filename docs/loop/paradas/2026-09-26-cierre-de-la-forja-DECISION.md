# DECISION DEL FUNDADOR, 26 SEP 2026: **CIERRE DE LA FORJA**

*Recogida con la linea serial parada (la campania cerro el 26 sep 2026 a las 21:53, `ACTA 79`, tag
`primer-equipo-completo`). El texto del fundador la fecha "28 sep 2026"; el reloj de la maquina marcaba el 26 sep
2026 a las 22:07 al recogerla. Por la nota `2026-09-25-fechas-de-las-decisiones-NOTA.md`, **vale la fecha del commit
que la recoge**.*

1. **Antes de fundir, por el proceso de la forja y con su auditoria:** el nodo del mundo 11 sin clase de pais
   (`evitar_preguntas_ilegales_entrevista`: contratar como metodo, segun `POLITICA_MARCO_PAIS.md` de My-idea) y las 3
   cifras de mercado (`vender_puesto_jugador`, `nombrar_delegados_amigos_casa`, `repartir_material_antes_reunion`: la
   cifra de mercado sale). Gate, suite y cierre en verde.
2. **Fundir `extraccion-mundo-11` en `main`** (`merge --no-ff`), con gate y suite en verde despues, y crear el tag
   `forja-mundo-11`.
3. **No hay mundo 12: la forja queda en reposo.** Las 11 preguntas de doctrina, las 44 deudas y la ficha de
   `bernerslee_bananas` quedan en sus fichas, sin trabajo ahora. La duda `79.9` del auditor se da por buena su
   lectura, sin reabrir nada.
4. Reportar el commit y el tag finales, y el censo del pack del mundo 11 que se integrara en My-idea (471 nodos, sin
   los 6 de ONU ni los 2 semilla).

## Como se cumplio el punto 1

- **La via.** La casa no tenia ninguna operacion para quitar un fragmento de un paso o de un resumen (`corregir` solo
  aniade al resumen; `scripts/retirar_paso.py` saca un paso entero). Nace `src/sustitucion.py`
  (`python forja.py sustituir`), por `EXTRACTOR.md` 2: operacion escrita, bajo cerrojo (D.44), con simulacion sobre
  copia y gate antes de escribir, marca de CORRECCION DECLARADA en el propio nodo y el texto anterior literal en la
  bitacora; con sus pruebas y cada guarda con su caso positivo (`PruebaSustitucionDeclarada`).
- **La auditoria.** Un auditor independiente leyo la operacion, sus pruebas y las sustituciones contra la doctrina de
  la casa y dio ROJO con siete puntos (la fecha, el cerrojo, un caso positivo que no probaba el gate, la normalizacion
  de espacios, la falta de rastro en el nodo, dos frases de `evitar_preguntas_ilegales_entrevista` que seguian leyendo
  la lista de Estados Unidos como universal, y el "pregunta el importe en tu mercado" de la prima). Los siete se
  corrigieron; los datos se descartaron y se volvieron a escribir con la operacion corregida.
- **Queda para el fundador, sin bloquear:** la cifra de la autora en `repartir_material_antes_reunion.atribuciones`
  ("miles de dolares de productividad desperdiciada", cifra del autor con su fecha, EXTRACTOR.md 9), que la operacion
  no alcanza; `censos/marco_pais.md` conserva el texto de marco con el que entro el nodo; y las lecturas que
  `forja.py rancios` da por rancias en estos nodos (D.15, no bloquean).
