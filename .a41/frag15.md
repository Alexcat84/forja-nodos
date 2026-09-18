### 1.5. **LA SUITE DE ACEPTACION SALE EN ROJO, Y LOS CUATRO ROJOS SON DE MI FASE Y NO DE LA VUELTA**

**LA CORRO ENTERA Y PEGO SU CIERRE:**

    $ python tests/test_aceptacion.py
    $ tail -4 .a41/aceptacion.txt
      D.55, la deuda no bloquea la produccion: 11 pruebas mas
    
      total: 305 pruebas, 3 fallos, 1 errores
    ========================================================================

    $ grep -E "^(FAIL|ERROR):" .a41/aceptacion.txt
    ERROR: test_el_reporte_vivo_pasa_su_propia_guarda (__main__.PruebaTablaDeCierre.test_el_reporte_vivo_pasa_su_propia_guarda)
    FAIL: test_caso_positivo_un_frente_recien_nacido_hereda_cero (__main__.PruebaHerenciaPorLinea.test_caso_positivo_un_frente_recien_nacido_hereda_cero)
    FAIL: test_el_aviso_nombra_la_linea_y_su_registro (__main__.PruebaHerenciaPorLinea.test_el_aviso_nombra_la_linea_y_su_registro)
    FAIL: test_la_linea_serial_del_repo_tiene_su_registro_escrito (__main__.PruebaHerenciaPorLinea.test_la_linea_serial_del_repo_tiene_su_registro_escrito)

**NO SUPONGO LA CAUSA: SE LA SACO A LOS DOS QUE LA ESCRIBEN, y la pego literal.**

    $ sed -n "487,490p" .a41/aceptacion.txt
      File "C:\Users\AlexDesk\Documents\forja-nodos\src\comun.py", line 80, in leer_texto
        with io.open(ruta, "r", encoding="utf-8") as f:
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    FileNotFoundError: [Errno 2] No such file or directory: 'C:\\Users\\AlexDesk\\Documents\\forja-nodos\\docs\\loop\\REPORTE.md'

    $ sed -n "533,535p" .a41/aceptacion.txt
      File "C:\Users\AlexDesk\Documents\forja-nodos\tests\test_aceptacion.py", line 4581, in test_la_linea_serial_del_repo_tiene_su_registro_escrito
        self.assertTrue(credito.nacida(credito.LINEA_SERIAL),
    AssertionError: False is not true : docs/loop/CREDITO_serial.jsonl sin tandas: la migracion de D.48 no esta en el arbol

> **`LECTURA`, y separo lo que MIDO de lo que DEDUZCO:**
>
> **LO QUE EL INSTRUMENTO DICE:** el `ERROR` cae por `docs/loop/REPORTE.md`, que es **uno de
> los cuatro que `D.34.2` retira para mi fase ciega**; y el tercer `FAIL` cae por
> `docs/loop/CREDITO_serial.jsonl`, que es el fichero de `1.4` que tampoco esta. **Esos dos los
> causa mi propia fase, y su mensaje de error nombra el fichero.**
>
> **LO QUE DEDUZCO Y NO MIDO:** los otros dos `FAIL` son de la misma clase,
> `PruebaHerenciaPorLinea`, cuyo asunto entero es **ese mismo registro por linea**, y por eso
> los atribuyo a la misma causa. **Pero su mensaje NO nombra el fichero**, asi que va como
> deduccion y no como medida.
>
> **LO QUE NO PUEDO DECIR, Y NO LO DIGO:** **no puedo certificar que la suite estuviera verde
> para la vuelta.** Para saberlo habria que correrla con los cuatro ficheros en el arbol, y eso
> es exactamente lo que mi fase no puede hacer. **Queda para el acta, con el reporte delante.**
>
> **EL PRECEDENTE ESTA ESCRITO Y ES MIO:** la `ACTA 40` `1.1` dejo dicho *el siguiente auditor
> que clone un hash va a ver once rojos y va a creer que ha encontrado algo*. **Hoy son cuatro
> y por otra puerta, y por eso lo vuelvo a dejar escrito.**

---

