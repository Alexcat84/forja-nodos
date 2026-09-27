"""d052: la frontera que ninguna senial va a levantar, escrita dentro de la ficha.

Adjudicado por el auditor con la vara 6.1 (DOS DOCTRINAS LEGITIMAS NO SON DUPLICADO:
son FRONTERA DECLARADA), ACTA 50 seccion 50.5.b. No es caida de nadie y no abre doctrina.

Escribe dentro de cubrir_indicadores_problemas_reunion_individual, por correccion
declarada y sin borrar, la frontera con las dos posiciones y sus fuentes, nombrando el
id del nodo del grafo y su linea del otro libro, y diciendo que la senial no la levanta
y con que cifra.

NO fusiona nada, NO emite veredicto en bitacora/VEREDICTOS.jsonl y NO toca el nodo del
grafo. Comprueba por ASERCION lo mismo que la TAREA 3.
"""
import json, pathlib

BASE = pathlib.Path("cuarentena/grove_high_output")
FICHA = BASE / "cubrir_indicadores_problemas_reunion_individual.json"
MARCA = "FRONTERA DECLARADA EN LA VUELTA 52 CONTRA UN NODO DEL GRAFO"

BLOQUE = (
    " %s, POR CORRECCION DECLARADA Y SIN BORRAR NADA DE LO DE ARRIBA (manual principio 6). "
    "ES EL PAGO DE d052, ADJUDICADO POR EL AUDITOR EN LA ACTA 50 SECCION 50.5.b CON LA VARA 6.1: "
    "dos doctrinas legitimas no son duplicado, son FRONTERA DECLARADA, y se escriben las dos posiciones con sus fuentes en vez de fundirlas. "
    "EL OTRO NODO ES dirigir_reunion_individual_semanal, QUE YA VIVE EN dataset/nodos.jsonl y viene del libro zhuo_manager. "
    "LAS DOS POSICIONES, CON SUS DOS PASOS IMPRESOS DE SUS DOS FICHEROS Y NO DE MEMORIA: "
    "LA DE ESTA FICHA, que sale de fuentes/grove_high_output/cap_05.md L43, es su paso 1: "
    "Empieza por las cifras de rendimiento, o sea los indicadores que usa el subordinado, como los ritmos de pedidos entrantes, la produccion o el estado de los proyectos. "
    "LA DEL NODO DEL GRAFO, que sale de zhuo_manager, es su paso 4: "
    "Centrala en tu persona a cargo y en lo que la ayudaria a tener mas exito, no en ti y en lo que tu necesitas. Si lo que buscas es un parte de situacion, usa otro canal. "
    "EN QUE SE CONTRADICEN, DICHO SIN SUAVIZARLO: los dos mandan cosas contrarias sobre CON QUE SE EMPIEZA LA MISMA REUNION. "
    "Grove manda abrir por los indicadores y el estado de los proyectos, que es exactamente lo que el otro libro llama parte de situacion y manda sacar de esta reunion y llevar a otro canal. "
    "NO ES UN DUPLICADO Y NO SE FUNDE: son dos doctrinas de dos casas distintas sobre el mismo acto, cada una con su fuente y su fecha, y la vara 6.1 manda dejarlas las dos escritas. "
    "Y NO ES CAIDA DE NADIE: asi lo adjudico el auditor, y asi queda registrado aqui. "
    "QUE MIDE LA MAQUINA DE ESTA CASA ENTRE LAS DOS, Y ES EL MOTIVO POR EL QUE ESTO SE ESCRIBE A MANO: la senial 1 las deja en 0,1125 con el umbral en 0,35, "
    "asi que NINGUNA SENIAL VA A LEVANTAR ESTE PAR NUNCA, ni el dia de la insercion ni despues. "
    "Y en la misma tanda de la vuelta 51 dos pares de HERMANOS midieron 0,5501 y 0,5298: la maquina ordena por como esta escrito el texto, no por lo que el texto manda hacer, "
    "que es EXTRACTOR.md 11 con cifras de esta casa (las seniales ordenan, nunca deciden) y es D.19 (la jerarquia la busca la lectura). "
    "POR QUE ME TOCA A MI Y NO A LA ADUANA: la aduana compara mi candidato con el grafo y consigo mismo, y no tiene los dos libros delante. "
    "Esta contradiccion la encontro el auditor leyendo los dos pasos, no siguiendo una senial, y por eso la sede de la frontera es la ficha que viaja. "
    "LO QUE ESTO NO HACE, dicho por su nombre: no fusiona los dos nodos, no emite veredicto en bitacora/VEREDICTOS.jsonl (su puerta la cierra D.39 y hoy mide CERRADA para este libro), "
    "no toca el nodo del grafo ni una letra, y no abre doctrina (D.56, la cola sigue congelada en 11). "
    "EL DIA DE LA INSERCION SE CABLEA CON LOS DOS TEXTOS DELANTE, como arista D.29 de PARIENTE POR CONTRASTE, y esta frontera es lo que hace que ese dia no haya que volver a leer los dos libros. "
    "Y DIGO LO QUE ESTA FICHA HIZO MAL EN LA VUELTA 51, porque el auditor lo midio: de las cuatro fichas del uno a uno, esta era LA UNICA que no nombraba a ese vecino "
    "(.v51aud/11_quien_nombra_a_quien.py da dirigir_reun:0 para ella), mientras las otras tres declararon arista de contraste contra zhuo_manager sin que ninguna senial se lo pidiera. "
    "Hoy lo nombra, y lo nombra con la contradiccion escrita entera."
) % MARCA


def main():
    antes_raw = FICHA.read_text(encoding="utf-8")
    d = json.loads(antes_raw)
    viejo = d["resumen_teorico"]
    assert MARCA not in viejo, "ya pagada"
    d["resumen_teorico"] = viejo + BLOQUE

    a = json.loads(antes_raw)
    b = dict(d)
    assert b["resumen_teorico"].startswith(viejo), "no es prefijo"
    claves = [k for k in set(a) | set(b) if a.get(k) != b.get(k)]
    assert claves == ["resumen_teorico"], "cambia mas que el resumen: %s" % claves
    assert a["pasos_accionables"] == b["pasos_accionables"], "pasos movidos"
    assert a["titulo"] == b["titulo"], "titulo movido"
    assert a.get("atribuciones") == b.get("atribuciones"), "atribuciones movidas"

    FICHA.write_text(json.dumps(d, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("    ficha                                   : %s" % d["id"])
    print("    resumen_teorico antes                   : %d caracteres" % len(viejo))
    print("    resumen_teorico despues                 : %d caracteres" % len(d["resumen_teorico"]))
    print("    veces que nombra dirigir_reunion_individual_semanal, antes y despues: %d y %d"
          % (viejo.count("dirigir_reunion_individual_semanal"),
             d["resumen_teorico"].count("dirigir_reunion_individual_semanal")))
    print("    ASERCION: solo cambia resumen_teorico, el viejo es PREFIJO del nuevo,")
    print("              pasos, titulo y atribuciones identicos. PASO.")
    print("    dataset/nodos.jsonl y bitacora/VEREDICTOS.jsonl: NO SE TOCAN por este guion.")


if __name__ == "__main__":
    main()
