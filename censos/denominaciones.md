# Censo de denominaciones

Manual seccion 3.1 y seccion 5: nombre largo, sigla y termino en otro idioma son TRES denominaciones aparte y cada una se registra. El alias cubre el id, no la busqueda del lector.

Lo escribe la aduana al insertar (src/aduana.py). No se edita a mano salvo para corregir, y una correccion no borra: declara (manual principio 6).

| fecha | nodo | clase | denominacion | idioma | nota |
|---|---|---|---|---|---|
| 2026-08-12 | registrar_fuente_canonica | nombre_largo | Registro de la fuente canonica de un libro | castellano | - |
| 2026-08-12 | registrar_fuente_canonica | sigla | RFC | castellano | - |
| 2026-08-12 | registrar_fuente_canonica | otro_idioma | canonical source registration | ingles | - |
| 2026-08-12 | elegir_grafia_clave | nombre_largo | Eleccion de la grafia unica de una clave de fuente | castellano | - |
