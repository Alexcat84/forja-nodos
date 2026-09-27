# -*- coding: utf-8 -*-
"""LA CITA DE LINEA LLEVA SU SALIDA PEGADA AL LADO (D.35).

Imprime la tabla de los pasos que mire dos veces, con el trozo LITERAL de la linea
del libro que los sostiene, leido de `fuentes/scott_radical_candor/cap_11.md`.
"""
import io
import sys

LIBRO = "fuentes/scott_radical_candor/cap_11.md"
LINEAS = io.open(LIBRO, encoding="utf-8").read().split("\n")

MAPA = [(chr(0x2014), "-"), (chr(0x2013), "-"), (chr(0x2019), "'"), (chr(0x2018), "'"),
        (chr(0x201c), '"'), (chr(0x201d), '"'), (chr(0x2026), "..."), (chr(0xa0), " ")]


def limpia(texto):
    for viejo, nuevo in MAPA:
        texto = texto.replace(viejo, nuevo)
    return texto.replace("|", "/")


def cita(numero, ancla, largo):
    texto = limpia(LINEAS[numero - 1])
    donde = texto.find(ancla)
    assert donde >= 0, (numero, ancla)
    antes = "..." if donde > 0 else ""
    trozo = texto[donde:donde + largo]
    despues = "..." if donde + largo < len(texto) else ""
    return "%d: %s%s%s" % (numero, antes, trozo, despues)


salida = io.open(sys.argv[1], "w", encoding="utf-8", newline="\n")
salida.write("| paso | la salida de `.v31/cita.py` sobre el libro, pegada | veredicto |\n")
salida.write("|---|---|---|\n")


def fila(rotulo, numero, ancla, largo, veredicto):
    salida.write("| %s | `%s` | %s |\n" % (rotulo, cita(numero, ancla, largo), veredicto))


fila("`decidir_quien_comunica_cada_cuanto` paso `6`: los diez rotulos de la rueda, "
     "enumerados uno a uno",
     17, "1:1 Conversations", 40,
     "**TRANSCRIPCION**: los diez estan en `L17` a `L35`, un rotulo por linea, y el paso "
     "los pasa los diez")
fila("`montar_reuniones_solas_mentalidad_frecuencia` paso `10`: *cincuenta minutos a la "
     "semana, cinco horas, cinco personas*",
     53, "I like to meet with each person", 190, "**TRANSCRIPCION**")
fila("`conducir_reunion_equipo_agenda_tres_bloques` paso `20`: *deja que los duenios no "
     "sean ni tu ni la gente que te reporta*",
     161, "The debate and decision owners", 180, "**TRANSCRIPCION**")
fila("`escribir_apuntes_sala_estudio_equipo` paso `10`: *el texto nombra los sitios donde "
     "vale hacerlo*",
     155, "You can use Google Docs", 60,
     "**TRANSCRIPCION**, y es el que mire dos veces: el paso dice que el libro los nombra "
     "**sin nombrarlos**. Dice MENOS que el libro, no mas, asi que no es `PUENTE`")
fila("`pelear_proliferacion_reuniones_bloquear_ejecucion` paso `7`: *bloquea tiempo para "
     "estar a solas y ejecutar, por la misma razon*",
     233, "I have found that the most effective", 210,
     "**TRANSCRIPCION**, y **no escribe las dos horas**, que son del caso del CEO de `L171`")
salida.close()
print("escrita la tabla de citas en %s" % sys.argv[1])
