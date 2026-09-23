## 9. LO QUE ESTA PAGINA NO HACE, Y LO QUE DEJA PARA EL TURNO NORMAL

- **No compara con el extractor.** Su reporte, sus fichas corregidas de la `64` y su carpeta `.v64ext/`
  quedan sin abrir hasta que el arnes selle esta pagina.
- **No escribe veredictos en `bitacora/` ni aristas en el dataset**: son clases leidas, no insertadas.
- **Lo que queda para el turno normal:** `R5` sobre el reporte de la `64`; la fidelidad de las cinco
  fichas corregidas **contra mi tabla de `067c9df`**, para ver si lo que el extractor reescribio es el
  paso `1` de `emparejar` y que hizo con mis dos dudas; y cada par de `6` y `7` contra sus veredictos
  listos.
- **Mi evidencia se queda en `.v64aud/`**: `antes_<id>.json`, `fidelidad.tsv`, `contar_fidelidad.py` y
  su salida, `pasos.py`, `pares_d140.py`, `vecinos_hoy.py` con su salida, los seis `informe_<id>.txt` y
  `barrido.log`.

## 10. LAS GUARDAS AL CERRAR ESTA PAGINA

    $ python forja.py gate 2>&1 | tail -3
    GATE VERDE.
      nodos verificados: 346
      guardas: esquema, reglas_id, fuentes, orden_fuentes, auto_arista, arista_duplicada, vuelta, cita_incompleta, deprecado_en_superficie, arista_rota, arista_incompleta, guiones, censo_no_decrece

    $ python forja.py guiones docs/loop/APERTURA_CIEGA.md .v64aud/
    BARRIDO DE GUIONES VERDE: cero guiones largos y cero guiones medios.

**Gate y guiones en VERDE al cerrar la pagina. Ningun proceso mio queda vivo**: el barrido de la seccion `5` termino a las `11:15:56` con los seis `rc=0`, y lo recogi dentro del turno. **No commiteo**: sella y commitea el arnes.
