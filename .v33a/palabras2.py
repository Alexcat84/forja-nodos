# PRIMERA LINEA (HEREDADO 4): CERO CIFRAS TECLEADAS COMO DATO. Las tres formas de contar
# van sobre el mismo fichero fuente; lo unico tecleado es su nombre.
import io, re
RUTA = 'fuentes/scott_radical_candor/cap_08.md'
L = io.open(RUTA, encoding='utf-8').read().split('\n')
ini = [n for n,l in enumerate(L) if l.strip()=='---'][1] + 1
def bloque(a,b): return '\n'.join(L[a:b])
formas = {
  'split() a secas'            : lambda t: len(t.split()),
  'regex [A-Za-z0-9 apostrofo guion]' : lambda t: len(re.findall(r"[A-Za-z0-9’'-]+", t)),
  'regex solo letras y digitos': lambda t: len(re.findall(r"[A-Za-z0-9]+", t)),
}
casos = {
  'cuerpo entero tras el frontmatter (L8 al final)' : bloque(ini, len(L)),
  'cuerpo sin el arranque del capitulo siguiente'   : bloque(ini, 186),
  'tramo FREE AT WORK (L46 a L66)'                  : bloque(45, 66),
  'tramo FREE AT WORK con su rotulo (L45 a L66)'    : bloque(44, 66),
}
for nc, txt in casos.items():
    print(nc)
    for nf, f in formas.items():
        print("    %-36s %5d" % (nf, f(txt)))
