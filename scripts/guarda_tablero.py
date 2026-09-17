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
  4. **Y LO PASA POR `D.51`:** el libro declarado tiene que ser **el que el orden del
     mundo 11 le toca a esta linea**, no otro. Si no lo es, se detiene **nombrando el
     que si**.

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

    impiden = []

    vale, motivo = tablero.puede_abrir(clave, linea, filas)
    if not vale:
        impiden.append(
            "D.49: el encargo declara el libro '%s' y esta linea ('%s') NO puede "
            "tomarlo. %s" % (clave, linea, motivo))

    # D.51: NINGUNA LINEA ELIGE LIBRO. Se comprueba aunque D.49 ya haya caido, porque
    # las dos cosas que el encargo puede tener mal son distintas: D.49 dice que ese
    # libro no es tuyo, y D.51 dice cual es.
    toca, porque, relevo = tablero.siguiente_por_prioridad(linea, filas)
    if toca is None:
        impiden.append("D.51: a esta linea no le toca NINGUN libro ahora mismo. %s"
                       % porque)
    elif toca != clave:
        aviso = ("D.51: el encargo declara '%s' y el orden del mundo 11 le da a esta "
                 "linea '%s'. %s" % (clave, toca, porque))
        if relevo is not None:
            aviso += (" El relevo pendiente es la rama '%s'." % relevo.get("rama"))
        impiden.append(aviso)
    return impiden


def main(argumentos=()):
    comun.salida_utf8()
    linea = credito.linea_actual()

    # SIN OBJETO, Y SE DICE EN VOZ ALTA. Un arbol sin `ORDEN_DE_LOTES.md` no tiene
    # campania que coordinar: no hay libros, no hay lineas y no hay nada que D.49 o
    # D.51 puedan decidir. **Una guarda que no puede medir no inventa un veredicto**,
    # igual que el tallado dice TALLADO SIN OBJETO cuando no hay documento.
    #
    # Y NO ES UN AGUJERO: el banco de pruebas del arnes corre asi a proposito, y hay
    # una prueba que exige que el repo de verdad SI tenga su tablero con una fila por
    # lote. Que esto pase en silencio ahi seria el agujero.
    if not os.path.exists(tablero.RUTA_ORDEN):
        print("GUARDA DEL TABLERO SIN OBJETO: no hay %s en este arbol, asi que no hay "
              "campania que coordinar (D.49, D.51)."
              % comun.relativa(tablero.RUTA_ORDEN))
        return 0

    try:
        filas = tablero.escribir()
    except tablero.TableroMalDeclarado as roto:
        print("GUARDA DEL TABLERO EN ROJO: %s" % roto)
        return 1

    clave = libro_declarado()
    print("GUARDA DEL TABLERO (D.49)")
    print("  linea de este arbol : %s" % linea)
    print("  libro que declara el encargo : %s" % (clave or "(NINGUNO DECLARADO)"))
    toca, porque, _ = tablero.siguiente_por_prioridad(linea, filas)
    print("  libro que el orden le da (D.51): %s" % (toca or "NINGUNO"))
    print("    %s" % porque[:150])
    con_dueno = [f for f in tablero.libros(filas)
                 if f["dueno"] != tablero.NINGUNO]
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
