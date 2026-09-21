# -*- coding: utf-8 -*-
"""EL TABLERO DE FRENTES: SEDE UNICA DEL ESTADO DE LA CAMPANIA (D.49, D.50).

    python forja.py tablero                 lo imprime, medido en este instante
    python forja.py tablero --escribir      lo vuelca a docs/loop/TABLERO.jsonl
    python forja.py tablero --puedo <clave> si esta linea puede abrir ese libro
    python forja.py tablero --dueno <clave> quien lo trabaja hoy
    python forja.py tablero --siguiente     que libro le toca a ESTA linea (D.51)

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
# EL CAPITULO DE UN CANDIDATO ES EL QUE SU FICHA DECLARA, no el que menciona.
UNIDAD_DE_ORIGEN = re.compile(
    r"UNIDAD DE ORIGEN:\s*fuentes/[a-z0-9_]+/(cap_\d+)\.md", re.I)

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
    for nombre in ("alcance", "frente_activo", "corte_definitivo"):
        if not (datos.get(nombre) or {}).get("cita"):
            raise TableroMalDeclarado(
                "config/frentes.json: '%s' sin cita. Una declaracion sin cita no se "
                "puede releer." % nombre)
    if not (datos.get("orden_de_prioridad") or {}).get("cita"):
        raise TableroMalDeclarado(
            "config/frentes.json: 'orden_de_prioridad' sin cita. El orden lo da el "
            "tablero (D.51), y un orden sin cita no se puede releer.")
    for grupo in ("liberados", "cerrados_en_extraccion", "minados_en_cero",
                  "coste_por_turno"):
        for clave, dato in (datos.get(grupo) or {}).items():
            # Las claves con guion bajo son la nota de lectura del grupo, no una
            # declaracion, y esta casa ya las usa asi en la raiz del fichero.
            if clave.startswith("_"):
                continue
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
    """LOS CAPITULOS MINADOS SALEN DE LO QUE SUS CANDIDATOS DECLARAN COMO ORIGEN.

    Un capitulo minado no deja marca en el repo (lo dice `ORDEN_DE_LOTES.md` desde la
    vuelta 16). Lo que si deja marca es **el candidato que salio de el**.

    Y `SALIO DE EL` NO ES `LO MENCIONA` (21 sep 2026). Hasta hoy esta funcion buscaba
    `cap_NN` EN CUALQUIER PARTE del fichero, y un candidato que nombra otro capitulo
    en su prosa lo marcaba como minado. **El ejemplar es del reves de lo que uno
    esperaria**: un candidato de `cap_13` de `gerber_emyth` escribe

        (por ejemplo si el capitulo entero es postura sin inventario, como paso
         con cap_09 y cap_10)

    o sea **dice que esos dos NO dieron nada**, y el tablero leia ahi que si dieron.
    Medido el 21 sep: `3` falsos positivos en `gerber_emyth` (`cap_09`, `cap_10` y
    `cap_17`) y `0` en `grove_high_output`.

    **Y NO ES COSMETICO:** `ultimo_capitulo` sale de esta lista, y `D.50` manda
    continuar por el capitulo SIGUIENTE al ultimo minado. Un capitulo sin minar que
    alguien nombre de pasada **se salta el relevo y no lo mina nadie.**

    EL REPLIEGUE ES POR FICHA Y ES OBLIGATORIO, no una cortesia: los libros ya
    insertados no declaran origen (`zhuo_manager` `0` de `136`, `smart_who` `0` de
    `59`, `onu_consumidor` `0` de `6`, y `scott_radical_candor` solo `103` de `142`).
    Una regla estricta les borraria el capitulo a todos. **La ficha que declara su
    origen manda; la que no, se lee como se leia.**
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
        declarado = UNIDAD_DE_ORIGEN.search(crudo)
        if declarado:
            vistos.add(declarado.group(1))
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


