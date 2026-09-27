# DECISION DEL FUNDADOR, 23 SEP 2026: **NINGUN EJECUTOR NI AUDITOR POR DEBAJO DE OPUS 5.5**

*Instruccion dada en la sesion de chat el 23 sep por la tarde, con la serial insertando la
tanda de la vuelta `65`. **La decision va arriba, literal.** Debajo, como quedo aplicada.*

---

## LA DECISION, LITERAL

> asegurate que cualquier ejecutor/auditor use el modelo opus 5.5, no menos que eso.

---

## LO QUE SE MIDIO ANTES DE TOCAR NADA

Del uso real de cada turno (`modelUsage` del JSON que devuelve cada asiento), no del comando:

    serial   extractor  claude-opus-5-5   9,12 USD   (el unico modelo de su turno)
    serial   auditor    claude-opus-5-5   8,16 USD   (el unico modelo de su turno)
    marquet  extractor  claude-sonnet-5   4,28 USD   el ultimo turno por debajo; su linea ya estaba cerrada
    marquet  auditor    claude-opus-5-5   3,51 USD

**La serial ya cumplia.** Lo que faltaba era que no dependiera de escribir bien el comando.

## COMO QUEDO APLICADA, con la serial parada (`PARALELO.md` `7`)

| | donde |
|---|---|
| **el arnes no arranca** si cualquiera de los dos asientos pide un modelo fuera de la lista, y dice cual y en que asiento | `orquestador_forja.sh`, `comprobar_arranque`, frenos `3` |
| **la lista va escrita en el arnes, no en una variable de entorno**: una variable la puede bajar quien lance; cambiar la linea deja rastro en git | `MODELOS_ADMITIDOS="claude-opus-5-5"` |
| **y por dentro**: un subagente que un asiento lance, o que pida `sonnet` u `opus` a secas, hereda Opus 5.5 | `CLAUDE_CODE_SUBAGENT_MODEL`, `ANTHROPIC_DEFAULT_OPUS_MODEL` y `ANTHROPIC_DEFAULT_SONNET_MODEL`, las tres en `claude-opus-5-5`; comprobadas en el binario de Claude Code `2.1.280` |
| **el tablero** publica los dos asientos de la serial en Opus 5.5 con esta cita; la fila de marquet queda como historia de su frente | `config/frentes.json`, `modelos_por_linea` |

**SUS CASOS, en el banco del arnes:** `21` (Sonnet en el extractor: no arranca y no gasta
turno), `21b` (un Opus anterior en el auditor: tampoco), `21c` (Opus 5.5 en los dos: arranca,
y un subagente heredaria Opus 5.5).

**LO QUE NO SE TOCA, y se dice:** Claude Code usa un modelo pequenio para tareas internas suyas
(por ejemplo, poner titulo a una sesion). No ejecuta ni audita nada, y en los turnos medidos de
la serial no aparecio. **Si el fundador quiere cerrarlo tambien**, es una variable mas
(`ANTHROPIC_DEFAULT_HAIKU_MODEL`), con su coste.
