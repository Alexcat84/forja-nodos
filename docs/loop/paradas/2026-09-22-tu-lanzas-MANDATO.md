# MANDATO DEL FUNDADOR, 22 SEP 2026: **TU LANZAS, TU VIGILAS, TU DECIDES LO TUYO**

*No es la respuesta a una parada: es una **delegacion permanente** a la sesion de chat, y
por eso va archivada aparte. **Todo reinicio de racha que la sesion haga por delegacion
cita este fichero**, porque `AUDITOR_FORJA.md` `5.4` exige que la decision que reinicia
viva en `docs/loop/paradas/`, y la delegacion es la decision.*

---

## EL MANDATO, LITERAL

> SESION DE CHAT en forja-nodos. Commitea y pushea lo pendiente en la
> rama activa antes de tocar nada. MANDATO DEL FUNDADOR (22 sep 2026):
> TU LANZAS, TU VIGILAS, TU DECIDES LO TUYO. Aplica primero la decision
> del 22 sep (fusion de gerber, reinicio de la racha de marquet, las doce
> filas a DEUDA, modelos nuevos) y despues:
>
> 1. LANZA LAS DOS LINEAS en segundo plano, cada una con su log propio:
>    cd /c/Users/AlexDesk/Documents/forja-nodos && git checkout
>    extraccion-mundo-11 && nohup env RAMA=extraccion-mundo-11
>    MODO_INSERCION=insertar MODELO_EXTRACTOR=claude-opus-5-5
>    MODELO_AUDITOR=claude-opus-5-5 MAX_VUELTAS=20 bash
>    orquestador_forja.sh > /tmp/serial.log 2>&1 &
>    cd /c/Users/AlexDesk/Documents/forja-marquet_turn_the_ship && nohup
>    env RAMA=extraccion-marquet_turn_the_ship MODO_INSERCION=cuarentena
>    MODELO_EXTRACTOR=claude-sonnet-5 MODELO_AUDITOR=claude-opus-5-5
>    MAX_VUELTAS=20 bash orquestador_forja.sh > /tmp/marquet.log 2>&1 &
>    Antes, fija el esfuerzo: ALTO en los dos asientos de la serial, por
>    defecto en el frente. Si fijarlo exige tocar el arnes, es ARNES:
>    hazlo con su prueba.
> 2. VIGILA: revisa las dos lineas al menos cada hora (proceso vivo,
>    ultima linea del log, PARA_ALEXIS de cada arbol). Cuando una pare,
>    aplica el guion de reanudacion y RELANZA TU MISMO en estos casos:
>    (a) ARNES: arreglalo con caso positivo y negativo, dictamen en
>        paradas/, relanza.
>    (b) CREDITO: tienes DELEGACION DEL FUNDADOR para reiniciar una racha
>        cuando se cumplan las dos condiciones: la especie ya tiene cura
>        mecanica instalada (o la instalas tu con su caso positivo), y las
>        cuatro guardas de dato estan verdes. Escribe el reinicio en
>        paradas/ como DECISION DELEGADA, con su motivo, y relanza. Si la
>        especie no tiene cura mecanica posible, sube.
>    (c) FIN DE CUOTA: el arnes espera solo; avisame con la hora, porque
>        el fundador tiene un reinicio de reserva y decide si lo gasta.
>    (d) MARQUET CIERRA SU EXTRACCION: cosechalo tu (una fusion, gate y
>        suite, TABLERO), y la serial lo inserta como septimo al acabar
>        Gerber.
> 3. SUBE SOLO LO CRITICO, y para esa linea (la otra sigue): DOCTRINA
>    nueva que ninguna regla responde; una guarda de DATO en rojo que no
>    puedes reparar (gate, cerrojo, censo no decreciente, fidelidad con
>    puente) o cualquier perdida de nodo; conflicto de fusion dentro de
>    dataset/, bitacora/ o censos/; un turno por encima de 25 USD dos
>    veces seguidas; cualquier cambio de alcance (abrir o soltar un
>    libro). Todo lo demas es tuyo.
> 4. CADA REPORTE que me mandes abre con una linea: SIN NOVEDAD, o la
>    especie y lo que hiciste, o NECESITO AL FUNDADOR y por que.

---

## LO QUE ESTE MANDATO CAMBIA, Y LO QUE NO

| | antes | **con este mandato** |
|---|---|---|
| lanzar y relanzar | el fundador | **la sesion**, en los casos `2.a` a `2.d` |
| reiniciar una racha | solo el fundador (`5.4`) | **la sesion tambien, con DOS condiciones a la vez**: cura mecanica instalada **y** las cuatro guardas de dato en verde. Sin las dos, sube |
| cosechar un frente | el fundador (`D.50` paso `b`) | **la sesion, para Marquet** (`2.d`). Para cualquier otro frente, sigue siendo del fundador |
| abrir o soltar un libro | el fundador | **el fundador. No cambia** (`3`) |

> **LO QUE NO SE DELEGA, Y CONVIENE TENERLO DELANTE CADA VEZ:** `AUDITOR_FORJA.md` `5.4`
> sigue diciendo que *un auditor que pone su propia racha a cero se esta absolviendo*. **El
> bucle no reinicia nada.** Quien reinicia por delegacion es la sesion de chat, que no
> escribe ni el reporte ni el acta de la vuelta que reinicia, y **lo hace por escrito, en
> `paradas/`, con el motivo y las dos condiciones medidas delante.**

### Las dos condiciones de `2.b`, en forma de comprobacion

Un reinicio delegado **solo se escribe si las dos salen verdes, y el fichero pega su salida**:

1. **la especie tiene cura mecanica instalada**: una guarda en `src/` o `scripts/`, con su caso
   positivo en `tests/`, que impide escribir otra vez la figura que cayo. Si no existe y se
   puede instalar, se instala primero, con su caso positivo, y despues se reinicia.
2. **las cuatro guardas de dato de `D.55` en verde**: `gate`, `cerrojo`, `censo_no_decrece`
   y `fidelidad`.

### Los cinco casos que se suben, y para esa linea sola

`DOCTRINA` nueva sin regla que la responda; una guarda de DATO en rojo que no se pueda reparar,
o cualquier perdida de nodo; conflicto de fusion dentro de `dataset/`, `bitacora/` o
`censos/`; **un turno por encima de `25` USD dos veces seguidas**; y cualquier cambio de
alcance. **La otra linea sigue.**
