# -*- coding: utf-8 -*-
"""EL ESTADO DEL ARBOL EN ESTA FASE, tal cual, para dejarlo escrito."""
import subprocess
for orden in (['git', 'rev-parse', 'HEAD'],
              ['git', 'rev-parse', '--abbrev-ref', 'HEAD'],
              ['git', 'status', '--short'],
              ['git', 'log', '-1', '--format=%h %ad', '--date=iso']):
    print('$ ' + ' '.join(orden))
    print(subprocess.check_output(orden).decode('utf-8', 'replace').rstrip())
    print()
