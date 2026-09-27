# PARADA DEL 12 SEP 2026: **FALSO POSITIVO DE `D.40`**

> ## DICTAMEN: **LA GUARDA ERA MAS ESTRICTA QUE LA LETRA. LA APERTURA ESTABA BIEN.**
>
> **LO QUE LA APERTURA DE LA VUELTA 19 ESCRIBIO** (`APERTURA_CIEGA.md` L18 y L23):
>
>     > ### **ACTA ANTERIOR LEIDA: `80fd74cdf15bb0b1ff02bcbe560ba03f11f22472`**
>     ### `HEREDADO 1`: **CUMPLIDO**
>
> **LA HUELLA ES LA BUENA AL DIGITO**, remedida hoy:
>
>     $ git hash-object docs/loop/ACTA_AUDITOR.md
>       80fd74cdf15bb0b1ff02bcbe560ba03f11f22472
>
> **EL AUDITOR LEYO EL ACTA, REMIDIO LA HUELLA Y DECLARO EL REMEDIO. Lo que fallo fue mi
> comprobador**, que buscaba esas dos lineas **desnudas** y no las reconocia dentro del
> markdown con el que esta casa escribe absolutamente todo.
>
> **Y LA MITAD QUE YA ESTABA ROTA UNA VUELTA ANTES:** el remedio de la `ACTA 16` 7.3 pedia
> `grep -c "ACTA ANTERIOR LEIDA" -> 1`, **y la propia apertura de la vuelta 18 midio 2 y lo
> dijo en voz alta** (*`-> 2 (mi remedio pide 1)`*). Una apertura que declara arriba y lo
> repite en su tabla de cierre **cita la linea que declara**: **un conteo exacto castiga a
> quien declara de mas.**
>
> ### QUE SE HIZO, Y NO SE TOCO NI UNA LINEA DE LA APERTURA
>
> 1. **El comprobador verifica PRESENCIA y no conteo** (`src/herencia.py`): se quita el
>    adorno de markdown antes de buscar, y **basta con que UNA de las veces que aparece la
>    declaracion este bien puesta.**
> 2. **Caso positivo, porque aflojar formato no es aflojar exigencia:** una apertura sin
>    declaracion **sigue cayendo** por bien maquetada que este, y **una huella ajena
>    decorada tampoco cuela.**
> 3. **Caso negativo:** la apertura real de la vuelta 19 pasa, la que cita su declaracion
>    dos veces pasa, y una huella corta sigue siendo la misma huella. **13 pruebas en
>    `PruebaHerencia`**, y **el banco del arnes escribe ahora sus lineas en el markdown de
>    la casa**, que es la forma exacta en que fallo.
> 4. **Retirada por correccion declarada la clausula de conteo del remedio de la `ACTA 16`
>    7.3**, anotada en `D.40` del banco. **No se borra de su acta**, que es sede del
>    auditor: se declara que esa mitad ya no rige.
> 5. **Arreglado un defecto mio de este mismo escritor:** la linea de estado salia con
>    `$(git rev-parse ...)` sin expandir, y por eso el cuerpo de abajo lo muestra en crudo.
>    **El cuerpo no se toca**, que es la costumbre de esta carpeta.
>
> ### LO QUE ESTA PARADA **NO** DICE
>
> **No dice que `D.40` sobre.** El arnes entrego la herencia, el auditor la declaro y la
> declaracion se pudo comprobar: **eso es la regla funcionando.** Lo que fallo fue la vara
> con la que se leyo la declaracion, **y una vara que tumba a quien cumple hace justo el
> dano que `D.40` vino a evitar**, porque enseña a escribir para la guarda en vez de para
> el que lee.
>
> **Y NO HAY RACHA QUE MOVER.** Esto no es `REMEDIO ROTO` ni `CIFRA PUBLICADA PROPIA`: el
> auditor cumplio. **La falta es del instrumento, y el instrumento es mio.**

> **ARCHIVADA.** Este fichero fue `docs/loop/PARA_ALEXIS.md` hasta que se dictamino lo que
> pedia. **Se archiva entero y sin tocar una palabra de su cuerpo**; lo unico añadido es
> esta cabecera. El arnes solo mira `docs/loop/PARA_ALEXIS.md`, asi que el bucle ya no esta
> detenido por el.
>
> **LO QUE FALTA DE LA VUELTA 19 ES SU ACTA.** El extractor cerro su vuelta y
> `PROMPT_SIGUIENTE.md` queda **intacto**: no se reencarga nada, porque nada de lo
> encargado quedo sin hacer.

---

# PARA_ALEXIS: la apertura ciega no declaro lo que heredaba

La vuelta 2 entrego al auditor los remedios que el acta anterior dejo escritos
(D.40), y su apertura ciega no los declaro. **El arnes se detuvo ANTES de que se
escribiera el acta.**

Lo que falta:

APERTURA CIEGA INCOMPLETA: 2 cosa(s) que faltan (D.40).
  la linea 'ACTA ANTERIOR LEIDA' esta, pero con otra huella: se espera '80fd74cdf15bb0b1ff02bcbe560ba03f11f22472'
  falta la linea 'HEREDADO 1: CUMPLIDO' o 'NO APLICA' (heredado 1 de 1)

QUE SIGNIFICA. D.40 existe porque tres actas seguidas perdieron el mismo remedio
por tener que ir a buscarlo. El arnes ya lo entrega en el prompt: lo unico que se
pide es declarar que se leyo el acta, por su huella, y que se hizo con cada
remedio heredado. Un remedio entregado y no declarado es un remedio perdido.

QUE NO SIGNIFICA. No dice que el trabajo este mal, ni que la clasificacion sea
falsa. Dice que la vuelta no puede certificar que la herencia se recogio.

Estado: rama extraccion-mundo-11, hash $(git rev-parse --short HEAD 2>/dev/null || echo desconocido).

Como retomar: borra este fichero y relanza. El auditor recibira la misma herencia
y esta vez tiene que declararla.
