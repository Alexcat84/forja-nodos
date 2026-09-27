set -u
cd "$(git rev-parse --show-toplevel)"
rm -f .v54/d033_tasa.txt
echo '$ por 12 corridas: python -m unittest tests.test_aceptacion.PruebaE.test_e_guion_largo_rompe_el_hook' >> .v54/d033_tasa.txt
for i in $(seq 1 12); do
  ini=$(date +%s)
  salida=$(python -m unittest tests.test_aceptacion.PruebaE.test_e_guion_largo_rompe_el_hook 2>&1)
  cod=$?
  fin=$(date +%s)
  if [ $cod -eq 0 ]; then res=VERDE; else res=ROJO; fi
  echo "corrida $i  $res  $((fin-ini)) s" >> .v54/d033_tasa.txt
  if [ $cod -ne 0 ]; then echo "$salida" > ".v54/d033_fallo_$i.txt"; fi
done
echo FIN >> .v54/d033_tasa.txt
