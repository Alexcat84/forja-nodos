# -*- coding: utf-8 -*-
"""LA GUARDA DEL TABLERO: EL ARNES COMPRUEBA AL ABRIR VUELTA (D.49).

    python scripts/guarda_tablero.py            mide, comprueba, y devuelve 0 o 1

QUE HACE, EN TRES PASOS.

  1. **VUELVE A MEDIR EL TABLERO** y lo escribe (`docs/loop/TABLERO.jsonl`). Un tablero
     que se actualiza cuando alguien se acuerda es la frase escrita a mano que `D.49`
     vino a sustituir.
  2. **LEE QUE LIBRO DECLARA EL ENCARGO DE ESTA VUELTA**, en `PROMPT_SIGUIENTE.md`:

         LIBRO DE ESTA VUELTA: scott_radical_candor

  3. **LO PASA POR `D.49`** con la linea de este arbol. Si el libro tiene dueño y no es
     esta linea, **se detiene nombrando al dueño.**

POR QUE EL ENCARGO TIENE QUE DECLARARLO, Y NO SE ADIVINA. El arnes no sabe que es un
libro (`D.45`), y buscar la clave suelta dentro del texto del encargo **es exactamente la
trampa que el tallado ya pago dos veces**: un encargo nombra a los tres frentes en su
seccion de *lo que no se toca*, y una guarda que lee menciones **tumbaria la vuelta por
decir que no los toca.** Asi que no se busca: **se exige declarado, en su propia linea.**

**Y SI NO LO DECLARA, EL ARNES SE DETIENE IGUAL.** Un encargo que no dice sobre que libro
trabaja no es un encargo que la guarda pueda mirar, y `D.49` dice que **toda linea lee el
tablero en su apertura y lo cita.** Para declarar que una vuelta no toca ningun libro
existe `NINGUNO`, y eso es una declaracion, no un silencio.
"""

import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, RAIZ)

from src import comun, credito, tablero  # noqa: E402

RUTA_ENCARGO = os.path.join(RAIZ, "docs", "loop", "PROMPT_SIGUIENTE.md")

# La declaracion, con la decoracion que esta casa escribe: negrita, cita, comillas.
DECLARACION = re.compile(
    r"^[\s>*#`]*LIBRO\s+DE\s+ESTA\s+VUELTA\s*:?[\s*`]*([A-Za-z0-9_]+)", re.M | re.I)

SIN_LIBRO = "NINGUNO"


def libro_declarado(texto=None):
    """La clave que el encargo declara, o `None` si no declara ninguna."""
    if texto is None:
        texto = comun.leer_texto(RUTA_ENCARGO) if os.path.exists(RUTA_ENCARGO) else ""
    encaje = DECLARACION.search(texto or "")
    return encaje.group(1) if encaje else None


def comprobar(texto=None, linea=None, filas=None):
    """Devuelve la lista de motivos que IMPIDEN abrir la vuelta. Vacia es verde."""
    linea = linea or credito.linea_actual()
    clave = libro_declarado(texto)

    if clave is None:
        return ["el encargo de esta vuelta NO DECLARA su libro. D.49: toda linea lee el "
                "tablero en su apertura y lo cita. Escribe en %s una linea "
                "'LIBRO DE ESTA VUELTA: <clave>', o 'LIBRO DE ESTA VUELTA: NINGUNO' si "
                "la vuelta no toca ningun libro." % comun.relativa(RUTA_ENCARGO)]

    if clave.upper() == SIN_LIBRO:
        return []

    vale, motivo = tablero.puede_abrir(clave, linea, filas)
    if vale:
        return []
    return ["el encargo declara el libro '%s' y esta linea ('%s') NO puede tomarlo. %s"
            % (clave, linea, motivo)]


def main(argumentos=()):
    comun.salida_utf8()
    linea = credito.linea_actual()
    try:
        filas = tablero.escribir()
    except tablero.TableroMalDeclarado as roto:
        print("GUARDA DEL TABLERO EN ROJO: %s" % roto)
        return 1

    clave = libro_declarado()
    print("GUARDA DEL TABLERO (D.49)")
    print("  linea de este arbol : %s" % linea)
    print("  libro que declara el encargo : %s" % (clave or "(NINGUNO DECLARADO)"))
    con_dueno = [f for f in filas if f["dueno"] != tablero.NINGUNO]
    for fila in con_dueno:
        print("  con dueño: %-30s %-22s lo trabaja '%s'"
              % (fila["clave"], fila["estado"], fila["dueno"]))

    impiden = comprobar(linea=linea, filas=filas)
    if not impiden:
        print("")
        print("TABLERO VERDE: la vuelta puede abrir.")
        return 0
    print("")
    print("TABLERO EN ROJO. La vuelta NO abre:")
    for motivo in impiden:
        print("  %s" % motivo)
    return 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
