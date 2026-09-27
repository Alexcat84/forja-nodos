# -*- coding: utf-8 -*-
"""LA GUARDA QUE EL REPORTE DECLARA MORDIENDO, VUELTA A MORDER POR MUTACION
(cosecha 7.C). La puerta de D.39 sobre config/frentes.json, mutada en una COPIA
fuera del arbol: si lee el estado y no una constante, tiene que cambiar."""
import io, json, os, tempfile

crudo = io.open("config/frentes.json", encoding="utf-8").read()
d = json.loads(crudo)
cerrados = d.get("cerrados_en_extraccion", d)
print("cerrados_en_extraccion en el repo      :", sorted(cerrados.keys()))
print("grove_high_output CERRADO EN EXTRACCION:",
      "grove_high_output" in cerrados, "   <- lo que el repo dice")

mutado = json.loads(crudo)
mutado.setdefault("cerrados_en_extraccion", {})["grove_high_output"] = {
    "cita": "MUTACION DEL AUDITOR, NO ES UNA DECISION"}
tmp = os.path.join(tempfile.gettempdir(), "frentes_mutado_auditor.json")
io.open(tmp, "w", encoding="utf-8").write(json.dumps(mutado, ensure_ascii=False))
leido = json.loads(io.open(tmp, encoding="utf-8").read())
print("grove_high_output CERRADO EN EXTRACCION:",
      "grove_high_output" in leido["cerrados_en_extraccion"],
      "   <- con la celda mutada")
os.remove(tmp)
