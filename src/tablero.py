# -*- coding: utf-8 -*-
"""EL TABLERO DE FRENTES: SEDE UNICA DEL ESTADO DE LA CAMPANIA (D.49, D.50).

    python forja.py tablero                 lo imprime, medido en este instante
    python forja.py tablero --escribir      lo vuelca a docs/loop/TABLERO.jsonl
    python forja.py tablero --puedo <clave> si esta linea puede abrir ese libro
    python forja.py tablero --dueno <clave> quien lo trabaja hoy

POR QUE EXISTE. El 17 sep 2026 la linea serial iba a cerrar el lote 4, y `D.32` dice
que **el acta que cierra un lote abre el siguiente sin parada entre medias**. El
siguiente por orden era el lote `5`, `marquet_turn_the_ship`, **que estaba siendo
extraido en otra rama con `9` candidatos dentro**. Lo unico que lo impedia era una
frase escrita a mano en el encargo, y esta casa tiene medido lo que vale eso: `D.35`,
**un remedio que se cumple acordandose no es un remedio.**

SE GENERA DEL DATO, NO SE TECLEA. Cada fila sale de:

    el orden y las claves   docs/loop/ORDEN_DE_LOTES.md, su tabla
    la rama                 git branch, `extraccion-<clave>`
    el worktree             git worktree list
    los capitulos minados   los candidatos de su bandeja, por lo que CITAN
    el commit que los mino  el ultimo commit propio de esa rama que nombra ese capitulo
    los candidatos          `cuarentena/<clave>/` EN EL ARBOL DE SU DUEÑO
    los insertados          `cuarentena/_insertados/<clave>/`
    los nodos en el grafo   `dataset/nodos.jsonl`, por su fuente
    las unidades del libro  `fuentes/<clave>/`

LO QUE EL DATO NO PUEDE DECIR VIVE EN `config/frentes.json`, CON SU CITA: cual es el
frente activo (un frente detenido esperando decision **sigue teniendo su libro**) y que
libro esta `CERRADO EN EXTRACCION` (que es la adjudicacion de un acta, no una cuenta de
ficheros). **Cada fila dice de donde sale su estado**, medido o declarado.

POR QUE EL ARBOL DEL DUEÑO Y NO ESTE. Los cuatro worktrees comparten el historial, asi
que **el arbol de cada frente tiene las bandejas de los otros libros copiadas**. Contar
`cuarentena/marquet_turn_the_ship/` aqui da `3`, y en su frente da `9`. **La cifra buena
es la del arbol de quien lo trabaja**, y por eso esta funcion va a buscarla alli.
"""

import json
import os
import re
import subprocess
import sys

from . import comun

RUTA_TABLERO = os.path.join(comun.RAIZ, "docs", "loop", "TABLERO.jsonl")
RUTA_ORDEN = os.path.join(comun.RAIZ, "docs", "loop", "ORDEN_DE_LOTES.md")
RUTA_FRENTES = os.path.join(comun.RAIZ, "config", "frentes.json")

RAMA_DE_INSERCION = os.environ.get("RAMA_DE_INSERCION", "extraccion-mundo-11")
LINEA_SERIAL = "serial"
NINGUNO = "NINGUNO"

FILA_DE_LOTE = re.compile(r"^\|\s*\*{0,2}(\d+)\*{0,2}\s*\|\s*`([a-z0-9_]+)`\s*\|")
CAPITULO = re.compile(r"cap_(\d+)")

# LOS SEIS ESTADOS de la decision del fundador del 17 sep 2026, punto 1.
ESTADOS = ("SIN EMPEZAR", "EN CURSO", "PAUSADO", "CERRADO EN EXTRACCION",
           "COSECHADO", "INSERTADO")


class TableroMalDeclarado(Exception):
    """Una declaracion de `config/frentes.json` sin cita. Nunca se usa a ciegas."""


def _git(*argumentos):
    try:
        salida = subprocess.check_output(("git",) + argumentos, cwd=comun.RAIZ,
                                         stderr=subprocess.STDOUT)
    except (subprocess.CalledProcessError, OSError):
        return ""
    return salida.decode("utf-8", "replace").strip()


def declaraciones():
    """Lo que `config/frentes.json` declara, comprobando que todo lleve cita."""
    datos = comun.leer_json(RUTA_FRENTES)
    for nombre in ("alcance", "frente_activo"):
        if not (datos.get(nombre) or {}).get("cita"):
            raise TableroMalDeclarado(
                "config/frentes.json: '%s' sin cita. Una declaracion sin cita no se "
                "puede releer." % nombre)
    for grupo in ("liberados", "cerrados_en_extraccion"):
        for clave, dato in (datos.get(grupo) or {}).items():
            if not (dato or {}).get("cita"):
                raise TableroMalDeclarado(
                    "config/frentes.json: '%s' de '%s' sin cita." % (clave, grupo))
    return datos


