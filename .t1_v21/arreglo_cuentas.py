# -*- coding: utf-8 -*-
"""CORRECCION DECLARADA: LAS CUENTAS QUE YO LE ATRIBUI AL LIBRO Y EL LIBRO NO DA.

LA ESPECIE ES LA QUE LA VUELTA 20 SE CAZO A SI MISMA (ACTA 20 1.4): *mi P16 decia
la diferencia que el texto pone entre LAS DOS MANERAS de compadecerse, y el texto
NO da esa cuenta*. La relectura D.30 de hoy, con `.t1_v21/cuentas21.py` delante,
encontro 17 ocurrencias de la misma especie en mis 194 pasos.

LO QUE CAMBIA Y LO QUE NO. **No se retira ni un contenido**: los medios que el
libro nombra siguen enteros, uno a uno. Lo que se retira es la CUENTA atribuida al
libro donde el libro no la escribe. Cada linea de abajo lleva su comprobacion: el
guion falla si el texto de partida no esta tal cual, asi que no puede corregir a
ciegas.

LAS QUE SE QUEDAN, Y SE DICEN PARA QUE LA CORRECCION SE PUEDA AUDITAR: `dos anios`
(L49 two years), `las dos cosas que Russ les explico` (L53 Russ explained two
things), `cuarenta y cinco minutos` (L59 forty-five minutes), `cinco anios` (L63
five-year plans), `tres a cinco suenios` (L69), `tres a cinco columnas` (L71),
`seis a dieciocho meses` (L79), `tus tres conversaciones` (L97 YOUR three
conversations), `veinte minutos` (L103), `tres a cinco puntos` (L109), `cinco a
quince minutos` (L113), `tres o cuatro palabras` (L137), `ocho personas` (L145),
`unas cuatro personas` (L147 Four people is about the right size), `cuarenta y
cinco / quince / una hora` (L157), `tres o cuatro candidatos` (L161), `quince
minutos de sala de estudio` (L163), `las tres cosas` (L173 three things), `una de
las dos casillas` (L177 one of the two poor performance boxes), `tres o seis
meses` (L185), `dos veces al anio` (L209 twice a year), `diez anios despues` (L231
Ten years later), `las dos cosas` de P34 (L243 It rarely hurts to do both).
"""
import json

# (id, viejo, nuevo, por que)
ARREGLOS = [
    ("conversar_historia_vida_descubrir_motivadores",
     "El texto da sus dos ejemplares:",
     "El texto da sus ejemplares:",
     "L49 pone dos respuestas seguidas y NO escribe la cuenta"),
    ("conversar_historia_vida_descubrir_motivadores",
     "Haz lo mismo con los otros dos ejemplares que el texto pone:",
     "Haz lo mismo con los otros ejemplares que el texto pone:",
     "L49 pone dos mas y NO escribe la cuenta"),
    ("conversar_suenios_cruzar_habilidades",
     "que el texto nombra con sus tres preguntas:",
     "que el texto nombra con sus preguntas:",
     "L71 pone tres preguntas y NO escribe la cuenta"),
    ("armar_plan_anual_crecimiento_equipo",
     "y el texto nombra tres, tu jefe, un igual o alguien de recursos humanos.",
     "y el texto los nombra: tu jefe, un igual o alguien de recursos humanos.",
     "L105 nombra tres y NO escribe la cuenta"),
    ("armar_plan_anual_crecimiento_equipo",
     "hazte las tres preguntas del texto:",
     "hazte las preguntas del texto:",
     "L109 pone tres preguntas y NO escribe la cuenta"),
    ("montar_proceso_contratacion_reducir_sesgo",
     "basandola en tres cosas: el papel,",
     "basandola en lo que el texto nombra: el papel,",
     "L137 nombra tres bases y NO escribe la cuenta"),
    ("montar_proceso_contratacion_reducir_sesgo",
     "El texto da sus dos ejemplares: meticulosa,",
     "El texto da sus ejemplares: meticulosa,",
     "L137 da dos ejemplos y NO escribe la cuenta"),
    ("montar_proceso_contratacion_reducir_sesgo",
     "Cuenta con lo que esa prueba consigue en las dos direcciones:",
     "Cuenta con lo que el texto dice que esa prueba consigue:",
     "L139 dice las dos cosas y NO escribe la cuenta"),
    ("montar_proceso_contratacion_reducir_sesgo",
     "y cuenta con las dos razones que el texto da:",
     "y cuenta con las razones que el texto da:",
     "L147 da dos razones y NO escribe la cuenta"),
    ("montar_proceso_contratacion_reducir_sesgo",
     "contando con las dos caras que el texto le pone:",
     "contando con lo que el texto dice de esa medida:",
     "L163 dice las dos caras y NO escribe la cuenta"),
    ("admitir_pronto_mal_desempenio_cuatro_razones",
     "con sus dos preguntas y en ese orden:",
     "con sus preguntas y en ese orden:",
     "L177 hace dos preguntas y NO escribe la cuenta"),
    ("calibrar_decision_despido_documentarla",
     "y cuenta con los dos errores opuestos que el texto quiere evitar con eso:",
     "y cuenta con los errores opuestos que el texto quiere evitar con eso:",
     "L183 pone dos errores y NO escribe la cuenta"),
    ("sopesar_consejo_legal_despedir_humildad",
     "Compara entonces las dos respuestas,",
     "Compara entonces las respuestas,",
     "L193 pone dos respuestas y NO escribe la cuenta"),
    ("calibrar_ascensos_evitar_politica",
     "porque es lo que los cinco consejos vienen a prevenir:",
     "porque es lo que los consejos del texto vienen a prevenir:",
     "L213 dice some tips y NO escribe la cuenta. LA CUENTA CINCO ES MIA"),
    ("calibrar_ascensos_evitar_politica",
     "Y quedate tambien con sus dos defectos, que el texto dice",
     "Y quedate tambien con sus defectos, que el texto dice",
     "L211 pone dos defectos y NO escribe la cuenta"),
    ("evitar_obsesion_ascenso_estatus",
     "Pesa las dos cosas como el texto las pesa:",
     "Pesa el coste contra el beneficio como el texto los pesa:",
     "L233 opone coste y beneficio y NO escribe la cuenta"),
    ("evitar_obsesion_ascenso_estatus",
     "Pero ten presentes las dos mitades que el texto separa y que son",
     "Pero ten presente lo que el texto separa a continuacion, y es",
     "L235 separa las dos mitades y NO escribe la cuenta"),
    # LAS TRES CUENTAS DE TITULO Y DENOMINACION, la misma especie en otra sede
    ("montar_proceso_contratacion_reducir_sesgo",
     "con las cinco practicas que el texto nombra para manejar el sesgo",
     "con las practicas que el texto nombra para manejar el sesgo",
     "TITULO: L135 dice some simple things y NO escribe la cuenta. Y mi propia "
     "cuenta de rotulos es SEIS, no cinco: la cifra del titulo estaba ademas mal"),
    ("calibrar_ascensos_evitar_politica",
     "con los cinco consejos que el texto da",
     "con los consejos que el texto da",
     "TITULO: L213 dice some tips y NO escribe la cuenta"),
    ("reconocer_excelencia_trayectoria_gradual",
     "Las tres vias para reconocer",
     "Las vias para reconocer",
     "NOMBRE LARGO: L247 dice Another great way y NO escribe la cuenta"),
]

