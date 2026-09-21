# ENCARGO DE LA VUELTA 2 DEL FRENTE `gerber_emyth`: **REANUDAR**, cerrando el hueco entre `cap_04` y `cap_07`

*Linea **`gerber_emyth`** (`extraccion-gerber_emyth`, worktree
`C:/Users/AlexDesk/Documents/forja-gerber_emyth`). **Escrito por la sesion de chat del 21 sep
2026**, no por un auditor, al aplicar el punto `3` de la decision del fundador de ese dia.*

> # **LIBRO DE ESTA VUELTA: `gerber_emyth`**
> # **CLASE DE ESTA VUELTA: EXTRACCION**

**Commitea y pushea lo pendiente en la rama activa antes de tocar nada.**

---

## 0. LO PRIMERO: **ESTE FRENTE ESTUVO CUATRO DIAS PARADO Y ACABA DE RECIBIR CUATRO DIAS DE MAQUINARIA**

**Tu vuelta `1` fue el `17` sep y paro por doctrina.** Sus dos motivos estan **resueltos**, y
su archivo esta en `docs/loop/paradas/2026-09-17-gerber-la-racha-y-la-linea-vieja-RESUELTA.md`.
**Leelo antes de empezar**, porque el segundo te afecta directamente:

| lo que tu vuelta `1` levanto | como quedo |
|---|---|
| de quien es la racha con varias sesiones | **`D.48`**: cada linea lleva la suya, y la tuya vive en `docs/loop/CREDITO_gerber_emyth.jsonl` |
| la linea del arnes que `D.43` dejo vieja | **ARREGLADA el 21 sep.** Ya no te manda correr el informe del lote entero en tu turno |

> ### **NO LANCES EL INFORME DEL LOTE ENTERO. Te costo una hora el `17` sep y no termino.**
>
> `D.43` lo saca del turno **porque no cabe**: mas de tres horas para `83` candidatos. Lo
> corre el arnes. **Lo que si corres, y en el mismo acto en que escribes cada ficha, es el
> informe DE ESE CANDIDATO**, que es barato.

**Y DE LO QUE ACABA DE LLEGAR A TU ARBOL, tres cosas cambian como trabajas:**

- **`D.58`, regimen ligero: la fase ciega esta APAGADA en `cuarentena`.** Tu turno del
  auditor es directo y corto. **El techo del regimen ligero son TRES capitulos por vuelta.**
- **`D.59`: toda media, porcentaje o razon que publiques la imprime un instrumento**, con su
  numerador y su denominador nombrados. Una cifra derivada a mano de dos celdas **no se
  publica**, y hay una guarda que corre en cada commit.
- **`D.60`, nueva hoy: un mundo se cierra cuando sus libros estan INSERTADOS, no
  extraidos.** Te toca de refilon y conviene que lo sepas: **si cierras tu extraccion antes
  de que se agote la cuota de la semana, entras al mundo `11` como sexto libro** por el
  relevo `D.50`. Si no, tu bandeja queda entera y **no bloquea nada**.

---

## 1. POR QUE ESTE FRENTE ES LA UNICA LINEA VIVA ESTA SEMANA

**La serial esta PARADA a proposito.** La extraccion del mundo `11` se consumo el `21` sep
(`grove_high_output`, `18` de `18` capitulos, `92` candidatos), y **la insercion de Grove se
pospuso a la semana siguiente por limite de cuota**, por enmienda del fundador del mismo dia.

**Eso significa dos cosas para ti:**

1. **Toda la cuota de la semana es tuya.** No compites con una insercion.
2. **Nadie va a insertar mientras corres**, asi que el grafo se queda en `346` nodos y **la
   poblacion de tu aduana no se mueve por debajo de ti.**

**Y LO QUE NO CAMBIA: TU NO INSERTAS NUNCA.** `MODO_INSERCION=cuarentena`, y si alguien
escribe `insertar` en este arbol **el arnes se detiene antes de gastar un turno**
(`PARALELO.md` `3.2`, con su caso positivo y su negativo en `tests/prueba_arnes.sh`).

---

