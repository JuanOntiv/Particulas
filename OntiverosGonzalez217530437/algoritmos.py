from math import *
from math import atan2
from random import randint
from collections import defaultdict
from heapq import heappop, heappush 

def distancia_euclidina(x_1, y_1, x_2, y_2):
        distancia = sqrt((x_2 - x_1)**2 + (y_2-y_1)**2)

        return distancia

def get_puntos(n:int) -> list:
        puntos = []

        for i in range (n):
                x = randint(0, 500)
                y = randint(0, 500)
                punto = ( x, y)
                puntos.append(punto)

        return puntos

def puntos_mas_cercanos(puntos_list):
    resultado = []
    for punto_i in puntos_list:
        min_dist = float('inf')
        cercano = None

        for punto_j in puntos_list:
            if punto_i != punto_j:
                dist_origen = distancia_euclidina(punto_i.origen_x, punto_i.origen_y, punto_j.origen_x, punto_j.origen_y)
                dist_destino = distancia_euclidina(punto_i.destino_x, punto_i.destino_y, punto_j.destino_x, punto_j.destino_y)

                if dist_origen < min_dist:
                    min_dist = dist_origen
                    cercano = punto_j

                if dist_destino < min_dist:
                    min_dist = dist_destino
                    cercano = punto_j

        resultado.append((punto_i, cercano))

    return resultado

def puntos_mas_cercanos2(puntos_list)->list:
    resultado = []
    for punto_i in puntos_list:
        x1 = punto_i[0]
        y1 = punto_i[1]
        min = 1000
        cercano = (0,0)

        for punto_j in puntos_list:
            if punto_i != punto_j:
                x2 = punto_j[0]
                y2 = punto_j[1]

                d = distancia_euclidina(x1,y1,x2,y2)

                if d < min:
                    min = d
                    cercano = (x2,y2)

        resultado.append((punto_i, cercano))

    return resultado


def distancia_euclidina2(punto1, punto2):
        x1, y1 = punto1
        x2, y2 = punto2

        distancia = sqrt((x2 - x1) ** 2 + (y2 - y1)**2)

        return distancia

def generar_grafo(puntos_list, distancia_max=200):
    grafo = defaultdict(list)
    for i, punto1 in enumerate(puntos_list):
        for j, punto2 in enumerate(puntos_list):
            if i != j and distancia_euclidina2(punto1, punto2) <= distancia_max:
                distancia = distancia_euclidina2(punto1, punto2)
                grafo[punto1].append((punto2, distancia))
    return grafo


def generar_grafo2(puntos_list, distancia_max=200):
    grafo = defaultdict(list)
    for i, punto1 in enumerate(puntos_list):
        for j, punto2 in enumerate(puntos_list):
            if i != j and distancia_euclidina2(punto1, punto2) <= distancia_max:
                distancia = distancia_euclidina2(punto1, punto2)
                grafo[punto1].append((punto2, distancia))
                grafo[punto2].append((punto1, distancia))  # Agrega la conexión inversa para un grafo no dirigido
    return grafo



def prim1(grafo):
    arista = []
    lista_aristas = matriz(grafo)
 
    puntos_seleccionado = [False for _ in grafo]
    puntos_seleccionado[0] = True

    tam = len(grafo)
    indice = 0
    x = 0
    y = 0

    while indice < tam - 1:
        min_dist = float('inf')
        for i in range(tam):
            if puntos_seleccionado[i]:
                for j in range(tam):
                    if not puntos_seleccionado[j] and lista_aristas[i][j][2]:
                        if min_dist > lista_aristas[i][j][2]:
                            x = i
                            y = j
                            min_dist = lista_aristas[i][j][2]
        v = lista_aristas[x][y]
        puntos_seleccionado[y] = True
        arista.append(v)
        indice += 1
    return arista


def matriz(grafo):
    lista = []

    for punto_i in grafo:
        lista2 = []
        for punto_j in grafo:
            distancia = distancia_euclidina(punto_i[0], punto_i[1], punto_j[0], punto_j[1])
            lista2.append([punto_i, punto_j, distancia])
        lista.append(lista2)

    return lista


def orient(p, q, r):
    valores = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
    if valores == 0:
        return 0
    return 1 if valores > 0 else 2

def graham1(puntos):
    num = len(puntos)

    if num < 3:
        print("No es posible formar una envolvente convexa con menos de 3 puntos.")
        return None

    pivote = min(puntos, key=lambda punto: (punto[1], punto[0]))
    puntos2 = sorted(puntos, key=lambda punto: (atan2(punto[1] - pivote[1], punto[0] - pivote[0]), punto))
    conv = [pivote, puntos2[0], puntos2[1]]

    for i in range(2, num):
        while len(conv) > 1 and orient(conv[-2], conv[-1], puntos2[i]) != 2:
            conv.pop()
        conv.append(puntos2[i])
    return conv




#Aleatorios
def dijkstra(grafo, punto_inicial):
    distancia = {punto: float('infinity') for punto in grafo}
    distancia[punto_inicial] = 0
    heap = [(0, punto_inicial)]
    while heap:
        actual_dist, punto_actual = heappop(heap)
        if actual_dist > distancia[punto_actual]:
            continue
        for vecino, peso in grafo[punto_actual]:
            nueva_dist = actual_dist + peso
            if nueva_dist < distancia[vecino]:
                 distancia[vecino] = nueva_dist
                 heappush(heap, (nueva_dist, vecino))
    return distancia

def find(union_set, elemento):
    while union_set[elemento] != elemento:
        elemento = union_set[elemento]
    return elemento

def union(union_set, x, y):
    x_raiz = find(union_set, x)
    y_raiz = find(union_set, y)
    union_set[x_raiz] = y_raiz

def kruskal(grafo, punto_i):
    aristas = []

    for punto, vecinos in grafo.items():
        for vecino, distancia in vecinos:
             aristas.append((distancia, punto, vecino))
    aristas.sort()

    union_set = {punto: punto for punto in grafo}

    arbol_min = defaultdict(list)

    for peso, punto1, punto2 in aristas:
        if find(union_set, punto1) != find(union_set, punto2):
            union(union_set, punto1, punto2)
            arbol_min[punto1].append((punto2, peso))
            arbol_min[punto2].append((punto1, peso))

    return arbol_min

def prim(grafo):
    arbol_min = defaultdict(list)
    punto_i = list(grafo.keys())[0]
    visitados = set([punto_i])
    heap = [(peso, punto_i, vecino) for vecino, peso in grafo[punto_i]]
    while heap:
        peso, punto_i, punto_f = heappop(heap)
        if punto_f not in visitados:
            visitados.add(punto_f)
            arbol_min[punto_i].append((punto_f, peso))
            arbol_min[punto_f].append((punto_i, peso))
            for vecino, peso in grafo[punto_f]:
                if vecino not in visitados:
                    heappush(heap, (peso, punto_f, vecino))
    return arbol_min