# casar.py: casa cada candidato de la bandeja con la unidad de fuentes/ de la que sale.
# PRIMERA LINEA OBLIGADA (REMEDIO 4 de la ACTA 30): este instrumento NO lleva ni una
# lista de ids ni un termino de busqueda tecleado. Los terminos los saca del propio
# candidato: tokens capitalizados y numeros, que son los que sobreviven a la traduccion.
# El separador de millar se normaliza de 5.000 a 5,000 porque el candidato escribe en
# castellano y el libro en ingles; esa sustitucion es la unica constante del fichero.
import json, re, sys, pathlib, collections

bandeja = pathlib.Path(sys.argv[1])
fuente = pathlib.Path(sys.argv[2])

def cuerpo(p):
    t = p.read_text(encoding="utf-8", errors="replace")
    partes = t.split("---", 2)
    return partes[2] if len(partes) > 2 else t

unidades = {f.stem: cuerpo(f) for f in sorted(fuente.glob("cap_*.md"))}
TOK = re.compile(r"\b[A-Z][a-zA-Z]{2,}\b|\b\d[\d,]{2,}\b")
TOPE = 4

print("candidato | unidad ganadora | aciertos | segunda | tokens que la casan")
for f in sorted(bandeja.glob("*.json")):
    d = json.loads(f.read_text(encoding="utf-8"))
    texto = " ".join([d["titulo"], d["condiciones_activacion"],
                      d["entregable_esperado"]] + d["pasos_accionables"])
    texto = re.sub(r"(\d)\.(\d\d\d)", r"\1,\2", texto)
    marcador = collections.Counter()
    donde = collections.defaultdict(list)
    for t in sorted(set(TOK.findall(texto))):
        dentro = [u for u, c in unidades.items() if t in c]
        if dentro and len(dentro) <= TOPE:
            for u in dentro:
                marcador[u] += 1
                donde[u].append(t)
    orden = marcador.most_common(2)
    gana = orden[0] if orden else ("SIN CASAR", 0)
    seg = orden[1] if len(orden) > 1 else ("ninguna", 0)
    print("%s | %s | %d | %s %d | %s" % (d["id"], gana[0], gana[1], seg[0], seg[1],
                                         ",".join(donde[gana[0]])))