def frentes_activos(declarado=None):
    """Los libros que tienen dueno ahora mismo, como tupla.

    `frente_activo.clave` admite **una clave o una lista de claves** (22 sep 2026).
    Hasta hoy era una sola, y con una sola el tablero **no podia dar dueno a dos
    frentes a la vez**: el segundo salia `PAUSADO` con dueno `NINGUNO`, que es lo
    que `D.49` usa para decir *este libro esta libre*. **Un frente corriendo con su
    libro marcado como libre es exactamente la colision que `D.49` existe para
    impedir.**

    `null` es ninguno, y es como estuvo el fichero mientras solo corrio la serial.
    """
    if declarado is None:
        declarado = declaraciones()
    clave = (declarado.get("frente_activo") or {}).get("clave")
    if not clave:
        return ()
    if isinstance(clave, str):
        return (clave,)
    return tuple(clave)


def medir():
    """UNA FILA POR LIBRO, con la verdad de este instante."""
    declarado = declaraciones()
    activos = frentes_activos(declarado)
    liberados = declarado.get("liberados") or {}
    cerrados = declarado.get("cerrados_en_extraccion") or {}
    cosechados = declarado.get("cosechados") or {}
    en_cero = declarado.get("minados_en_cero") or {}
    mapa_worktrees = worktrees()
    existentes = ramas()
    nodos = comun.leer_jsonl(comun.RUTA_DATASET)

    orden = ((declarado.get("orden_de_prioridad") or {}).get("libros")) or {}

    filas = []
    for numero, clave in lotes():
        rama = "extraccion-%s" % clave
        rama = rama if rama in existentes else None
        worktree = mapa_worktrees.get(rama) if rama else None
        propios = (_git("log", rama, "--not", RAMA_DE_INSERCION, "--pretty=format:%h")
                   .split("\n") if rama else [])
        propios = [c for c in propios if c.strip()]

        # LA BANDEJA SE CUENTA EN EL ARBOL DE SU DUEÑO, no en este.
        arbol = (comun.RAIZ if clave in cosechados
                 else (worktree if (worktree and propios) else comun.RAIZ))
        bandeja = os.path.join(arbol, "cuarentena", clave)
        candidatos = _contar_json(bandeja)
        archivo = os.path.join(comun.RAIZ, "cuarentena", "_insertados", clave)
        # UN CAPITULO MINADO SIGUE MINADO DESPUES DE INSERTARSE. Contar solo la
        # bandeja daria "ningun capitulo" para los tres lotes ya insertados, y para
        # el lote 4 daria los pendientes en vez de los minados. El relevo de D.50
        # necesita saber por donde va el LIBRO, no por donde va la bandeja.
        # UN CAPITULO MINADO A CERO ESTA MINADO (d096, y d088 y d102 son la misma
        # familia). El campo salia de lo que los candidatos CITAN, asi que un
        # capitulo leido y adjudicado en cero **no podia aparecer nunca**: grove
        # perdia cap_08, cap_09 y cap_18, y gerber perdio cap_05 y cap_06 el mismo
        # dia en que los leyo enteros.
        #
        # Y NO SE MIDE, SE DECLARA CON SU FIRMA: que un capitulo no de nodo es una
        # ADJUDICACION DE UN ACTA, no un hecho del arbol. Un instrumento que lo
        # dedujera de la ausencia no podria distinguir *leido y vacio* de *sin
        # leer*, que es justo la diferencia que importa. Por eso vive en
        # config/frentes.json con su cita, como cerrados_en_extraccion.
        capitulos = sorted(set(_capitulos_de_bandeja(bandeja))
                           | set(_capitulos_de_bandeja(archivo))
                           | set((en_cero.get(clave) or {}).get("capitulos") or ()))
        ultimo = capitulos[-1] if capitulos else ""

        insertados = _contar_json(archivo)
        en_grafo = _nodos_en_grafo(clave, nodos)
        unidades = _contar_json_md(os.path.join(comun.RAIZ, "fuentes", clave))

        # ------------------------------------------------- el estado y su dueño
        de = "medido"
        if clave in cosechados:
            # COSECHADO: su rama ya se fundio aqui, asi que sus candidatos estan en
            # ESTA bandeja y su racha murio con el frente (D.48). Se comprueba ANTES
            # que la rama: la rama sigue existiendo despues de cosechar, y sin este
            # orden un frente cosechado seguiria pareciendo un frente vivo.
            estado, dueno = "COSECHADO", NINGUNO
            de = "declarado: %s" % cosechados[clave]["cita"]
        elif rama and propios and clave not in liberados:
            estado = "EN CURSO" if clave in activos else "PAUSADO"
            dueno = clave if clave in activos else NINGUNO
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

        # LA PRIORIDAD ES UNA DECISION, NO UNA MEDIDA, y por eso sale declarada con
        # su cita. Los libros que no estan en la lista son los que ya entraron al
        # mundo 11: no se eligen, porque no queda nada que elegir de ellos.
        prioridad = orden.get(clave) or {}
        filas.append({
            "tipo": "libro",
            "lote": numero,
            "clave": clave,
            "prioridad": prioridad.get("prioridad"),
            "fuera_de_campania": bool(prioridad.get("fuera_de_campania")),
            "motivo_de_prioridad": prioridad.get("motivo", ""),
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
    return filas + cola_de_doctrina(declarado)


def libros(filas=None):
    """Las filas de LIBRO del tablero. La cola de doctrina no es un libro."""
    return [f for f in (filas if filas is not None else leer())
            if f.get("tipo", "libro") == "libro"]


def cola_de_doctrina(declarado=None):
    """LA COLA DE DOCTRINA, UNA FILA POR PREGUNTA (`D.56` punto 4).

    **Una pregunta que se contesta cuando haya tiempo y que no esta escrita en ningun
    sitio no esta en cola: esta olvidada.** Por eso vive en el tablero, que es la sede
    que toda linea lee en su apertura, y no en un acta de dieciseis mil lineas.

    **`bloquea` es el campo que la saca de la cola:** una pregunta que impide a una
    linea seguir **sube sola**, sin esperar al cierre del mundo 11.
    """
    declarado = declarado if declarado is not None else declaraciones()
    cola = declarado.get("cola_de_doctrina") or {}
    filas = []
    for pregunta in cola.get("preguntas", []):
        filas.append({
            "tipo": "doctrina",
            "n": pregunta.get("n"),
            "pregunta": pregunta.get("pregunta", ""),
            "medida_en": pregunta.get("medida_en", ""),
            "bloquea": bool(pregunta.get("bloquea")),
            "levantada_por": cola.get("levantadas_por", ""),
            "cita": cola.get("cita", ""),
            "cuando_se_resuelve": cola.get("que_dice", ""),
        })
    return filas


def doctrina_que_bloquea(filas=None):
    """Las preguntas de la cola que SI bloquean, y que por eso suben solas."""
    return [f for f in (filas if filas is not None else leer())
            if f.get("tipo") == "doctrina" and f.get("bloquea")]


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
    for fila in libros(filas):
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
    for fila in sorted(libros(filas), key=lambda f: f.get("lote", 999)):
        vale, motivo = puede_abrir(fila["clave"], linea, filas)
        if vale and fila.get("estado") in ("SIN EMPEZAR", "COSECHADO"):
            return fila["clave"], motivo
    return None, "ningun libro del orden esta libre para la linea '%s'." % linea


def siguiente_por_prioridad(linea, filas=None):
    """`D.51`: EL ORDEN LO DA EL TABLERO, Y NINGUNA LINEA ELIGE LIBRO.

    Devuelve `(clave, motivo, relevo)`:

      - `clave` es el libro de **PRIORIDAD MAS BAJA cuyo estado lo permita** (`D.49`);
      - si esta linea **ya tiene un libro suyo en curso**, ese es el que le toca, porque
        `D.50` releva **al cerrar** uno, no a mitad;
      - `relevo` es la fila del primer libro que **solo** esta bloqueado por no estar
        cosechado, que es lo que hay que pedirle al fundador (`D.50` `(b)`);
      - si no hay ninguno, `clave` es `None` **y el motivo lo dice**: `D.51` manda parar
        y decirlo, no buscarse otro.

    **LOS LIBROS FUERA DE CAMPANIA NO SE ELIGEN NUNCA.** El corte del mundo 11 los deja
    en la bandeja con su ficha, para entrar por la aduana de a uno **cuando el fundador
    lo decida**, y una campania que los tomara sola seria la campania decidiendo su
    propio alcance.
    """
    filas = libros(filas)

    propio = [f for f in filas if f.get("dueno") == linea
              and f.get("estado") in ("EN CURSO", "CERRADO EN EXTRACCION")]
    if propio:
        fila = sorted(propio, key=lambda f: f.get("lote", 999))[0]
        return fila["clave"], ("'%s' ya es de esta linea y esta %s: se continua, que "
                               "D.50 releva AL CERRAR y no a mitad."
                               % (fila["clave"], fila["estado"])), None

    ordenadas = sorted([f for f in filas if f.get("prioridad")],
                       key=lambda f: f["prioridad"])
    relevo = None
    for fila in ordenadas:
        if fila.get("fuera_de_campania"):
            continue
        vale, motivo = puede_abrir(fila["clave"], linea, filas)
        if vale:
            return fila["clave"], ("prioridad %s del orden del mundo 11. %s"
                                   % (fila["prioridad"], motivo)), relevo
        if relevo is None and fila.get("estado") == "PAUSADO" and fila.get("rama"):
            relevo = fila

    if relevo is not None:
        return None, ("NINGUN LIBRO DEL ORDEN ESTA LIBRE PARA '%s'. El de prioridad "
                      "mas baja que lo estaria es '%s', y le falta el paso (b) de "
                      "D.50: su rama '%s' no esta cosechada, con %d candidato(s) "
                      "dentro. El bucle no funde ramas: se pide y se para."
                      % (linea, relevo["clave"], relevo.get("rama") or "?",
                         relevo.get("candidatos_en_bandeja", 0))), relevo
    return None, ("NINGUN LIBRO DEL ORDEN ESTA LIBRE PARA '%s', y ninguno espera "
                  "relevo. Si los libros del CORTE del mundo 11 estan INSERTADOS "
                  "(D.60, y el corte lo declara config/frentes.json), lo que toca es "
                  "el CIERRE DEL MUNDO 11 (PARALELO.md): un PARA_ALEXIS de MUNDO 11 "
                  "COMPLETO y parar." % linea), None


def corte_del_mundo():
    """Los libros que el fundador declara como corte del mundo (`D.60`)."""
    declarado = declaraciones().get("corte_definitivo") or {}
    return list(declarado.get("libros_del_mundo_11") or ())


def mundo_11_completo(filas=None, corte=None):
    """Los libros del CORTE del mundo 11, y si estan todos ya `INSERTADO`.

    EL CORTE LO DECLARA EL FUNDADOR, NO LA PRIORIDAD (`D.60`, 21 sep 2026).

    Hasta hoy esta funcion contaba **los libros CON PRIORIDAD**, y eso metia en el
    corte a `gerber_emyth` y `marquet_turn_the_ship`, que `D.60` deja fuera y
    condicionales: **una bandeja a medias no retrasa un cierre.** Con la cuenta
    vieja, el mundo 11 no podia declararse completo nunca sin minar dos libros
    enteros que la campania decidio no pagar.

    `corte_definitivo` estaba escrito en `config/frentes.json` desde la manana del
    21 sep **y nadie lo leia**. Es la misma especie que `D.58`: una regla escrita
    que no llego al codigo.
    """
    filas = libros(filas)
    if corte is None:
        corte = corte_del_mundo()
    por_clave = {f.get("clave"): f for f in filas}
    del_mundo = [por_clave[c] for c in corte if c in por_clave]
    faltan = [f for f in del_mundo if f.get("estado") != "INSERTADO"]
    return (not faltan), del_mundo, faltan


def relevables(filas=None):
    """Los libros que `D.50` manda relevar: `EN CURSO` o `PAUSADO` en otra rama."""
    pendientes = []
    for fila in sorted(libros(filas), key=lambda f: f.get("lote", 999)):
        if fila.get("estado") in ("EN CURSO", "PAUSADO") and fila.get("rama"):
            pendientes.append(fila)
    return pendientes


# --------------------------------------------------------------------- la voz

def texto(filas=None):
    filas = filas if filas is not None else medir()
    partes = ["TABLERO DE FRENTES (D.49, D.50): sede unica del estado de la campania",
              "  registro: %s" % comun.relativa(RUTA_TABLERO), ""]
    partes.append("  %-4s %-4s %-30s %-22s %-20s %5s %7s"
                  % ("prio", "lote", "clave", "estado", "dueno", "band", "ult cap"))
    partes.append("  " + "-" * 104)
    for fila in sorted(libros(filas),
                       key=lambda f: (f.get("prioridad") or 0, f.get("lote", 99))):
        marca = str(fila.get("prioridad") or ".")
        if fila.get("fuera_de_campania"):
            marca += "*"
        partes.append("  %-4s %-4s %-30s %-22s %-20s %5d %7s"
                      % (marca, fila["lote"], fila["clave"], fila["estado"],
                         fila["dueno"], fila["candidatos_en_bandeja"],
                         fila["ultimo_capitulo"] or "."))
    partes.append("")
    partes.append("  prioridad: el orden del mundo 11 (D.51). El asterisco es FUERA DE")
    partes.append("  CAMPANIA: no se extrae, queda en bandeja para la aduana de a uno.")
    partes.append("  Sin prioridad: ya dentro del mundo 11, no hay nada que elegir.")
    partes.append("")
    con_dueno = [f for f in libros(filas) if f["dueno"] != NINGUNO]
    partes.append("  libros CON DUEÑO ahora mismo: %d" % len(con_dueno))
    for fila in con_dueno:
        partes.append("    %-30s lo trabaja '%s' (%s)"
                      % (fila["clave"], fila["dueno"], fila["estado"]))
    completo, del_mundo, faltan = mundo_11_completo(filas)
    partes.append("")
    if completo:
        partes.append("  MUNDO 11 COMPLETO: los %d libros del corte estan INSERTADOS (D.60)."
                      % len(del_mundo))
        partes.append("  Lo que toca es el CIERRE (PARALELO.md): PARA_ALEXIS de MUNDO 11")
        partes.append("  COMPLETO con el censo por libro, y parar.")
    else:
        partes.append("  MUNDO 11: faltan %d de %d libros del corte (%s)"
                      % (len(faltan), len(del_mundo),
                         ", ".join(f["clave"] for f in faltan)))

    # EL PRECIO DEL REGIMEN LIGERO, AL LADO DEL DE LA CAMPANIA (22 sep 2026, punto 2).
    # Va declarado y no medido aqui: sale del loop.log de cada corrida, que es un
    # fichero por arbol, y este instrumento corre en cualquiera de ellos.
    coste = dict((k, v) for k, v in (declaraciones().get("coste_por_turno") or {})
                 .items() if not k.startswith("_"))
    if coste:
        partes.append("")
        partes.append("  COSTE POR TURNO, MEDIDO (D.58, regimen ligero):")
        for nombre in sorted(coste, key=lambda n: coste[n]["media_usd"]):
            dato = coste[nombre]
            partes.append("    %-48s %8.4f USD/turno" % (nombre, dato["media_usd"]))
            partes.append("      %2d turnos, %8.4f total     extractor %8.4f  |  "
                          "auditor %8.4f"
                          % (dato["turnos"], dato["total_usd"],
                             dato["extractor_usd"], dato["auditor_usd"]))
            partes.append("      %s" % dato["modelos"])

    cola = [f for f in filas if f.get("tipo") == "doctrina"]
    if cola:
        bloquean = [f for f in cola if f.get("bloquea")]
        partes.append("")
        partes.append("  COLA DE DOCTRINA (D.56): %d pregunta(s), %d bloquea(n)"
                      % (len(cola), len(bloquean)))
        for fila in sorted(cola, key=lambda f: f.get("n") or 0):
            partes.append("    %s%-2s %s"
                          % ("BLOQUEA " if fila.get("bloquea") else "        ",
                             fila.get("n"), (fila.get("pregunta") or "")[:78]))

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
        if "--siguiente" in resto:
            from . import credito
            linea = credito.linea_actual()
            clave, motivo, relevo = siguiente_por_prioridad(linea)
            print("D.51, EL ORDEN LO DA EL TABLERO. Linea '%s':" % linea)
            print("  le toca: %s" % (clave or "NINGUNO, y es parada"))
            print("  %s" % motivo)
            if relevo is not None:
                print("  el relevo que hay que pedir: rama %s" % relevo.get("rama"))
            return 0 if clave else 1
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
