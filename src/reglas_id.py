# -*- coding: utf-8 -*-
"""Reglas de id escritas y ejecutables (manual seccion 2).

La version en prosa, con ejemplos validos e invalidos, vive en
docs/REGLAS_DE_ID.md. Este modulo es la misma ley en codigo: si las dos
se separan, manda el documento y este archivo esta roto.
"""

import re

from . import comun

PATRON = re.compile(r"^[a-z][a-z0-9_]*$")

# Preposiciones y articulos: prohibidos como pieza de un id.
PALABRAS_VACIAS = {
    "a", "al", "ante", "bajo", "con", "contra", "de", "del", "desde", "durante",
    "el", "en", "entre", "hacia", "hasta", "la", "las", "lo", "los", "mediante",
    "para", "por", "que", "segun", "sin", "so", "sobre", "tras", "un", "una",
    "unas", "unos", "y", "o", "u", "e",
}

# =========================================================================
# REGLA 1, REESCRITA POR DECISION DEL FUNDADOR DEL 10 SEP 2026.
#
# La version vieja era una lista negra de 37 palabras que se llamaba a si
# misma "lexico ajeno que aparece con mas frecuencia en esta forja". El
# estreno de la aduana la midio: dejaba pasar al menos 269 de los 3.169 ids
# vivos del catalogo auditado (8,5 por ciento), y dejaba entrar
# `variance_analysis` y `work_breakdown_structure` enteros.
#
# LA DECISION NO FUE ENGORDARLA A CIEGAS NI PONER UNA PRUEBA DE IDIOMA
# AUTOMATICA. Fue darle CRITERIO, y son dos listas:
#
#   NEGRA  palabra inglesa QUE TIENE EQUIVALENTE CORRIENTE EN CASTELLANO.
#          Si la palabra existe en castellano y se usa, el id la usa.
#   BLANCA prestamo ASENTADO en el castellano de negocios, donde traducir
#          fabricaria un termino que nadie dice.
#
# NO ES PURISMO, Y ESTE ES EL MOTIVO TECNICO: dos grafias del mismo concepto
# parten la familia. `retencion_clientes` y `customer_retention` tienen clave
# de familia DISJUNTA, asi que la señal 2 no los ve juntos y entran los dos.
# Un solo idioma en los ids no es gusto: es que la señal pueda hacer su
# trabajo. El termino ingles viaja igual, en denominaciones.otros_idiomas
# (manual seccion 3.1), que es su sede.
#
# LOS 269 IDS DEL CATALOGO SON COSA JUZGADA (decision del fundador, misma
# fecha): esta lista rige lo que se ESCRIBE de ahora en adelante. No se
# reabre un id ya adjudicado por una lista que llego despues.
# =========================================================================

