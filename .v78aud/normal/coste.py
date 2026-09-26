# ACTA 77: el coste de los dos turnos de la vuelta 78 contra el umbral de 10 USD (D.55), leido de los json del arnes. Copia de .v77aud/normal/coste.py con la cabecera cambiada. Solo lee.
import json, io
for f in ("docs/loop/ultimo_extractor.json", "docs/loop/ultimo_apertura.json"):
    j = json.load(io.open(f, encoding="utf-8")); u = j["usage"]
    print("%s | USD %.2f | %d s de API | turnos %d | entrada %d | cache escrita %d | cache leida %d | salida %d (pensamiento %d)" % (
        f.split("/")[-1], j["total_cost_usd"], j["duration_api_ms"] // 1000, j["num_turns"], u["input_tokens"],
        u["cache_creation_input_tokens"], u["cache_read_input_tokens"], u["output_tokens"], u["output_tokens_details"]["thinking_tokens"]))
