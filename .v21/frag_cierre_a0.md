
---

# O.6. EL CIERRE DE LA VUELTA 21

*`EXTRACTOR.md` 4: **el estado al cierre se mide al cierre.** Toda cifra que describa el estado al
cerrar se RECOMPUTA si algo de la propia vuelta pudo haberla movido. Todo lo de abajo se corrio
DESPUES de escribir los trece candidatos y DESPUES de la correccion de las 22 cuentas.*

## O.6.1. LAS GUARDAS, CORRIDAS AL CIERRE

    $ python forja.py gate
      GATE VERDE.
        nodos verificados: 203
        guardas: esquema, reglas_id, fuentes, orden_fuentes, auto_arista, arista_duplicada,
                 vuelta, cita_incompleta, deprecado_en_superficie, arista_rota,
                 arista_incompleta, guiones

    $ python forja.py guiones
      BARRIDO DE GUIONES VERDE: cero guiones largos y cero guiones medios.

    $ python tests/test_aceptacion.py | tail -3
      D.40, lo que un auditor le deja al siguiente lo entrega el arnes: 13 pruebas mas
      la poblacion del informe es grafo mas bandejas (12 sep 2026, punto 3): 6 pruebas mas
      total: 98 pruebas, 0 fallos, 0 errores

    $ python forja.py resolutor | tail -2
      nodos deprecados (archivo): 0
      alias registrados: 0

    $ python forja.py rancios | tail -3
      veredictos comprobados: 148
      citas de enlace mutuo comprobadas: 0
      todos siguen emitidos contra el texto que leyeron

> ### **LAS CINCO EN VERDE, Y LA PRUEBA DE ACEPTACION TRAE **98** PRUEBAS Y NO 90: OCHO MAS QUE AL CERRAR LA VUELTA 20, LAS DE `D.40` Y LAS DE LA POBLACION NUEVA.** No las escribi yo (moratoria de maquinaria, `EXTRACTOR.md` 13): **son las que nacieron con las cuatro decisiones del 12 sep**, y las cito porque el numero cambio debajo de mi.

### O.6.1.b. **Y EL HOOK ME ABORTO UN COMMIT, CON MI NOMBRE: DOS GUIONES MIOS EN MI PROPIO GUION**

*`EXTRACTOR.md` 6: **deja correr el hook. Si falla, corriges y reintentas; jamas lo saltas.** Fallo,
corregi y reintente, y lo cuento entero porque una caida que no se cuenta no existe.*

    [pre-commit] barrido de guiones
    BARRIDO DE GUIONES EN ROJO: 2 hallazgo(s)
      .t1_v21/frontera21.py linea 28 columna 29: guion largo (U+2014)
      .t1_v21/frontera21.py linea 28 columna 48: guion medio (U+2013)
    [pre-commit] COMMIT ABORTADO: hay guiones largos o medios en el repo.

**LA CAUSA ES DE LIBRO Y ES MIA:** mi guion de frontera normaliza las comillas y los guiones del
original **y para hacerlo tenia los dos guiones escritos como literales**. La guarda barre TODO el
repo, incluido el codigo que la ayuda.

**LA CORRECCION, y es lo contrario de un apanio:** los dos literales pasan a escribirse **por su
punto de codigo** (`chr(0x2014)` y `chr(0x2013)`), con el motivo en un comentario de tres lineas
para que el proximo que escriba un normalizador no pague lo mismo.

    $ python forja.py guiones
      BARRIDO DE GUIONES VERDE: cero guiones largos y cero guiones medios.
    $ python .t1_v21/frontera21.py | head -1
      (sigue imprimiendo la misma tabla, con la comprobacion en True)

**Y `D.33` NO ME CUBRE AQUI, Y LO DIGO ANTES DE QUE NADIE LO PIENSE:** el patron nuevo exime
`docs/loop/ultimo_*.json` y `loop.log`, que son **volcados del arnes**. `.t1_v21/frontera21.py` es
**codigo que escribo yo**, y la parada del 12 sep dice con todas las letras que la exencion es **de
CAPA y no de contenido**.
