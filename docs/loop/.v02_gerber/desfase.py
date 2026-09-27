# desfase.py: mide el desfase entre numerar el FICHERO CRUDO y numerar el CUERPO
# (lo que queda tras el frontmatter). Sin constantes tecleadas: cuenta los --- del
# propio fichero. Existe porque dos documentos que citan "L" con bases distintas
# se contradicen sin que ninguno mienta.
import sys, pathlib
for p in sorted(pathlib.Path(sys.argv[1]).glob("cap_*.md")):
    lineas = p.read_text(encoding="utf-8", errors="replace").splitlines()
    cortes = [i for i, l in enumerate(lineas, 1) if l.strip() == "---"]
    print("%s  lineas %4d  cierre del frontmatter en L%d  desfase crudo menos cuerpo = %d"
          % (p.stem, len(lineas), cortes[1], cortes[1]))
