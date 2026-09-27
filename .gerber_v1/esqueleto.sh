echo '$ git show 6d2d56a:docs/loop/REPORTE.md   (el esqueleto TAL COMO SE ABRIO)'
git show 6d2d56a:docs/loop/REPORTE.md | sed -n '/G1.0. EL ESQUELETO/,/^## G1.1/p' | grep '^|' | sed 's/^/  /'
echo ''
echo '$ git show a218170:docs/loop/REPORTE.md   (el esqueleto TAL COMO SE RESTAURO)'
git show a218170:docs/loop/REPORTE.md | sed -n '/G1.0. EL ESQUELETO/,/^## G1.1/p' | grep '^|' | sed 's/^/  /'
echo ''
echo '$ por commit: cuantas de las secciones G1.9 y G1.10 existian en el arbol'
for c in 6d2d56a 1ede50b 1f2b648 b2f0714 b820215 920fcc0 1fe4be8 a218170 384165b abf7515; do
  n=$(git show $c:docs/loop/REPORTE.md | grep -c '^## G1\.9\.\|^## G1\.10\.')
  s=$(git show $c:docs/loop/REPORTE.md | grep -c 'G1\.6` a `G1\.10')
  printf '  %s  secciones G1.9 o G1.10 en el arbol: %s   el esqueleto las promete: %s\n' "$c" "$n" "$s"
done
