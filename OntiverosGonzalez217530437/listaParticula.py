from particula import Particula
import json
from grafos import *

class ListaParticula():
    def __init__(self) -> None:
        self.__particulas = []
        
    def __str__(self) -> str:
        return "".join(
            str(part) + "\n" for part in self.__particulas)
    
    def __len__(self):
        return len(self.__particulas)
    
    def __iter__(self):
        self.cont = 0
        return self
    
    def __next__(self):
        if self.cont < len(self.__particulas):
            part = self.__particulas[self.cont]
            self.cont += 1
            return part
        
        else: 
            raise StopIteration


    def agregar_final(self, part: Particula) -> None:
        self.__particulas.append(part)

    def agregar_inicio(self, part: Particula) -> None: 
        self.__particulas.insert(0, part)
    
    def mostrar(self) -> None:
        for part in self.__particulas:
            print(part)

    def get_puntos(self):
        puntos = []
        for particula in self.__particulas:
            x = particula.origen_x
            y = particula.origen_y
            punto = (x, y)
            puntos.append(punto)
            x = particula.destino_x
            y = particula.destino_y
            punto = (x, y)
            puntos.append(punto)
        for punto in puntos:
            print(punto)
        return puntos

    def get_puntos2(self):
        puntos = []
        for particula in self.__particulas:
            punto01 = Punto(particula.origen_x, particula.origen_y,
                            particula.red, particula.green, particula.blue)
            punto02 = Punto(particula.destino_x, particula.destino_y,
                            particula.red, particula.green, particula.blue)
            puntos.append(punto01)
            puntos.append(punto02)

    def get_grafo(self):
        g = Grafo()
        for particula in self.__particulas:
            punto01 = Punto(particula.origen_x, particula.origen_y,
                            particula.red, particula.green, particula.blue)
            punto02 = Punto(particula.destino_x, particula.destino_y,
                            particula.red, particula.green, particula.blue)
            nodo_origen = Nodo(punto01)
            nodo_destino = Nodo(punto02)
            ponderacion= particula.distancia

            arista = AristaNoDirigida(nodo_origen, nodo_destino, ponderacion)
            g.agregar_arista(arista)
        return g
    
    def get_grafo2(self):
        g = {}
        for particula in self.__particulas:
            origen = (particula.origen_x, particula.origen_y)
            destino = (particula.destino_x, particula.destino_y)
            arista = [(destino, particula.distancia), (origen, particula.distancia)]

            if origen in g:
                g[origen].extend(arista)
            else:
                g[origen] = arista

            if destino in g:
                g[destino].extend(arista)
            else:
                g[destino] = arista
        print("Grafo construido:")        
        for nodo, adyacentes in g.items():
            print(f"{nodo}: {adyacentes}")
        return g


    def guardar(self, ubicacion):
        try:
            with open(ubicacion, 'w') as archivo:
                lista = [part.to_dict() for part in self.__particulas]
                print(lista)
                json.dump(lista, archivo, indent=5)
                return 1
        except:
            return 0
    
    def abrir(self, ubicacion):
        try:
            with open(ubicacion, 'r') as archivo:
                lista = json.load(archivo)
                self.__particulas = [Particula(**part) for part in lista]
                return 1
        except:
            return 0
        

    def sort_by_id(self):
        self.__particulas.sort(key=lambda particula: particula.id)

    def sort_by_distancia_reverse(self):
        self.__particulas.sort(key=lambda particula: particula.distancia, reverse=True)

    
    def sort_by_vel(self):
        self.__particulas.sort(key=lambda particula: particula.velocidad)


class Punto:
    def __init__(self, x:int=0, y:int=0, red:int=0, green:int=0, blue:int=0):
        self.x = x
        self.y = y
        self.red = red
        self.green = green
        self.blue = blue

    def __repr__(self) -> str:
        return f"Punto(x: {self.x}, y: {self.y})"
    

class Punto2:
    def __init__(self, x:int=0, y:int=0):
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return f"Punto(x: {self.x}, y: {self.y})"