## 2. TU ESTADO, MEDIDO Y NO RECORDADO

    $ python forja.py tablero --puedo gerber_emyth
    LINEA 'gerber_emyth', LIBRO 'gerber_emyth': SI
      'gerber_emyth' ya es de esta linea ('gerber_emyth'): continuarlo es lo que toca.

    $ ls fuentes/gerber_emyth/ | wc -l
    22
    $ ls cuarentena/gerber_emyth/*.json | wc -l
    10

**Tus `10` candidatos, con el capitulo del que salieron:**

    construir_empresa_plantilla_vision_diaria                cap_08
    dar_valor_constante_cuatro_publicos                      cap_11
    dictar_ritmo_crecimiento_preguntas_escritas              cap_07
    documentar_trabajo_manual_operaciones                    cap_11
    fingir_prototipo_cinco_mil_replicas                      cap_11
    hacer_trabajo_futuro_imaginar_negocio                    cap_04
    interrogar_negocio_cinco_preguntas                       cap_11
    operar_modelo_gente_destreza_minima                      cap_11
    trazar_modelo_negocio_cliente_primero                    cap_08
    unificar_color_forma_vestuario_modelo                    cap_11

**MINADOS: `cap_04`, `cap_07`, `cap_08`, `cap_11`. Cuatro de `22`.**

---

## 3. LA TAREA: **`cap_05` Y `cap_06`, Y SON DOS Y NO TRES A PROPOSITO**

**El fundador escribio *continua desde el `cap_05` con la frontera heredada*, y eso es lo que
haces.**

**POR QUE ESOS DOS Y NO OTROS:** `cap_05` y `cap_06` son **exactamente el hueco entre dos
capitulos que ya minaste**, `cap_04` y `cap_07`. **Tienes frontera conocida y verificable a
los dos lados**, que es la situacion mas barata de auditar que este libro te puede dar hoy.

**POR QUE DOS Y NO LOS TRES QUE `D.58` PERMITE:** es tu primera vuelta despues de cuatro dias
parado **y con cuatro dias de maquinaria recien fusionada en tu arbol**. Una vuelta corta que
sale limpia vale mas que una larga que hay que repetir. **Si esta sale limpia, la siguiente
sube a tres.**

### 3.1. Lo que entregas por cada capitulo

1. **LA FRONTERA, fila a fila contra el fichero**, con sus numeros de linea, sus palabras, y
   **cero solapes y cero lineas sin cubrir**. Se comprueba al digito, asi que no la estimes.
2. **Los candidatos que el capitulo de**, en `cuarentena/gerber_emyth/<id>.json`, **cada uno
   con su `python forja.py informe` corrido en el mismo acto en que lo escribes.**
3. **`PASOS INVENTADOS POR CAPITULO`, UNA FILA POR CAPITULO Y NO UNA MEDIA**
   (`AUDITOR_FORJA.md` `8`). **Si un capitulo da CERO candidatos, la fila se escribe igual**
   y dice `SIN SUPERFICIE`: **un cero es una medida, no un silencio.**
4. **La muestra de fidelidad con la semilla de esta vuelta:**

       python scripts/muestra_fidelidad.py --libro gerber_emyth --capitulos cap_05,cap_06 --semilla g2

### 3.2. **UN CAPITULO QUE DA CERO SE CIERRA IGUAL, Y ESTO ES NUEVO PARA TI**

**Lo acaba de demostrar la serial y te ahorra una parada.** Grove cerro con `3` de sus `18`
capitulos en cero, **y los tres estan firmados**: `cap_08` y `cap_09` releidos ENTEROS,
`cap_18` con sus `35` citas de nodo comprobadas una a una.

> **Un capitulo vacio no se puede comprobar por muestra: no hay pasos que muestrear.** La
> unica verificacion posible es **leerlo entero y decir contra que se leyo.** Si `cap_05` o
> `cap_06` no dan nodo, **eso no es un fallo tuyo: es un resultado**, y se firma leyendo.

El cierre entero de Grove esta en `docs/CIERRE_LOTE_7_GROVE.md` si quieres ver como se hizo.

---

## 4. LO QUE NO HACES EN ESTA VUELTA, Y NO ES NEGOCIABLE

- **NO INSERTAS.** Ni un nodo. `MODO_INSERCION=cuarentena`.
- **NO TOCAS EL ARNES NI LA MAQUINARIA.** `D.45`, **moratoria total en el frente**:
  `orquestador_forja.sh`, `src/`, `scripts/`, `tests/`, `hooks/` y `esquema/` estan vedados.
  **Si encuentras un defecto, lo MIDES y lo SUBES en tu `PARA_ALEXIS`, no lo arreglas.** Tu
  vuelta `1` hizo exactamente eso y tenia razon las dos veces.
- **NO ESCRIBES DOCTRINA.** Moratoria total en el frente. Si una pregunta necesita regla
  nueva, es parada.
- **NO TOCAS `cap_01`, `cap_02` NI `cap_03`.** Siguen sin minar y **lo sabemos**: el
  fundador mando empezar en `cap_05`. **Anotalo en `docs/loop/DEUDA.jsonl`** como hueco
  conocido con esta cita, para que ningun auditor lo lea como desliz. **No es un blocante.**
- **NO LANZAS EL INFORME DEL LOTE ENTERO.** Ya dicho arriba, y es lo que te costo la vuelta
  `1`.

---

## 5. AL CERRAR

- **Escribe tu tanda**: `python forja.py credito --anotar`. **Tu racha es tuya y empieza en
  cero** (`D.48`). Una linea que no escribe su credito **nace de nuevo cada vuelta**, y eso
  no es una racha en cero: es una racha que no existe.
- **Commitea `docs/loop/` y tu carpeta de evidencia.**
- **Si nada te obliga a parar, NO escribas `PARA_ALEXIS.md`**, y deja el encargo de la vuelta
  siguiente en `docs/loop/PROMPT_SIGUIENTE.md`. **Mide las condiciones de parada una a una y
  publica que las mediste**, en vez de suponer que no se cumplen.
