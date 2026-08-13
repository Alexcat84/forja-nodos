#!/bin/sh
# Instalador del hook de pre-commit de forja-nodos.
#
#     bash hooks/install_hooks.sh
#
# Copia hooks/pre-commit a .git/hooks/pre-commit y lo deja ejecutable. Se copia
# en vez de enlazarse porque los enlaces simbolicos no viajan igual en Windows,
# y esta forja tiene que arrancar donde este.
#
# Si ya editaste hooks/pre-commit, vuelve a correr esto: sobrescribe.

set -e

RAIZ=$(git rev-parse --show-toplevel)
ORIGEN="$RAIZ/hooks/pre-commit"
DESTINO="$RAIZ/.git/hooks/pre-commit"

if [ ! -f "$ORIGEN" ]; then
    echo "no encuentro $ORIGEN"
    exit 1
fi

mkdir -p "$RAIZ/.git/hooks"
cp "$ORIGEN" "$DESTINO"
chmod +x "$DESTINO" 2>/dev/null || true

echo "hook instalado en .git/hooks/pre-commit"
echo "corre el gate y el barrido de guiones en cada commit, y aborta en rojo."
echo ""
echo "comprobacion rapida (ha de terminar en verde):"
echo "    sh hooks/pre-commit"
