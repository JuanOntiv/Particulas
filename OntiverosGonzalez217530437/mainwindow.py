from PySide2.QtWidgets import QMainWindow, QFileDialog, QMessageBox, QTableWidgetItem, QGraphicsScene, QGraphicsLineItem, QGraphicsEllipseItem
from PySide2.QtCore import Slot, Qt, QLineF
from PySide2.QtGui import QPen, QColor, QTransform, QWheelEvent, QPainter, QAccessibleValueChangeEvent
from ui_mainwindow import Ui_MainWindow
from listaParticula import * 
from particula import * 
from algoritmos import *
from pprint import pprint 
from random import *
from grafos import *

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.listaParticula = ListaParticula()
        self.puntos2 = []
        self.puntos = []        
        self.graf = None

        self.ui.agregar_inicio_pushButton.clicked.connect(self.click_agregar_inicio)
        self.ui.agregar_final_pushButton.clicked.connect(self.click_agregar_final)
        self.ui.mostrar_pushButton.clicked.connect(self.click_mostrar)
        self.ui.mostrar_tabla_pushButton.clicked.connect(self.mostrar_Tabla)
        self.ui.buscar_pushButton.clicked.connect(self.buscar_id)

        self.ui.actionAbrir.triggered.connect(self.action_Abrir_Archivo)
        self.ui.actionGuardar.triggered.connect(self.action_Guardar_Archivo)

        self.ui.dibujar.clicked.connect(self.dibujar)
        self.ui.limpiar.clicked.connect(self.limpiar)

        self.scene = QGraphicsScene()
        self.ui.graphicsView.setScene(self.scene)

        #Ordenamientos
        self.ui.actionOrdenar_por_Id.triggered.connect(self.sort_id)
        self.ui.actionOrdenar_por_Distancia_Rev.triggered.connect(self.sort_distancia_reverse)
        self.ui.actionOrdenar_por_Velocidad.triggered.connect(self.sort_velocidad)

        #Fuerza Bruta
        self.ui.actionPuntos.triggered.connect(self.dibujar_puntos)
        self.ui.actionPuntos_Cercanos.triggered.connect(self.mostrar_puntos_cercanos)

        #Grafos
        self.ui.pushButton_grafo.clicked.connect(self.mostrar_lista)

        self.scene2 = QGraphicsScene()
        self.ui.graphicsView_2.setScene(self.scene2)

        self.ui.actionDijkstra.triggered.connect(self.dijkstra)
        self.ui.actionPrim.triggered.connect(self.Prim1)
        self.ui.actionGraham.triggered.connect(self.Graham)


        #Grafos Aleatorios

        #Aleatorios
        self.ui.spinBox_puntos.valueChanged[int].connect(self.spinBox_puntos)
        self.ui.horizontalSlider.valueChanged[int].connect(self.slider_puntos)
        self.ui.Dibujar_Al_pushButton.clicked.connect(self.dibujar_puntos3)
        self.ui.puntos_cercanos_al_pushButton.clicked.connect(self.mostrar_puntos_cercanos2)
        
        self.scene3 = QGraphicsScene()
        self.ui.graphicsView_3.setScene(self.scene3)

        self.ui.Dijkstra_pushButton.clicked.connect(self.dijkstra_al)
        self.ui.kruskal_pushButton.clicked.connect(self.kruskal_al)
        self.ui.prim_pushButton.clicked.connect(self.prim_al)
        

 

    @Slot( )
    def click_agregar_final(self):
        id = self.ui.id_spinBox.value()
        origen_x = self.ui.origen_x_spinBox.value()
        origen_y = self.ui.origen_y_spinBox.value()
        destino_x = self.ui.destino_x_spinBox.value()
        destino_y = self.ui.destino_y_spinBox.value()
        velocidad = self.ui.velocidad_spinBox.value()
        red = self.ui.red_spinBox.value()
        green = self.ui.green_spinBox.value()
        blue = self.ui.blue_spinBox.value()

        particula = Particula(id, origen_x, origen_y, destino_x, destino_y, velocidad, red, green, blue)
        self.listaParticula.agregar_final(particula)

    @Slot( )
    def click_agregar_inicio(self):
        id = self.ui.id_spinBox.value()
        origen_x = self.ui.origen_x_spinBox.value()
        origen_y = self.ui.origen_y_spinBox.value()
        destino_x = self.ui.destino_x_spinBox.value()
        destino_y = self.ui.destino_y_spinBox.value()
        velocidad = self.ui.velocidad_spinBox.value()
        red = self.ui.red_spinBox.value()
        green = self.ui.green_spinBox.value()
        blue = self.ui.blue_spinBox.value()

        particula = Particula(id, origen_x, origen_y, destino_x, destino_y, velocidad, red, green, blue)
        self.listaParticula.agregar_inicio(particula)

    @Slot()
    def click_mostrar(self) -> None:
        self.ui.plainTextEdit.clear()
        self.ui.plainTextEdit.insertPlainText(str(self.listaParticula))
        #self.listaParticula.mostrar()


    @Slot()
    def action_Abrir_Archivo(self):
        #print("Abrir_Archivo")
        ubicacion = QFileDialog.getOpenFileName(
            self, 
            'Abrir Archivo', 
            '.', 'JSON (*.json)'
        )[0]
        if self.listaParticula.abrir(ubicacion):
            QMessageBox.information(
                self, 
                "Exito",
                  "Se abrio el archivo " + ubicacion)
        else:
            QMessageBox.information(
                self, 
                "Error",
                  "No se pudo abrir el archivo " + ubicacion)
        

    @Slot()
    def action_Guardar_Archivo(self):
        ubicacion = QFileDialog.getSaveFileName(self, 'Guardar Archivo', '.', 'JSON (*.json)')[0]
        print(ubicacion)
        if self.listaParticula.guardar(ubicacion):
            QMessageBox.information(self, "Exito", "Se pudo crear el archivo " + ubicacion)
        else:
            QMessageBox.information(self, "Error", "No se pudo crear el archivo " + ubicacion)

    @Slot()
    def mostrar_Tabla(self):
        self.ui.tabla.setColumnCount(10)
        headers = ["ID", "Origen x", "Origen y", "Destino x", "Destino y", "Velocidad", "Red", "Green", "Blue", "Distancia"]
        
        self.ui.tabla.setHorizontalHeaderLabels(headers)
        self.ui.tabla.setRowCount(len(self.listaParticula))

        row = 0
        for partic in self.listaParticula:
            id_widget = QTableWidgetItem(str(partic.id))
            origen_x_widget = QTableWidgetItem(str(partic.origen_x))
            origen_y_widget = QTableWidgetItem(str(partic.origen_y))
            destino_x_widget = QTableWidgetItem(str(partic.destino_x))
            destino_y__widget = QTableWidgetItem(str(partic.destino_y))
            velocidad_widget = QTableWidgetItem(str(partic.velocidad))
            rojo_widget = QTableWidgetItem(str(partic.red))
            verde_widget = QTableWidgetItem(str(partic.green))
            azul_widget = QTableWidgetItem(str(partic.blue))
            distancia_widget = QTableWidgetItem(str(partic.distancia))

            self.ui.tabla.setItem(row, 0, id_widget)
            self.ui.tabla.setItem(row, 1, origen_x_widget)
            self.ui.tabla.setItem(row, 2, origen_y_widget)
            self.ui.tabla.setItem(row, 3, destino_x_widget)
            self.ui.tabla.setItem(row, 4, destino_y__widget)
            self.ui.tabla.setItem(row, 5, velocidad_widget)
            self.ui.tabla.setItem(row, 6, rojo_widget)
            self.ui.tabla.setItem(row, 7, verde_widget)
            self.ui.tabla.setItem(row, 8, azul_widget)
            self.ui.tabla.setItem(row, 9, distancia_widget)

            row += 1


    @Slot()
    def buscar_id(self):
        id = self.ui.buscar_lineEdit.text()

        encontrado = True

        for partic in self.listaParticula:
            if id == str(partic.id):
                print("a")
                self.ui.tabla.clear()
                self.ui.tabla.setRowCount(1)
                headers = ["ID", "Origen x", "Origen y", "Destino x", "Destino y", "Velocidad", "Red", "Green", "Blue", "Distancia"]
                
                self.ui.tabla.setHorizontalHeaderLabels(headers)

                id_widget = QTableWidgetItem(str(partic.id))
                origen_x_widget = QTableWidgetItem(str(partic.origen_x))
                origen_y_widget = QTableWidgetItem(str(partic.origen_y))
                destino_x_widget = QTableWidgetItem(str(partic.destino_x))
                destino_y__widget = QTableWidgetItem(str(partic.destino_y))
                velocidad_widget = QTableWidgetItem(str(partic.velocidad))
                rojo_widget = QTableWidgetItem(str(partic.red))
                verde_widget = QTableWidgetItem(str(partic.green))
                azul_widget = QTableWidgetItem(str(partic.blue))
                distancia_widget = QTableWidgetItem(str(partic.distancia))

                self.ui.tabla.setItem(0, 0, id_widget)
                self.ui.tabla.setItem(0, 1, origen_x_widget)
                self.ui.tabla.setItem(0, 2, origen_y_widget)
                self.ui.tabla.setItem(0, 3, destino_x_widget)
                self.ui.tabla.setItem(0, 4, destino_y__widget)
                self.ui.tabla.setItem(0, 5, velocidad_widget)
                self.ui.tabla.setItem(0, 6, rojo_widget)
                self.ui.tabla.setItem(0, 7, verde_widget)
                self.ui.tabla.setItem(0, 8, azul_widget)
                self.ui.tabla.setItem(0, 9, distancia_widget)

                encontrado = True
                print("b")
                return
        if encontrado:
            QMessageBox.warning(
                self, 
                "Atencion",
                f'La particula con el id "{id}" no fue encontrada'
            )

    #QScene    
    def wheelEvent(self, event):
        print(event.delta())
        if event.delta() > 0:
            self.ui.graphicsView.scale(1.2, 1.2)
            self.ui.graphicsView_2.scale(1.2, 1.2)
            self.ui.graphicsView_3.scale(1.2, 1.2)
        else:
            self.ui.graphicsView.scale(0.8, 0.8)
            self.ui.graphicsView_2.scale(0.8, 0.8)
            self.ui.graphicsView_3.scale(0.8, 0.8)

    @Slot()
    def dibujar(self):
        pen = QPen()
        pen.setWidth(2)

        for partic in self.listaParticula:
            r = partic.red
            g = partic.green
            b = partic.blue

            color = QColor(r,g,b)
            pen.setColor(color)

            x_origen = partic.origen_x
            y_origen = partic.origen_y
            x_destin = partic.destino_x
            y_destin = partic.destino_y

            self.scene.addEllipse(x_origen, y_origen, 6, 6, pen)    
            self.scene.addEllipse(x_destin , y_destin , 6, 6, pen)
            self.scene.addLine(x_origen+3, y_origen+3, x_destin+3, y_destin+3, pen)
        #print("dibujar")

    @Slot()
    def limpiar(self):
        self.scene.clear()
        #print("limpiar")


    #Ordenamientos:
    @Slot()
    def sort_id(self):
        self.listaParticula.sort_by_id()

    @Slot()
    def sort_distancia_reverse(self):
        self.listaParticula.sort_by_distancia_reverse()

    @Slot()
    def sort_velocidad(self):
        self.listaParticula.sort_by_vel()


    #Fuerza Bruta:
    @Slot()
    def dibujar_puntos(self):
        pen = QPen()
        pen.setWidth(2)
        self.scene.clear()  # Limpia la escena antes de mostrar los puntos
        for partic in self.listaParticula:
            r = partic.red
            g = partic.green
            b = partic.blue
            color = QColor(r, g, b)
            pen = QPen(color)
            x_origen = partic.origen_x
            y_origen = partic.origen_y
            x_destin = partic.destino_x
            y_destin = partic.destino_y
            self.scene.addEllipse(x_origen, y_origen, 6, 6, pen)
            self.scene.addEllipse(x_destin, y_destin, 6, 6, pen)

    @Slot()
    def dibujar_puntos2(self):
        self.scene.clear()
        pen = QPen()
        pen.setWidth(2)
        
        for particula in self.listaParticula:
            color = QColor(particula.red, particula.green, particula.blue)
            pen.setColor(color)

            origen = QGraphicsEllipseItem(particula.origen_x, particula.origen_y, 6, 6)
            destino = QGraphicsEllipseItem(particula.destino_x, particula.destino_y, 6, 6)

            origen.setPen(pen)
            destino.setPen(pen)

            self.scene.addItem(origen)
            self.scene.addItem(destino)

    @Slot()
    def mostrar_puntos_cercanos(self):
        resultado = puntos_mas_cercanos(list(self.listaParticula))

        for punto1, punto2 in resultado:
            pen = QPen()
            pen.setWidth(3)
            color = QColor(punto1.red, punto1.green, punto1.blue)
            pen.setColor(color)
            x1_origen = punto1.origen_x
            y1_origen = punto1.origen_y
            x1_destino = punto1.destino_x
            y1_destino = punto1.destino_y

            x2_origen = punto2.origen_x
            y2_origen = punto2.origen_y
            x2_destino = punto2.destino_x
            y2_destino = punto2.destino_y

            # Dibujar líneas desde los puntos de origen y destino de ambas partículas
            self.scene.addLine(x1_origen, y1_origen, x2_origen, y2_origen, pen)
            self.scene.addLine(x1_destino, y1_destino, x2_destino, y2_destino, pen)


    #Grafos
    '''@Slot()
    def grafo(self):
        self.graf = self.listaParticula.get_grafo()
        self.graf.print_lista_adyacencia()
        s = self.graf.grafo_to_str()
        self.ui.plainTextEdit_2.setPlainText(s)
        return self.graf'''
    
    @Slot()
    def mostrar_lista(self):
        grafo = self.listaParticula.get_grafo2()

        print("Lista de Adyacencia:")
        for nodo, adyacentes in grafo.items():
            print(f"{nodo}: {adyacentes}")

        # Mostrar en el textBrowser
        self.ui.textBrowser.clear()
        self.ui.textBrowser.append("Lista de Adyacencia:")
        for nodo, adyacentes in grafo.items():
            self.ui.textBrowser.append(f"{nodo}: {adyacentes}")

    @Slot()
    def dijkstra(self):
        self.scene2.clear()

        puntos_grafo = list(self.graf.get_lista_adyacencia().keys())
        puntos_seleccionados = sample(puntos_grafo, 2)

        punto_i, punto_f = puntos_seleccionados

        print("Punto inicial: ", punto_i)
        print("Punto final: ", punto_f)

        grafo = self.graf.get_lista_adyacencia()
        distancias = dijkstra(grafo, punto_i)

        camino_min = [punto_f]
        while punto_f != punto_i:
            vecinos = grafo[punto_f]
            punto_f, _ = min(vecinos, key=lambda x: distancias[x[0]])
            camino_min.append(punto_f)

        print("Camino minimo: ", camino_min)

        for punto, vecinos in grafo.items():
            for vecino, _ in vecinos:
                self.scene2.addLine(punto.x, punto.y, vecino.x, vecino.y, QPen(QColor(150, 150, 150)))

        for i in range(len(camino_min) - 1):
            x1, y1 = camino_min[i].x, camino_min[i].y
            x2, y2 = camino_min[i + 1].x, camino_min[i + 1].y
            self.scene2.addLine(x1, y1, x2, y2, QPen(QColor(255, 0, 0)))

    @Slot()
    def Prim1(self):
        self.scene2.clear()
        grafo = self.listaParticula.get_grafo2()
        self.dibujar_puntos()
        Prim = prim1(grafo)

        pen = QPen()
        pen.setWidth(3)
        pen.setColor(QColor(0, 0, 0))

        for arista in Prim:
            punto1, punto2, _ = arista
            self.scene2.addLine(punto1[0], punto1[1], punto2[0], punto2[1], pen)    

    @Slot()
    def Graham(self):
        self.scene2.clear()
        puntos = self.listaParticula.get_puntos()
        self.dibujar_puntos2()
        grahamm = graham1(puntos)

        if isinstance(grahamm, str):
            print(grahamm) 
        else:
            pen = QPen()
            pen.setWidth(3)
            pen.setColor(QColor(0, 0, 0))

            for i in range(len(grahamm) - 1):
                lineas = QGraphicsLineItem(QLineF(grahamm[i][0], grahamm[i][1], grahamm[i + 1][0], grahamm[i + 1][1]))
                lineas.setPen(pen)
                self.scene2.addItem(lineas)

            lineas = QGraphicsLineItem(QLineF(grahamm[-1][0], grahamm[-1][1], grahamm[0][0], grahamm[0][1]))
            lineas.setPen(pen)
            self.scene2.addItem(lineas)


    
    #ALEATORIOS
    @Slot(int)
    def spinBox_puntos(self, x):
        self.ui.horizontalSlider.setValue(x)

    @Slot(int)
    def slider_puntos(self, x):
        self.ui.spinBox_puntos.setValue(x)

    @Slot()
    def dibujar_puntos3(self):
        self.scene3.clear()
        self.puntos = ()

        self.puntos = get_puntos(self.ui.spinBox_puntos.value())
        pprint(self.puntos)

        for punto in self.puntos:
            x = punto[0]
            y = punto[1]
            self.scene3.addEllipse(x,y,6,6)

    @Slot()
    def mostrar_puntos_cercanos2(self):
        resultado = puntos_mas_cercanos2(self.puntos)
        pprint(resultado)

        for punto1, punto2 in resultado:
            x1 = punto1[0]
            y1 = punto1[1]
            x2 = punto2[0]
            y2 = punto2[1]

            self.scene3.addLine(x1, y1, x2, y2)
        
    @Slot()
    def dijkstra_al(self):
        self.scene3.clear()
        puntos_seleccionados = sample(self.puntos, 2)
        punto_i, punto_f = puntos_seleccionados

        print("Punto inicial: ", punto_i)
        print("Punto final: ", punto_f)

        grafo = generar_grafo(self.puntos)
        distancias = dijkstra(grafo, punto_i)

        camino_min = [punto_f]
        while punto_f != punto_i:
            vecinos = grafo[punto_f]
            punto_f, _ = min(vecinos, key=lambda x: distancias[x[0]])
            camino_min.append(punto_f)

        print("Camino minimo: ", camino_min)

        for punto, vecinos in grafo.items():
            for vecino, _ in vecinos:
                self.scene3.addLine(punto[0], punto[1], vecino[0], vecino[1], QPen(QColor(150, 150, 150,)))
        for i in range(len(camino_min) -1):
            x1, y1 = camino_min[i]
            x2, y2 = camino_min[i + 1]
            self.scene3.addLine(x1, y1, x2, y2, QPen(QColor(255,0,0)))


    @Slot()
    def kruskal_al(self):
        self.scene3.clear()
        puntos_seleccionados = sample(self.puntos, 2)
        punto_i, punto_f = puntos_seleccionados

        print("Punto inicial: ", punto_i)
        print("Punto final: ", punto_f)

        grafo = generar_grafo(self.puntos)
        arbol = kruskal(grafo, punto_i)

        for punto, vecinos in arbol.items():
            for vecino, _ in vecinos:
                if punto and vecino:
                    self.scene3.addLine(punto[0], punto[1], vecino[0], vecino[1], QPen(QColor(150, 150, 150,)))
        
        camino_min = list(arbol.keys())
        for i in range(len(camino_min) - 1):
            x1, y1 = camino_min[i]
            x2, y2 = camino_min[i + 1]
            self.scene3.addLine(x1, y1, x2, y2, QPen(QColor(255,0,0)))
        print("Camino minimo: ", camino_min)

    @Slot()
    def prim_al(self):
        self.scene3.clear()

        grafo = generar_grafo(self.puntos)
        arbol = prim(grafo)

        for punto, vecinos in arbol.items():
            for vecino, _ in vecinos:
                if punto and vecino:
                    self.scene3.addLine(punto[0], punto[1], vecino[0], vecino[1], QPen(QColor(150, 150, 150,)))
        
        camino_min = list(arbol.keys())
        for i in range(len(camino_min) - 1):
            x1, y1 = camino_min[i]
            x2, y2 = camino_min[i + 1]
            self.scene3.addLine(x1, y1, x2, y2, QPen(QColor(255,0,0)))
        print("Camino mínimo (Prim): ", camino_min)