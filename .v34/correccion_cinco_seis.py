# -*- coding: utf-8 -*-
"""LA CORRECCION EN CUARENTENA, ANTES DE INSERTAR: la cuenta pasaba de CINCO a SEIS.

Es una operacion DE UN SOLO USO y ya corrio: deja el registro de lo que hizo y NO
vuelve a tocar nada. Quien quiera recontarlo, cuenta los rotulos del libro.
"""
import io, json, os
VIEJO = "cuarentena/scott_radical_candor/dar_guia_acto_cinco_consejos.json"
for base in ("cuarentena/scott_radical_candor", "cuarentena/_insertados/scott_radical_candor"):
    NUEVO = "%s/dar_guia_acto_seis_consejos.json" % base
    if os.path.exists(NUEVO):
        d = json.load(io.open(NUEVO, encoding="utf-8"))
        print("CORRECCION EN CUARENTENA, ANTES DE INSERTAR")
        print("  id viejo : dar_guia_acto_cinco_consejos")
        print("  id nuevo : dar_guia_acto_seis_consejos")
        print("  la cuenta pasa de CINCO a SEIS rotulos, contados L123 L127 L129 L131 L133 L135")
        print("  pasos    : %d, ninguno anadido ni quitado" % len(d["pasos_accionables"]))
        print("  el id viejo sigue existiendo: %s" % os.path.exists(VIEJO))
        raise SystemExit(0)
raise SystemExit("NO ENCUENTRO dar_guia_acto_seis_consejos en ninguna de las dos sedes")
