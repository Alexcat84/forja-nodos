# -*- coding: utf-8 -*-
import json, io
p = 'cuarentena/scott_radical_candor/resolver_dudas_frecuentes_reuniones_salto_nivel.json'
d = json.load(open(p, encoding='utf-8'))
viejo = ("Nota la diferencia que el texto pone entre las dos maneras de compadecerse: "
         "vaya, se nota que esto es estresante, lo siento, vamos a ver que podemos hacer "
         "para mejorar la situacion, frente a vaya, tu jefe es un microgestor, no te "
         "preocupes, voy a ponerle fin a esto.")
nuevo = ("Nota el mundo de diferencia que el texto pone entre decir vaya, se nota que esto "
         "es estresante, lo siento, vamos a ver que podemos hacer para mejorar la "
         "situacion, y decir vaya, tu jefe es un microgestor, no te preocupes, voy a "
         "ponerle fin a esto.")
assert d['pasos_accionables'][-1] == viejo, d['pasos_accionables'][-1]
d['pasos_accionables'][-1] = nuevo
d['resumen_teorico'] = d['resumen_teorico'].replace(
    "LAS CUATRO FRASES LITERALES SON LAS DEL LIBRO, traducidas y no reescritas.",
    "LAS CUATRO FRASES LITERALES SON LAS DEL LIBRO, traducidas y no reescritas. "
    "CORRECCION DECLARADA DENTRO DEL ACTO DE ESCRIBIR, SIN BORRAR LO QUE HABIA: mi P16 "
    "decia la diferencia que el texto pone entre LAS DOS MANERAS de compadecerse, y el "
    "texto NO da esa cuenta, dice a world of difference between saying X and saying Y. "
    "Una cuenta que el libro no escribe es un puente de especie propia, primo del que "
    "D.37 llama la cuenta es condicion, y la caze con el barrido de cifras de mi propia "
    "vuelta antes de dar el candidato por escrito. El paso queda sin cuenta y con el "
    "mundo de diferencia que si es del libro.")
io.open(p, 'w', encoding='utf-8').write(json.dumps(d, ensure_ascii=False, indent=1))
print("corregido P16 de", d['id'], "| pasos:", len(d['pasos_accionables']))
