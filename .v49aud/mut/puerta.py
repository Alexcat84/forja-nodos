import json, pathlib
f = json.loads(pathlib.Path("config/frentes.json").read_text(encoding="utf-8"))
cer = f.get("cerrados_en_extraccion", {})
print('    $ python .v48/puerta.py   sobre config/frentes.json')
print("cerrados_en_extraccion :", cer)
print("grove_high_output CERRADO EN EXTRACCION:", "grove_high_output" in cer)
