
**`PASOS INVENTADOS`: `cap_05` `0` de `84` y `cap_06` `0` de `62`, el `0,0` por ciento los dos.** Ningun PUENTE, asi que
**ninguna ficha de la bandeja se corrigio** y el barrido corre sobre las fichas tal como estaban en `d8f4e2a` (`d031`). Si
caen como `P` todos los pasos de `D68.3` a `D68.6`, `cap_05` sale `5` de `84` (`D68.3` uno, `D68.4` uno, `D68.5` tres), el
`6,0`, y `cap_06` `4` de `62` (`D68.3` dos, `D68.4` uno, `D68.6` uno), el `6,5`: los dos bajo el `10`.

**Las `146` citas, localizadas por instrumento** (`D.35`): `.v68ext/citas.sh`, copia de `.v66ext/citas.sh` con tres
cambios dichos en su cabecera (la ruta, el capitulo de cada fila leido de su ficha, y el corte en el primer `? ` con
mayuscula). Salida entera en `.v68ext/citas_fidelidad.txt`; su ultima linea y las de los discutibles:

    $ bash .v68ext/citas.sh | tail -1
    filas: 146 | en su linea declarada: 146 | fuera: 0
    $ grep -n -o -F 'how do you decide how often somebody needs such a meeting' fuentes/grove_high_output/cap_05.md    # fijar_frecuencia_reunion_individual_madurez_tarea paso 1
    33:how do you decide how often somebody needs such a meeting
    $ grep -n -o -F 'Since I take notes in outline form, I am forced to categorize the info' fuentes/grove_high_output/cap_05.md    # tomar_notas_copia_guion_reunion_individual paso 4
    49:Since I take notes in outline form, I am forced to categorize the info
    $ grep -n -o -F 'Is he satisfied with his own performance' fuentes/grove_high_output/cap_05.md    # alentar_asuntos_corazon_vigilar_final_reunion paso 3
    53:Is he satisfied with his own performance
    $ grep -n -o -F 'All a manager can expect is that the commitment to support is honestly' fuentes/grove_high_output/cap_06.md    # conducir_etapas_modelo_ideal_decision paso 12
    29:All a manager can expect is that the commitment to support is honestly
    $ grep -n -o -F 'For experience, we at Intel are likely to ask a person in management s' fuentes/grove_high_output/cap_06.md    # decidir_nivel_competente_inferior paso 7
    33:For experience, we at Intel are likely to ask a person in management s
    $ grep -n -o -F 'And everyone in your operation should be made to understand this' fuentes/grove_high_output/cap_06.md    # vencer_sindrome_grupo_pares_autoconfianza paso 5
    49:And everyone in your operation should be made to understand this
    $ grep -n -o -F 'one can always ask the senior person present to assume control' fuentes/grove_high_output/cap_06.md    # tomar_mando_reunion_pares_presidente_ausente paso 3
    51:one can always ask the senior person present to assume control