# LA NEGRA. Sale de contar los 3.169 vivos del catalogo auditado, no de
# imaginar: cada pieza de aqui aparecio de verdad en un id, y cada una tiene
# su palabra castellana corriente al lado.
INGLES_CON_EQUIVALENTE = {
    # las 37 de la lista vieja, que siguen siendo negras
    "and", "audit", "book", "chapter", "check", "data", "edge", "extract",
    "extraction", "for", "framework", "gate", "graph", "guide", "knowledge",
    "loop", "merge", "node", "nodes", "of", "pipeline", "process", "review",
    "rule", "rules", "schema", "scope", "source", "sources", "step", "steps",
    "the", "to", "tool", "tools", "with", "workflow",
    # gestion y negocio
    "business", "management", "development", "performance", "governance",
    "ownership", "accountability", "administration", "execution", "operating",
    "planning", "scheduling", "budgeting", "forecasting", "monitoring",
    "tracking", "reporting", "staffing", "hiring", "employee",
    "employees", "owner", "owners", "leadership", "stakeholder", "stakeholders",
    "shareholder", "shareholders", "partners", "partnerships", "partnership",
    "collaboration", "cooperation", "community", "workshop",
    "meetings", "meeting", "homework", "letters", "letter", "statement",
    "agreement", "agreements", "convention", "settlement", "consideration",
    # calidad, riesgo y produccion
    "quality", "assurance", "conformance", "reliability", "maintenance",
    "manufacturing", "assembly", "equipment", "inspection", "sampling",
    "screening", "validation", "verification", "certification", "traceability",
    "documentation", "registration", "regulation", "deregulation", "compliance",
    "security", "safety", "protection", "prevention", "infection", "guarding",
    "lockout", "shock", "waste", "reduction", "rework", "outliers", "variance",
    "duration", "capability", "acceptance", "excellence", "integrity",
    "fairness", "materiality", "proneness", "adherence",
    # cadena y logistica
    "supply", "procurement", "warehouse", "warehouses", "shipping", "freight",
    "packaging", "picking", "loading", "handling", "inventory", "consignment",
    "backhaul", "distribution", "providers", "provider", "buyers", "buyer",
    "trucks", "truck", "fleet", "rationing", "shortage", "buffer", "stockout",
    # mercado y cliente
    "customer", "customers", "market", "markets", "selling", "sales",
    "pricing", "price", "discount", "advertising", "awareness", "acquisition",
    "retention", "loyalty", "share", "positioning", "segmentation", "targeting",
    "proposition", "offer", "welcome", "satisfaction", "complaint",
    # dinero
    "cash", "financing", "fundraising", "investment", "valuation", "payback",
    "profit", "revenue", "cost", "costs", "fee", "fees", "banker", "trading",
    "warrant", "warrants", "warranties", "warranty", "redemption", "licensing",
    "indemnification", "antidilution", "vesting", "goodwill", "runway",
    "equity",
    # conocimiento y metodo
    "theory", "hypothesis", "assumption", "assumptions", "experiment",
    "simulation", "investigation", "negotiation", "evaluation", "assessment",
    "measurement", "calculation", "estimating", "clustering",
    "mapping", "modeling", "prototyping", "iteration", "learning", "thinking",
    "understanding", "insight", "insights", "empathy", "awe", "consciousness",
    "rationality", "groupthink", "hindsight", "mentality", "attention",
    "feedback",
    # producto y obra
    "building", "engineering", "design", "usability", "functionality",
    "feasibility", "viability", "desirability", "affordances", "breakdown",
    "completion", "scoping", "integration", "automation", "computing",
    "spreadsheet", "worksheet", "checklist", "sheet",
    "sheets", "screen", "dashboard", "network", "networks", "layers", "stack",
    "phase", "phases", "activity", "activities", "action", "actions",
    "solution", "solutions", "option", "options", "effect", "effects",
    "growth", "traction", "innovation", "creation", "sustainability",
    "environment", "physical", "law", "laws", "rights",
    "right", "path", "pathways", "truth", "power", "influence", "wheel",
    "wheels", "wave", "waterfall", "shadow", "war", "room", "seed", "seeding",
    "wind", "green", "black", "high", "low", "thin", "sharp", "narrow",
    "hollow", "free", "good", "worst", "new", "three", "twos", "view",
    "views", "shop", "kit", "pool", "ring", "mesh", "mock", "hook", "yoke",
    "bucket", "buckets", "wedge", "metaphor", "methods", "method", "ways",
    "way", "thing", "things", "needs", "need", "known", "unknown", "unknowns",
    # `who` entra el 10 sep 2026 por decision del fundador, heredada del ACTA
    # 6: el titulo de un libro no exime a un id. Su equivalente corriente es
    # `quien`, y el ingles viaja en denominaciones.otros_idiomas.
    "who",
    # verbos y particulas sueltas de ingles
    "accomplish", "affirm", "attack", "back", "calling", "click", "down",
    "enough", "falling", "getting", "grow", "how", "keep", "kill", "make",
    "matching", "might", "noticing", "off", "playing", "proceed", "pruning",
    "push", "sharing", "speaking", "spotting",
    "starting", "staging", "take", "that", "what", "work", "works",
}

