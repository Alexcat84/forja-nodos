# PARA ALEXIS: **CAMPAÑA CONSUMADA. EL FRENTE `marquet_turn_the_ship` CIERRA SU EXTRACCION Y PIDE LA COSECHA**

Rama `extraccion-marquet_turn_the_ship`, worktree `C:/Users/AlexDesk/Documents/forja-marquet_turn_the_ship`.
Escrito por el auditor al cerrar la **`ACTA M9`** (`docs/loop/ACTA_AUDITOR.md`, al final), que audita la vuelta `8` del frente.

## MOTIVO

**La parada feliz de `AUDITOR_FORJA.md` `3`: campaña consumada.** El libro esta minado entero y la bandeja esta barrida
contra su texto final. **El bucle no cosecha, no funde y no crea remotos** (`3`, `D.50`), asi que **PIDO la cosecha; no la hago.**
Por el mandato del `22` sep punto `2.d` (`docs/loop/paradas/2026-09-22-tu-lanzas-MANDATO.md`), **la cosecha de Marquet la hace la
sesion** (una fusion, gate y suite, TABLERO), **y la serial lo inserta como septimo libro al acabar Gerber** (decision del `22` sep
punto `4`, `docs/loop/paradas/2026-09-22-dos-semanas-DECISION.md`).

## ESTADO EXACTO, MEDIDO EN ESTE TURNO

| | valor | de donde |
|---|---|---|
| rama | `extraccion-marquet_turn_the_ship` | `git rev-parse --abbrev-ref HEAD` |
| ultimo commit del extractor auditado | `75d2243` | `git log` |
| nodos en el grafo | `346` | `python forja.py gate`: `GATE VERDE.` / `nodos verificados: 346` |
| guiones | `BARRIDO DE GUIONES VERDE` | `python forja.py guiones` |
| resolutor | `nodos vivos: 346`, `0` deprecados, `0` alias | `python forja.py resolutor` |
| suite | `total: 376 pruebas, 0 fallos, 0 errores` | `python tests/test_aceptacion.py` |
| cierre | `CIERRE VERDE: las cuatro guardas que muerden, el tallado y el censo.` | `python scripts/cerrar_reporte.py` |
| bitacora / pares mutuos | `740` / `1` lineas | `wc -l` |
| candidatos en bandeja | **`20`** | `ls cuarentena/marquet_turn_the_ship/*.json \| wc -l` |
| capitulos minados | **`17` de `17`**, `13` con candidato y `4` en cero con su firma | `ACTA M7` `M7.5`, `ACTA M8` `M8.4` |
| pasos | `110`, con `0` PUENTE vivo | `ACTA M8` `M8.4` |
| barrido de la bandeja contra el texto final (`d104`) | **`20` de `20`**: `4` `ENTRARIA`, `16` `BLOQUEARIA`, `0` `CAERIA`, `0` choques | `ACTA M9` `M9.3` |
| pares en banda alta | `10`, leidos por sus pasos, **ninguno `REPITE`** | `ACTA M9` `M9.4` |
| credito de la linea | `REPORTE 1 de 3`; `CIFRA PUBLICADA`, `CLASE`, `DATO MOVIDO` y `AUDITOR` en `0`; `CREDITO ENTERO` | `python forja.py credito` |
| tablero | `PENDIENTES DE RELEVO (D.50)`: `lote 5   marquet_turn_the_ship   20 candidato(s) en extraccion-marquet_turn_the_ship` | `python forja.py tablero` |

## LO QUE SE NECESITA

1. **La cosecha** de `extraccion-marquet_turn_the_ship` (mandato `2.d`): la fusion, con `gate` y suite delante, y el TABLERO al dia.
2. **La insercion como septimo libro**, en la serial y en regimen completo, cuando acabe Gerber. **Cada candidato con su lectura de
   fidelidad ENTERA en su vuelta de insercion** (`D.58`), porque aqui solo se coteja muestra.
3. **Lo que la vuelta de insercion deberia tener delante** (no bloquea la cosecha):
   - **los `16` `BLOQUEARIA` son vecindades, no gemelos**: los diez pares de banda alta estan leidos (`M9.4`), y el par que yo miraria
     para una arista es `observar_reunion_rutinaria_senales_plantilla` con `recorrer_organizacion_escuchar_plantilla` (`0.414` / `0.420`).
   - **las deudas de la linea que siguen abiertas** (`docs/loop/DEUDA.jsonl`): `d094`, `d095`, `d096` (maquinaria de `forja.py herencia`
     e `informe`), `d097` (papeles de `.vm01/` de la vuelta `1`) y `d107` (`scripts/tallar_reporte.py` y `TALLADO: parcial`). **Ninguna
     es guarda de dato en rojo.** Las de maquinaria son de la serial o del fundador (`D.45`).

## COMO RETOMAR

**Esta linea no tiene vuelta siguiente: `docs/loop/PROMPT_SIGUIENTE.md` queda VACIO a proposito.** No se relanza el orquestador en
este worktree. Lo siguiente es la cosecha, desde la sesion, sobre la rama de arriba.
