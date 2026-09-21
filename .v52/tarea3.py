"""d051: saca el digito de senial de dentro del texto del que la senial se calcula.

Correccion declarada y sin borrar (manual principio 6): el bloque VEREDICTO de las
seis fichas de la vuelta 51 conserva la clase, el vecino nombrado, la razon y el par
emparejado; lo que se anade es la frase que dice de donde salio el digito y cuando,
nombrando el informe de aduana como sede de ese numero.

Comprueba por ASERCION que solo cambia resumen_teorico y que el texto viejo es
PREFIJO del nuevo, o revienta antes de guardar.
"""
import json, pathlib, re, sys

BASE = pathlib.Path("cuarentena/grove_high_output")

# de .v51/relojes.txt y comprobado con grep sobre cada informe
FICHAS = [
    ("infundir_regularidad_reunion_proceso", ".v51/aduana_c1.txt", "P6"),
    ("usar_tres_clases_reunion_proceso", ".v51/aduana_c2.txt", "P7"),
    ("fijar_frecuencia_reunion_individual_madurez_tarea", ".v51/aduana_c3.txt", "P11"),
    ("fijar_duracion_lugar_reunion_individual", ".v51/aduana_c4.txt", "P12"),
    ("preparar_guion_reunion_individual_subordinado", ".v51/aduana_c5.txt", "P13"),
    ("cubrir_indicadores_problemas_reunion_individual", ".v51/aduana_c6.txt", "P14"),
]

DIGITO = re.compile(r"levantado por similitud de texto (\d,\d{3})")


def bloque(idf, informe, pieza, digitos):
    con = (
        "LOS DIGITOS QUE ESTE BLOQUE ESCRIBE SON %s, Y CADA UNO ES LA MEDIDA DE AQUEL ACTO"
        % (", ".join(digitos))
        if digitos else
        "ESTE BLOQUE NO ESCRIBE NI UN DIGITO DE SENIAL, porque el informe de aquel acto no levanto ningun vecino"
    )
    return (
        " CORRECCION DECLARADA EN LA VUELTA 52, SIN BORRAR NI UNA LINEA DE LO DE ARRIBA (manual principio 6). "
        "ES EL PAGO DE d051, QUE EL AUDITOR DESENTERRO EN LA ACTA 50 SECCION 50.5.a Y ADJUDICO QUE NO ERA CAIDA DE NADIE. "
        "%s, medida por la aduana el 19 sep 2026 sobre la poblacion de aquel momento, y SU SEDE ES %s, "
        "que es el informe que la aduana imprimio en la pasada de esta misma ficha en la vuelta 51 (pieza %s). "
        "NO SON UNA MEDIDA VIVA DEL TEXTO DE HOY, y desde esta linea dejan de presentarse como tal. "
        "POR QUE NO PUEDEN SERLO, Y ESTA MEDIDO Y NO SUPUESTO: la senial 1 de esta casa compara titulo mas resumen mas pasos "
        "(src/aduana.py senal_similitud_texto sobre comun.texto_comparable), o sea que el resumen_teorico ENTRA en el texto que la senial mide; "
        "y este bloque VEREDICTO, que es el que escribe el digito, vive dentro de ese mismo resumen_teorico. "
        "Asi que escribir el digito aqui cambia el numero que el digito nombra. "
        "LA MEDIDA DE LO QUE ESO MUEVE, corrida por el auditor y por mi con el mismo instrumento (.v51/por_que_0445.py y .v51aud/44_crecimiento_ficha.py): "
        "el par mas alto de la tanda se publico en 0,445 y hoy da 0,550, y el corte del primer bloque VEREDICTO cae en el caracter 6705 y 7217 de las dos fichas, "
        "que es exactamente todo lo que esas fichas crecieron despues de medir. "
        "LA FRASE QUE LO RESUELVE LA ESCRIBI YO AL PAGAR d044 Y ME LA DEVUELVE EL AUDITOR: un comando escrito dentro de su propia poblacion no se arregla afinandolo, se arregla sacandolo. "
        "El digito es el mismo caso que el comando. "
        "QUE SE QUEDA Y QUE SE VA: se quedan la CLASE del veredicto, el VECINO nombrado, la RAZON entera y el PAR EMPAREJADO, que son lo que hace releible el veredicto y no dependen de ninguna cifra. "
        "Se va el digito COMO MEDIDA VIVA, y no se borra: queda arriba, escrito, y esta linea dice de que acto es y donde vive su informe. "
        "EL DIA DE LA INSERCION, el veredicto que llegue a bitacora/VEREDICTOS.jsonl llevara el digito QUE LA ADUANA MIDA EN ESE ACTO, no el de arriba, "
        "y la razon sera esta misma porque la razon no caduca. "
        "Y DESDE LA VUELTA 52 ESTO NO SE VUELVE A PAGAR: los veredictos que escribo hoy dentro de las fichas nuevas de cap_05 nombran su informe y no se llevan el numero dentro como si fuera de hoy."
        % (con, informe, pieza)
    )


def main():
    cambios = []
    for idf, informe, pieza in FICHAS:
        p = BASE / ("%s.json" % idf)
        antes_raw = p.read_text(encoding="utf-8")
        d = json.loads(antes_raw)
        viejo = d["resumen_teorico"]
        assert "CORRECCION DECLARADA EN LA VUELTA 52" not in viejo, "ya pagada: %s" % idf
        digitos = DIGITO.findall(viejo)
        d["resumen_teorico"] = viejo + bloque(idf, informe, pieza, digitos)

        # ASERCION: solo cambia resumen_teorico, y el viejo es PREFIJO del nuevo
        a = json.loads(antes_raw)
        b = dict(d)
        assert b["resumen_teorico"].startswith(viejo), "no es prefijo: %s" % idf
        claves = [k for k in set(a) | set(b) if a.get(k) != b.get(k)]
        assert claves == ["resumen_teorico"], "cambia mas que el resumen: %s %s" % (idf, claves)
        assert a["pasos_accionables"] == b["pasos_accionables"], "pasos movidos: %s" % idf
        assert a["titulo"] == b["titulo"], "titulo movido: %s" % idf
        assert a.get("atribuciones") == b.get("atribuciones"), "atribuciones movidas: %s" % idf

        p.write_text(json.dumps(d, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        cambios.append((idf, len(viejo), len(d["resumen_teorico"]), len(digitos), informe))

    print("    %-50s %9s %9s %8s  %s" % ("ficha", "antes", "despues", "digitos", "sede del digito"))
    for idf, a, b, n, inf in cambios:
        print("    %-50s %9d %9d %8d  %s" % (idf[:50], a, b, n, inf))
    print()
    print("    fichas corregidas                       : %d" % len(cambios))
    print("    digitos de senial que llevaban dentro   : %d" % sum(c[3] for c in cambios))
    print("    ASERCION: solo cambia resumen_teorico, el viejo es PREFIJO del nuevo,")
    print("              pasos, titulo y atribuciones identicos en las %d. TODAS PASARON." % len(cambios))


if __name__ == "__main__":
    main()