# LA BLANCA. Prestamos que el castellano de negocios ya dice sin traducir.
# Los seis primeros los nombro el fundador; el resto salio de medir los 269.
# TRADUCIRLOS FABRICARIA UN TERMINO QUE NADIE USA, y un id que nadie
# reconoce es un id que se vuelve a escribir de otra forma.
PRESTAMOS_ASENTADOS = {
    "marketing", "benchmarking", "startup", "lean", "coaching", "scrum",
    "backlog", "branding", "brainstorming", "bootstrapping", "coworking",
    "crossdocking", "crowdfunding", "engagement", "escrow",
    "freemium", "greenwashing", "kaizen", "kanban", "leasing",
    "marketplace", "marketplaces", "networking", "onboarding", "outsourcing",
    "pivot", "ranking", "retargeting", "software", "stock", "storytelling",
    "web",
}

# NI UNA COSA NI OTRA: NOMBRE PROPIO Y SIGLA. Un apellido no tiene
# equivalente en castellano, y una sigla tampoco: `deming` no se traduce y
# `osha` no es una palabra. No se cazan, y van escritas para que nadie las
# meta en la negra creyendo que se le escaparon.
NOMBRES_Y_SIGLAS = {
    "ackerman", "bloom", "coshh", "coo", "crosby", "deming", "ewma", "gee",
    "hawthorne", "hoshin", "jenkins", "juran", "leed", "niosh", "ooda",
    "osha", "ppph", "pugh", "shewhart", "shingo", "sp800171", "swot", "wald",
    "wallas", "wbs", "weibull", "westrum",
}

# LA NEGRA Y LA BLANCA NO PUEDEN SOLAPARSE: una palabra no puede tener
# equivalente corriente Y ser un prestamo asentado. Si alguna vez chocan, la
# regla dejo de tener criterio. Lo comprueba tests/test_aceptacion.py.
assert not (INGLES_CON_EQUIVALENTE & PRESTAMOS_ASENTADOS)
assert not (INGLES_CON_EQUIVALENTE & NOMBRES_Y_SIGLAS)

# Nombre viejo, conservado porque el documento en prosa lo cita. Es LA MISMA
# lista negra, con criterio y medida.
LEXICO_AJENO = INGLES_CON_EQUIVALENTE

# REGLA 2, ACOTADA POR DECISION DEL FUNDADOR DEL 10 SEP 2026.
#
# La version vieja prohibia TODO `_\d+$`. Medido sobre el catalogo: de los 48
# ids vivos que acaban en numero, 44 llevan un numero de UNA CIFRA y son
# versiones (`accion_correctiva_2`, `consejo_de_calidad_3`), y los 4 que
# llevan un numero mayor son DENOMINACIONES: `familia_normas_iso_9000`,
# `cumplimiento_ftc_rule_436`, `canales_de_traccion_19`, `riesgo_split_51_49`.
#
# NADIE HACE UNA VERSION 436. Ese es el corte, y esta contado: 48 de 48.
TOPE_DE_VERSION = 9


def piezas(identificador):
    return [p for p in identificador.split("_") if p]


def familia(identificador):
    """Clave de familia de un id (señal 2 de la aduana y guarda del gate).

    Normaliza sufijos numericos, preposiciones, articulos, plurales y el
    orden de las palabras. Dos ids con la misma clave son la misma familia:
    o son el mismo nodo, o merecen revision antes de existir.
    """
    piezas_normalizadas = set()
    for pieza in piezas(comun.normalizar_texto(identificador.replace("_", " ")).replace(" ", "_")):
        pieza = re.sub(r"\d+$", "", pieza)
        if not pieza or pieza in PALABRAS_VACIAS:
            continue
        # Plural y singular han de caer en la MISMA pieza. Se quita la ese
        # final y despues la e final, en ese orden: asi 'fuentes' y 'fuente'
        # dan los dos 'fuent', que es lo unico que importa aqui. Si solo se
        # quitara la ese, 'fuentes' daria 'fuente' y 'fuente' daria 'fuente'
        # en unos casos y 'fuent' en otros, y la familia dejaria de agrupar.
        if len(pieza) > 3 and pieza.endswith("s"):
            pieza = pieza[:-1]
        if len(pieza) > 4 and pieza.endswith("e"):
            pieza = pieza[:-1]
        if pieza:
            piezas_normalizadas.add(pieza)
    return frozenset(piezas_normalizadas)


