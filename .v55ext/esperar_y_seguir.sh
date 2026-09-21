#!/bin/bash
cd "$(dirname "$0")/.."
while ! grep -q "^FIN " .v55ext/aduana_p22.txt 2>/dev/null; do sleep 10; done
bash .v55ext/aduana_chain2.sh
