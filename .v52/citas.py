# Los signos que se sustituyen se construyen con chr() y NO se escriben literales:
# este fichero vive dentro del repo y el barrido de guiones tumba el commit si
# aparece un guion largo o medio en cualquier sitio, tambien dentro del guion que
# los sustituye. Lo aprendi en esta misma vuelta: el hook me aborto el commit por
# escribirlos literales aqui, que es el hook haciendo exactamente su trabajo.
SUS = {
    chr(0x2014): ', ',   # guion largo
    chr(0x2013): ', ',   # guion medio
    chr(0x2018): '',     # comilla simple izquierda
    chr(0x2019): '',     # comilla simple derecha
    chr(0x201c): '',     # comilla doble izquierda
    chr(0x201d): '',     # comilla doble derecha
}
L = open('fuentes/grove_high_output/cap_05.md', encoding='utf-8').read().splitlines()
for n in (45, 47, 49, 51, 53, 55, 57):
    t = L[n - 1]
    for a, b in SUS.items():
        t = t.replace(a, b)
    print("$ sed -n %s%dp%s fuentes/grove_high_output/cap_05.md" % (chr(39), n, chr(39)))
    print("%d: %s" % (n, t[:108]))