def similitud_familia(id_a, id_b):
    familia_a, familia_b = familia(id_a), familia(id_b)
    if not familia_a or not familia_b:
        return 0.0
    interseccion = len(familia_a & familia_b)
    union = len(familia_a | familia_b)
    return float(interseccion) / float(union)


def validar(identificador, campo="id", es_alias=False):
    """Devuelve la lista de fallos del id. Lista vacia es verde.

    Los ids_alias son ids MUERTOS: se les exige forma (snake_case, sin
    rayas) pero no doctrina (un alias existe justamente porque alguna vez
    se escribio mal). Al id canonico se le exige todo.
    """
    fallos = []
    if not isinstance(identificador, str) or not identificador:
        return ["%s: id vacio" % campo]
    if not PATRON.match(identificador):
        fallos.append("%s '%s': solo minusculas, digitos y guion bajo, empezando por letra"
                      % (campo, identificador))
        return fallos
    if "__" in identificador:
        fallos.append("%s '%s': guion bajo doble" % (campo, identificador))
    if es_alias:
        return fallos
    trozos = piezas(identificador)
    version = re.search(r"_(\d+)$", identificador)
    if version and int(version.group(1)) <= TOPE_DE_VERSION:
        fallos.append(
            "%s '%s': sufijo numerico de VERSION prohibido (regla 2 de "
            "docs/REGLAS_DE_ID.md). Un concepto, un nodo: si es otra cosa se "
            "llama de otra forma, y si es lo mismo no entra dos veces. El "
            "numero que es parte de la denominacion SI vale, y va donde le "
            "toca: los_14_puntos_deming, familia_normas_iso_9000"
            % (campo, identificador))
    vacias = [t for t in trozos if t in PALABRAS_VACIAS]
    if vacias:
        fallos.append("%s '%s': preposicion o articulo prohibido: %s (regla 3)"
                      % (campo, identificador, ", ".join(sorted(set(vacias)))))
    ajenas = [t for t in trozos if t in INGLES_CON_EQUIVALENTE]
    if ajenas:
        fallos.append(
            "%s '%s': palabra inglesa con equivalente corriente en castellano: "
            "%s (regla 1). El termino ingles va en denominaciones.otros_idiomas, "
            "que es su sede. Un prestamo asentado (marketing, startup, lean) SI "
            "vale: la lista blanca esta en src/reglas_id.py"
            % (campo, identificador, ", ".join(sorted(set(ajenas)))))
    if len(trozos) < 2:
        fallos.append("%s '%s': un id nombra un procedimiento, no una palabra suelta "
                      "(regla 5: verbo mas objeto)" % (campo, identificador))
    return fallos


def normalizar(bruto):
    """Lleva un id de entrada humana a la forma de la casa.

    No inventa doctrina: baja a minusculas, quita acentos, convierte
    espacios y rayas en guion bajo. Si despues de eso el id sigue
    rompiendo una regla, la aduana lo rechaza en vez de maquillarlo.
    """
    texto = comun.sin_acentos((bruto or "").strip().lower())
    for guion in comun.GUIONES_PROHIBIDOS:
        texto = texto.replace(guion, "_")
    texto = texto.replace("-", "_")
    texto = re.sub(r"[^a-z0-9_]+", "_", texto)
    texto = re.sub(r"_+", "_", texto)
    return texto.strip("_")