def lotes():
    """`[(numero, clave)]` en el orden de `ORDEN_DE_LOTES.md`, que es la sede del orden."""
    encontrados = []
    for linea in comun.leer_texto(RUTA_ORDEN).split("\n"):
        encaje = FILA_DE_LOTE.match(linea.strip())
        if encaje:
            encontrados.append((int(encaje.group(1)), encaje.group(2)))
    return encontrados


def worktrees():
    """`{rama: ruta}` de `git worktree list`."""
    mapa = {}
    for linea in _git("worktree", "list").split("\n"):
        encaje = re.match(r"^(\S+)\s+\S+\s+\[([^\]]+)\]", linea.strip())
        if encaje:
            mapa[encaje.group(2)] = encaje.group(1)
    return mapa


def ramas():
    return set(l.strip() for l in _git("branch", "--format=%(refname:short)").split("\n")
               if l.strip())


def _contar_json(carpeta):
    if not os.path.isdir(carpeta):
        return 0
    return len([f for f in os.listdir(carpeta) if f.endswith(".json")])


def _capitulos_de_bandeja(carpeta):
    """LOS CAPITULOS MINADOS SALEN DE LO QUE SUS CANDIDATOS CITAN, no de un rotulo.

    Un capitulo minado no deja marca en el repo (lo dice `ORDEN_DE_LOTES.md` desde la
    vuelta 16). Lo que si deja marca es **el candidato que salio de el**.
    """
    vistos = set()
    if not os.path.isdir(carpeta):
        return []
    for nombre in sorted(os.listdir(carpeta)):
        if not nombre.endswith(".json"):
            continue
        try:
            crudo = comun.leer_texto(os.path.join(carpeta, nombre))
        except (IOError, OSError):
            continue
        for encaje in CAPITULO.finditer(crudo):
            vistos.add("cap_%s" % encaje.group(1))
    return sorted(vistos)


def _commit_del_capitulo(rama, clave, capitulo):
    """El ultimo commit PROPIO de esa rama que nombra ese capitulo.

    `--not <rama de insercion>` es la mitad que importa: sin eso, la rama de un frente
    devuelve commits de la serial, **porque el frente nacio de ella y se llevo su
    historia entera.** Es la misma confusion que `D.48` cerro en el credito.
    """
    if not rama:
        return ""
    if rama == RAMA_DE_INSERCION:
        registro = _git("log", rama, "--pretty=format:%h %s", "-n", "400")
    else:
        registro = _git("log", rama, "--not", RAMA_DE_INSERCION,
                        "--pretty=format:%h %s")
    for linea in registro.split("\n"):
        if capitulo in linea and clave in linea:
            return linea.split(" ", 1)[0]
    for linea in registro.split("\n"):
        if capitulo in linea:
            return linea.split(" ", 1)[0]
    return ""


def _nodos_en_grafo(clave, nodos):
    cuenta = 0
    for nodo in nodos:
        for fuente in nodo.get("fuentes") or []:
            if (fuente or {}).get("clave") == clave:
                cuenta += 1
                break
    return cuenta


