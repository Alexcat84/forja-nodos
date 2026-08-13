# EJECUTOR.md, reglas permanentes del ejecutor del bucle

Anclaje: MANUAL_SISTEMA_DE_CONOCIMIENTO seccion 8 (escalado autonomo). Este
documento es la copia adaptada del protocolo de la casa que destilo el manual,
generalizado a esta forja: donde alli se hablaba de una campaña de saneo de un
grafo existente, aqui se habla de la extraccion de un libro hacia un grafo que
nace limpio.

Eres la sesion ejecutora de la forja. Cada vuelta del bucle te da un encargo en
docs/loop/PROMPT_SIGUIENTE.md. Estas reglas valen SIEMPRE, ademas de lo que
diga el encargo.

1. Commitea lo pendiente en la rama activa ANTES de tocar nada.

2. MODO DE CIERRE mientras la fase sea de LECTURA (extraccion de candidatos,
   medicion de señales, censos): se lee, se mide y se documenta; CERO
   reparaciones de nodos ya insertados. Los nodos existentes solo se tocan
   cuando el encargo diga explicitamente que se entro en fase de EJECUCION de
   operaciones, y entonces solo en la rama que el encargo indique.

3. Doctrinas tal como estan escritas: docs/MANUAL_SISTEMA_DE_CONOCIMIENTO.md
   (principios 1 a 10 y secciones 2 a 7), docs/REGLAS_DE_ID.md y
   docs/FLUJO_DE_EXTRACCION.md. Las reglas se citan por seccion; no se inventan.
   Si un candidato o una operacion pide una regla que no existe: NO pares,
   registra lo mejor sostenido, marcalo PENDIENTE DE DOCTRINA en su razon, y
   sigue. Paras SOLO si algo contradice una regla vigente o una cifra publicada
   con su corte: en ese caso lo escribes en el reporte como PARADA y no lo
   arreglas tu.

4. COMMIT POR TRAMO (un capitulo, o una operacion de fusion completa), para que
   nada dependa de que la sesion aguante. Los hallazgos que no pueden esperar
   van al mensaje del commit.

5. NINGUN NODO ENTRA SIN LA ADUANA. Se inserta con
   `python forja.py insertar candidato.json`, un candidato por vez. No existe
   la carga masiva: una carga masiva es un veredicto que nadie escribio. Si la
   aduana bloquea, LEES a los vecinos antes de escribir el veredicto: las
   señales ordenan, nunca deciden (principio 4).

6. Todo veredicto lleva su razon escrita y queda en bitacora/VEREDICTOS.jsonl.
   La razon escrita es el activo mas reutilizable del sistema entero. Un
   veredicto SANO sin razon es un nodo que entro por cansancio.

7. Reportes SOLO en checkpoints (por capitulo en la extraccion; por operacion
   en la ejecucion). El reporte completo va en docs/loop/REPORTE.md
   (sobrescribe el anterior) con: hash final, rutas tocadas, cuenta de nodos
   recomputada DEL ARCHIVO (nunca de memoria), veredictos por clase, censos
   ampliados, correcciones declaradas, PENDIENTES DE DOCTRINA, y LOS
   DISCUTIBLES MARCADOS para la relectura ciega del auditor (marcados ANTES de
   saber si aciertas).

8. Toda cifra con su fecha de corte; toda glosa con el corte de la cifra que
   interpreta; toda correccion declarada sin borrar el texto viejo ("una
   correccion que tapa lo que corrige no se puede auditar"); toda cifra de un
   autor con su atribucion, en el campo `atribuciones` y en su censo.

9. Todo conteo que toque ids pasa por src/resolutor.py antes de contar
   (principio 3). Toda perdida de catalogo declarada se re-verifica contra el
   grafo, sin importar quien la declare: una busqueda negativa no se puede
   citar.

10. Cero guiones largos y cero guiones medios en todo lo que escribas. Deja
    correr el hook; si falla, corriges y reintentas, jamas lo saltas.

11. Ninguna fusion se escribe sin plantillas/OPERACION_DE_FUSION.md rellena
    entera: las seis perdidas repartidas, el control de denominacion por
    separado (nombre largo, sigla e idioma son TRES comprobaciones), la
    simulacion sobre copia en memoria y el caso positivo corrido en rojo antes
    de arreglarlo.

12. No adivines. Lo que no este escrito y no puedas medir, lo traes como
    pregunta en el reporte.
