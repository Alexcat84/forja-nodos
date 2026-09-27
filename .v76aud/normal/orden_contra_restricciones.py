# ACTA 75: su orden (.v76ext/orden.txt, filas 1 a 22) contra las restricciones de mi lectura sellada (APERTURA_CIEGA.md 7) y
# contra las de esta acta (75.4): madre antes que hijo, y D.36 de un solo lado. Solo lee. Toda linea que reparte trae su suma (R7).
import collections, io, re, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
fila = {}
for l in open(".v76ext/orden.txt", encoding="utf-8"):
    m = re.match(r"^(\d+)\s+(\S+)\s+cap_", l)
    if m: fila[m.group(2)] = int(m.group(1))
R = [  # (madre o primero, hijo o despues, de donde sale)
 ("construir_estrategia_gente_cuatro_componentes", "aplicar_cinco_pasos_proceso_contratacion", "mi CONTINUA, 75.4 relectura conjunta"),
 ("aplicar_seis_pasos_sistema_venta", "medir_sistema_venta_trece_indicadores_benchmark", "CONTINUA de los dos"),
 ("cambiar_saludo_cliente_dos_ramas", "cuantificar_impacto_innovacion_6_pasos", "CONTINUA de los dos"),
 ("recorrer_siete_pasos_programa_desarrollo_negocio", "construir_estrategia_gente_cuatro_componentes", "D.37 de los dos"),
 ("fingir_prototipo_cinco_mil_replicas", "dar_valor_constante_cuatro_publicos", "D.37 de los dos"),
 ("fingir_prototipo_cinco_mil_replicas", "operar_modelo_gente_destreza_minima", "D.37 de los dos"),
 ("fingir_prototipo_cinco_mil_replicas", "documentar_trabajo_manual_operaciones", "D.37 de los dos"),
 ("fingir_prototipo_cinco_mil_replicas", "unificar_color_forma_vestuario_modelo", "D.37 de los dos"),
 ("fingir_prototipo_cinco_mil_replicas", "recorrer_siete_pasos_programa_desarrollo_negocio", "mi D.29, 75.4 relectura conjunta"),
 ("construir_estrategia_gente_cuatro_componentes", "documentar_trabajo_manual_operaciones", "su D.37 (D76.14), 75.4"),
 ("responder_8_preguntas_construir_primary_aim", "construir_estrategia_gente_cuatro_componentes", "mi D.29 sellada, que cae en 75.4"),
 ("responder_4_preguntas_estandares_objetivo_estrategico", "construir_estrategia_gente_cuatro_componentes", "mi D.29 sellada, que cae en 75.4"),
 ("fingir_prototipo_cinco_mil_replicas", "aplicar_cinco_pasos_proceso_contratacion", "D.36 de un solo lado"),
 ("medir_sistema_venta_trece_indicadores_benchmark", "construir_estrategia_gente_cuatro_componentes", "D.36 de un solo lado"),
 ("interrogar_negocio_cinco_preguntas", "operar_modelo_gente_destreza_minima", "D.36 de un solo lado"),
 ("dar_valor_constante_cuatro_publicos", "probar_traje_azul_seis_semanas", "D.36 de un solo lado"),
]
print("filas de su orden:", len(fila))
c = collections.Counter()
for a, b, o in R:
    ok = fila[a] < fila[b]
    c["la cumple" if ok else "LA VIOLA"] += 1
    print(f"  {fila[a]:>2} {a:<55} antes que {fila[b]:>2} {b:<55} {o:<36} {'la cumple' if ok else 'LA VIOLA'}")
print("restricciones:", len(R), "|", dict(c), "| suma:", sum(c.values()))