def medir():
    """UNA FILA POR LIBRO, con la verdad de este instante."""
    declarado = declaraciones()
    activo = (declarado.get("frente_activo") or {}).get("clave")
    liberados = declarado.get("liberados") or {}
    cerrados = declarado.get("cerrados_en_extraccion") or {}
    mapa_worktrees = worktrees()
    existentes = ramas()
    nodos = comun.leer_jsonl(comun.RUTA_DATASET)

    filas = []
    for numero, clave in lotes():
        rama = "extraccion-%s" % clave
        rama = rama if rama in existentes else None
        worktree = mapa_worktrees.get(rama) if rama else None
        propios = (_git("log", rama, "--not", RAMA_DE_INSERCION, "--pretty=format:%h")
                   .split("\n") if rama else [])
        propios = [c for c in propios if c.strip()]

        # LA BANDEJA SE CUENTA EN EL ARBOL DE SU DUEÑO, no en este.
        arbol = worktree if (worktree and propios) else comun.RAIZ
        bandeja = os.path.join(arbol, "cuarentena", clave)
        candidatos = _contar_json(bandeja)
        archivo = os.path.join(comun.RAIZ, "cuarentena", "_insertados", clave)
        # UN CAPITULO MINADO SIGUE MINADO DESPUES DE INSERTARSE. Contar solo la
        # bandeja daria "ningun capitulo" para los tres lotes ya insertados, y para
        # el lote 4 daria los pendientes en vez de los minados. El relevo de D.50
        # necesita saber por donde va el LIBRO, no por donde va la bandeja.
        capitulos = sorted(set(_capitulos_de_bandeja(bandeja))
                           | set(_capitulos_de_bandeja(archivo)))
        ultimo = capitulos[-1] if capitulos else ""

        insertados = _contar_json(archivo)
        en_grafo = _nodos_en_grafo(clave, nodos)
        unidades = _contar_json_md(os.path.join(comun.RAIZ, "fuentes", clave))

        # ------------------------------------------------- el estado y su dueño
        de = "medido"
        if rama and propios and clave not in liberados:
            estado = "EN CURSO" if clave == activo else "PAUSADO"
            dueno = clave if clave == activo else NINGUNO
            de = "declarado: %s" % (declarado["frente_activo"]["cita"])
        elif rama and propios and clave in liberados:
            estado, dueno = "PAUSADO", NINGUNO
            de = "declarado: %s" % liberados[clave]["cita"]
        elif candidatos == 0 and en_grafo > 0:
            estado, dueno = "INSERTADO", NINGUNO
        elif clave in cerrados:
            estado, dueno = "CERRADO EN EXTRACCION", LINEA_SERIAL
            de = "declarado: %s" % cerrados[clave]["cita"]
        elif candidatos > 0 or en_grafo > 0:
            estado, dueno = "EN CURSO", LINEA_SERIAL
        else:
            estado, dueno = "SIN EMPEZAR", NINGUNO

        filas.append({
            "lote": numero,
            "clave": clave,
            "rama": rama or "",
            "worktree": (worktree or "").replace("\\", "/"),
            "estado": estado,
            "dueno": dueno,
            "estado_de": de,
            "capitulos_minados": capitulos,
            "ultimo_capitulo": ultimo,
            "commit": _commit_del_capitulo(rama or RAMA_DE_INSERCION, clave, ultimo)
                      if ultimo else "",
            "candidatos_en_bandeja": candidatos,
            "bandeja_medida_en": comun.relativa(bandeja) if arbol == comun.RAIZ
                                 else bandeja.replace("\\", "/"),
            "insertados": insertados,
            "nodos_en_grafo": en_grafo,
            "unidades_del_libro": unidades,
            "commits_propios_de_su_rama": len(propios),
        })
    return filas


def _contar_json_md(carpeta):
    if not os.path.isdir(carpeta):
        return 0
    return len([f for f in os.listdir(carpeta) if f.endswith(".md")])


def leer():
    """El tablero escrito, tal cual esta en el arbol."""
    if not os.path.exists(RUTA_TABLERO):
        return []
    return comun.leer_jsonl(RUTA_TABLERO)


def escribir(filas=None):
    filas = filas if filas is not None else medir()
    comun.escribir_jsonl(RUTA_TABLERO, filas)
    return filas


def fila_de(clave, filas=None):
    for fila in (filas if filas is not None else leer()):
        if fila.get("clave") == clave:
            return fila
    return None


def puede_abrir(clave, linea, filas=None):
    """`D.49`: UN LIBRO, UN DUEÑO A LA VEZ.

    Devuelve `(True, motivo)` o `(False, motivo)`. La regla, literal:

        ninguna linea abre ni continua un libro cuyo ESTADO no sea SIN EMPEZAR con
        dueño NINGUNO, o PAUSADO con dueño NINGUNO y ya COSECHADO.
    """
    fila = fila_de(clave, filas)
    if fila is None:
        return False, ("'%s' no tiene fila en el tablero. Un libro sin fila no se "
                       "abre: primero se mide (forja.py tablero --escribir)." % clave)
    estado, dueno = fila.get("estado"), fila.get("dueno")

    if dueno and dueno != NINGUNO:
        if dueno == linea:
            return True, ("'%s' ya es de esta linea ('%s'): continuarlo es lo que "
                          "toca." % (clave, linea))
        return False, ("'%s' TIENE DUEÑO Y NO ERES TU: lo trabaja la linea '%s' "
                       "(estado %s, rama %s). D.49: un libro, un dueño a la vez."
                       % (clave, dueno, estado, fila.get("rama") or "la serial"))

    if estado == "SIN EMPEZAR":
        return True, "'%s' esta SIN EMPEZAR y sin dueño." % clave
    if estado == "COSECHADO":
        return True, ("'%s' esta COSECHADO y sin dueño: su trabajo ya llego a esta "
                      "rama, asi que se continua desde el capitulo siguiente al "
                      "ultimo minado (%s), citando su frontera. D.50."
                      % (clave, fila.get("ultimo_capitulo") or "ninguno"))
    if estado == "PAUSADO":
        return False, ("'%s' esta PAUSADO y NO COSECHADO: tiene %d candidato(s) en "
                       "%s que todavia no han llegado a esta rama. D.50 manda "
                       "RELEVARLO ENTERO antes de tocarlo, y el relevo empieza por "
                       "cosechar su rama (%s)."
                       % (clave, fila.get("candidatos_en_bandeja", 0),
                          fila.get("bandeja_medida_en") or "su frente",
                          fila.get("rama") or "?"))
    return False, ("'%s' esta en estado %s: no es ni SIN EMPEZAR ni COSECHADO, asi "
                   "que no se abre." % (clave, estado))


