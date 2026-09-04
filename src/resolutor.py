# -*- coding: utf-8 -*-
"""El resolutor de ids (manual principio 3: TODO ID PASA POR EL RESOLUTOR).

Ningun conteo, guarda o busqueda de este repo compara ids literales: se
resuelve primero (alias incluidos, caminando cadenas) y se compara despues.
Un chequeo literal inventa salud (auto-aristas invisibles) e inventa
enfermedad (aristas a deprecados que si resuelven).

Quien compare ids con == fuera de este modulo esta escribiendo un bug.
"""

from . import comun

LIMITE_CADENA = 32


class Resolutor(object):

    def __init__(self, nodos):
        self.nodos = list(nodos)
        self.canonicos = {}
        self.deprecados = set()
        self.mapa_alias = {}
        self.errores = []
        for nodo in self.nodos:
            identificador = nodo.get("id")
            if not isinstance(identificador, str) or not identificador:
                self.errores.append("hay un nodo sin id")
                continue
            if identificador in self.canonicos:
                self.errores.append("id canonico repetido en el dataset: %s" % identificador)
            self.canonicos[identificador] = nodo
            if nodo.get("estado") == "deprecado":
                self.deprecados.add(identificador)
        for nodo in self.nodos:
            destino = nodo.get("id")
            for alias in nodo.get("ids_alias") or []:
                if alias == destino:
                    self.errores.append("%s se declara alias de si mismo" % alias)
                    continue
                # UN ALIAS QUE ES A LA VEZ UN NODO VIVO son dos cosas con un
                # nombre, y eso es fallo. Pero un alias que es un nodo
                # DEPRECADO es justo la forma normal de una fusion: el
                # absorbido conserva su ficha como archivo y su id resuelve
                # al superviviente (D.17).
                if alias in self.canonicos and alias not in self.deprecados:
                    self.errores.append(
                        "%s es alias de %s y a la vez id canonico vivo: dos cosas con un nombre"
                        % (alias, destino))
                if alias in self.mapa_alias and self.mapa_alias[alias] != destino:
                    self.errores.append(
                        "alias %s reclamado por %s y por %s"
                        % (alias, self.mapa_alias[alias], destino))
                    continue
                self.mapa_alias[alias] = destino

    @classmethod
    def desde_dataset(cls, ruta=None):
        return cls(comun.leer_jsonl(ruta or comun.RUTA_DATASET))

    def resolver(self, identificador):
        """Camina la cadena de alias hasta el id canonico VIVO.

        Un id DEPRECADO no es el final del camino: es archivo, y su ficha
        existe para que la fusion sea auditable, pero quien lo nombra quiere
        llegar al superviviente (D.17). Solo si el deprecado no tiene
        sucesor declarado se devuelve el propio deprecado, porque su ficha
        sigue estando ahi y mentir diciendo que no existe seria peor.

        Devuelve None si el id no existe ni como canonico ni como alias
        resoluble, o si la cadena da una vuelta sobre si misma.
        """
        if not isinstance(identificador, str) or not identificador:
            return None
        visitados = []
        actual = identificador
        for _ in range(LIMITE_CADENA):
            if actual in self.canonicos and actual not in self.deprecados:
                return actual
            if actual in visitados:
                return None
            visitados.append(actual)
            siguiente = self.mapa_alias.get(actual)
            if siguiente is None:
                # sin sucesor: si es un deprecado suelto, es su propia ficha
                return actual if actual in self.canonicos else None
            actual = siguiente
        return None

    def cadena(self, identificador):
        """Traza el camino recorrido, para explicar un fallo del gate."""
        camino = [identificador]
        actual = identificador
        for _ in range(LIMITE_CADENA):
            if actual in self.canonicos and actual not in self.deprecados:
                return camino
            siguiente = self.mapa_alias.get(actual)
            if siguiente is None or siguiente in camino:
                return camino
            camino.append(siguiente)
            actual = siguiente
        return camino

    def existe(self, identificador):
        return self.resolver(identificador) is not None

    def esta_vivo(self, identificador):
        """Superficie o archivo. Un deprecado existe, pero no se ofrece."""
        return identificador in self.canonicos and identificador not in self.deprecados

    def nodo(self, identificador):
        resuelto = self.resolver(identificador)
        return self.canonicos.get(resuelto) if resuelto else None

    def mismo(self, id_a, id_b):
        """La unica comparacion de ids legitima del repo."""
        resuelto_a = self.resolver(id_a)
        resuelto_b = self.resolver(id_b)
        if resuelto_a is None or resuelto_b is None:
            return False
        return resuelto_a == resuelto_b

    def resolver_lista(self, identificadores):
        """Resuelve y deduplica conservando el orden. Los no resolubles se
        devuelven tal cual: quien decide si eso es fallo es el gate."""
        salida = []
        for identificador in identificadores or []:
            resuelto = self.resolver(identificador) or identificador
            if resuelto not in salida:
                salida.append(resuelto)
        return salida

    def ids_vivos(self):
        return sorted(i for i in self.canonicos if i not in self.deprecados)


def informe(ruta=None):
    resolutor = Resolutor.desde_dataset(ruta)
    lineas = ["nodos vivos: %d" % len(resolutor.ids_vivos()),
              "nodos deprecados (archivo): %d" % len(resolutor.deprecados),
              "alias registrados: %d" % len(resolutor.mapa_alias)]
    for alias in sorted(resolutor.mapa_alias):
        camino = resolutor.cadena(alias)
        lineas.append("  %s resuelve a %s%s"
                      % (alias, resolutor.resolver(alias) or "NADA",
                         "  (cadena: %s)" % " > ".join(camino) if len(camino) > 2 else ""))
    for error in resolutor.errores:
        lineas.append("  FALLO: %s" % error)
    return "\n".join(lineas)