# Y LOS DOS RETOQUES DE COHERENCIA que salen del mismo arreglo del titulo.
COHERENCIA = [
    ("montar_proceso_contratacion_reducir_sesgo",
     "El proceso de contratacion con sus cinco practicas rotuladas por el libro: "
     "la descripcion del puesto escrita por quien contrata, el filtro previo de "
     "habilidades a ciegas, el mismo comite para varios candidatos, las "
     "entrevistas informales y los apuntes en el momento, y la reunion "
     "presencial de decision con su sesgo hacia el no",
     "El proceso de contratacion con sus practicas rotuladas una a una por el "
     "libro: la descripcion del puesto escrita por quien contrata, el filtro "
     "previo de habilidades a ciegas, el mismo comite para varios candidatos, "
     "las entrevistas informales, los apuntes escritos en el momento, y la "
     "reunion presencial de decision con su sesgo hacia el no",
     "NOMBRE LARGO: decia cinco y enumeraba cinco fundiendo dos rotulos del "
     "libro en uno. Los rotulos del libro son SEIS (L137, L139, L145, L149, "
     "L153, L159) y ahora van los seis, sin cuenta atribuida"),
    ("calibrar_ascensos_evitar_politica",
     "y los cinco consejos para que la politica no arruine tu propia reunion "
     "de calibracion",
     "y los consejos, rotulados uno a uno por el libro, para que la politica no "
     "arruine tu propia reunion de calibracion",
     "NOMBRE LARGO: misma especie que el titulo"),
]

hechos = 0
fallos = []
for ident, viejo, nuevo, razon in ARREGLOS + COHERENCIA:
    ruta = 'cuarentena/scott_radical_candor/%s.json' % ident
    bruto = open(ruta, encoding='utf-8').read()
    if viejo not in bruto:
        fallos.append((ident, viejo[:60]))
        continue
    if bruto.count(viejo) != 1:
        fallos.append((ident, 'AMBIGUO x%d: %s' % (bruto.count(viejo), viejo[:50])))
        continue
    open(ruta, 'w', encoding='utf-8').write(bruto.replace(viejo, nuevo))
    hechos += 1
    print('OK  %-46s %s' % (ident[:46], razon))

print('')
print('arreglos aplicados : %d de %d' % (hechos, len(ARREGLOS + COHERENCIA)))
print('fallos             : %d  %s' % (len(fallos), fallos if fallos else '[]'))

# EL JSON HA DE SEGUIR SIENDO JSON, y los pasos han de seguir siendo los mismos.
for ident in sorted(set(i for i, _v, _n, _r in ARREGLOS + COHERENCIA)):
    d = json.load(open('cuarentena/scott_radical_candor/%s.json' % ident,
                       encoding='utf-8'))
    print('  %-46s json valido, %d pasos' % (ident[:46], len(d['pasos_accionables'])))