def siguiente_libre(linea, filas=None):
    """El primer libro del orden que esta linea SI puede tomar, con su motivo."""
    for fila in sorted(filas if filas is not None else leer(),
                       key=lambda f: f.get("lote", 999)):
        vale, motivo = puede_abrir(fila["clave"], linea, filas)
        if vale and fila.get("estado") in ("SIN EMPEZAR", "COSECHADO"):
            return fila["clave"], motivo
    return None, "ningun libro del orden esta libre para la linea '%s'." % linea


def relevables(filas=None):
    """Los libros que `D.50` manda relevar: `EN CURSO` o `PAUSADO` en otra rama."""
    pendientes = []
    for fila in sorted(filas if filas is not None else leer(),
                       key=lambda f: f.get("lote", 999)):
        if fila.get("estado") in ("EN CURSO", "PAUSADO") and fila.get("rama"):
            pendientes.append(fila)
    return pendientes


# --------------------------------------------------------------------- la voz

def texto(filas=None):
    filas = filas if filas is not None else medir()
    partes = ["TABLERO DE FRENTES (D.49, D.50): sede unica del estado de la campania",
              "  registro: %s" % comun.relativa(RUTA_TABLERO), ""]
    partes.append("  %-4s %-30s %-22s %-22s %5s %5s %7s"
                  % ("lote", "clave", "estado", "dueno", "band", "graf", "ult cap"))
    partes.append("  " + "-" * 104)
    for fila in filas:
        partes.append("  %-4s %-30s %-22s %-22s %5d %5d %7s"
                      % (fila["lote"], fila["clave"], fila["estado"], fila["dueno"],
                         fila["candidatos_en_bandeja"], fila["nodos_en_grafo"],
                         fila["ultimo_capitulo"] or "."))
    partes.append("")
    con_dueno = [f for f in filas if f["dueno"] != NINGUNO]
    partes.append("  libros CON DUEÑO ahora mismo: %d" % len(con_dueno))
    for fila in con_dueno:
        partes.append("    %-30s lo trabaja '%s' (%s)"
                      % (fila["clave"], fila["dueno"], fila["estado"]))
    pendientes = relevables(filas)
    if pendientes:
        partes.append("")
        partes.append("  PENDIENTES DE RELEVO (D.50), en orden de lote:")
        for fila in pendientes:
            partes.append("    lote %-3s %-30s %2d candidato(s) en %s"
                          % (fila["lote"], fila["clave"],
                             fila["candidatos_en_bandeja"], fila["rama"]))
    return "\n".join(partes)


def main(argumentos):
    comun.salida_utf8()
    resto = list(argumentos)
    try:
        if "--puedo" in resto:
            clave = resto[resto.index("--puedo") + 1]
            from . import credito
            linea = credito.linea_actual()
            vale, motivo = puede_abrir(clave, linea)
            print("LINEA '%s', LIBRO '%s': %s" % (linea, clave, "SI" if vale else "NO"))
            print("  " + motivo)
            return 0 if vale else 1
        if "--dueno" in resto:
            clave = resto[resto.index("--dueno") + 1]
            fila = fila_de(clave)
            if fila is None:
                print("'%s' no tiene fila en el tablero." % clave)
                return 1
            print("%s: estado %s, dueno %s (%s)"
                  % (clave, fila["estado"], fila["dueno"], fila["estado_de"]))
            return 0
        if "--escribir" in resto:
            filas = escribir()
            print(texto(filas))
            print("")
            print("ESCRITO: %d fila(s) en %s"
                  % (len(filas), comun.relativa(RUTA_TABLERO)))
            return 0
        print(texto())
        return 0
    except TableroMalDeclarado as roto:
        print("TABLERO MAL DECLARADO: %s" % roto)
        return 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
