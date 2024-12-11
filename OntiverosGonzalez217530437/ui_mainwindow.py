# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(943, 697)
        self.actionAbrir = QAction(MainWindow)
        self.actionAbrir.setObjectName(u"actionAbrir")
        self.actionGuardar = QAction(MainWindow)
        self.actionGuardar.setObjectName(u"actionGuardar")
        self.actionPuntos_Cercanos = QAction(MainWindow)
        self.actionPuntos_Cercanos.setObjectName(u"actionPuntos_Cercanos")
        self.actionPuntos = QAction(MainWindow)
        self.actionPuntos.setObjectName(u"actionPuntos")
        self.actionOrdenar_por_Id = QAction(MainWindow)
        self.actionOrdenar_por_Id.setObjectName(u"actionOrdenar_por_Id")
        self.actionOrdenar_por_Distancia_Rev = QAction(MainWindow)
        self.actionOrdenar_por_Distancia_Rev.setObjectName(u"actionOrdenar_por_Distancia_Rev")
        self.actionOrdenar_por_Velocidad = QAction(MainWindow)
        self.actionOrdenar_por_Velocidad.setObjectName(u"actionOrdenar_por_Velocidad")
        self.actionDijkstra = QAction(MainWindow)
        self.actionDijkstra.setObjectName(u"actionDijkstra")
        self.actionPrim = QAction(MainWindow)
        self.actionPrim.setObjectName(u"actionPrim")
        self.actionKruskal = QAction(MainWindow)
        self.actionKruskal.setObjectName(u"actionKruskal")
        self.actionGraham = QAction(MainWindow)
        self.actionGraham.setObjectName(u"actionGraham")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayout_3 = QGridLayout(self.tab)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.plainTextEdit = QPlainTextEdit(self.tab)
        self.plainTextEdit.setObjectName(u"plainTextEdit")

        self.gridLayout_3.addWidget(self.plainTextEdit, 0, 1, 1, 1)

        self.particle_groupBox = QGroupBox(self.tab)
        self.particle_groupBox.setObjectName(u"particle_groupBox")
        self.gridLayout = QGridLayout(self.particle_groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.velocidad_label = QLabel(self.particle_groupBox)
        self.velocidad_label.setObjectName(u"velocidad_label")

        self.gridLayout.addWidget(self.velocidad_label, 5, 0, 1, 1)

        self.origen_x_label = QLabel(self.particle_groupBox)
        self.origen_x_label.setObjectName(u"origen_x_label")

        self.gridLayout.addWidget(self.origen_x_label, 1, 0, 1, 1)

        self.id_spinBox = QSpinBox(self.particle_groupBox)
        self.id_spinBox.setObjectName(u"id_spinBox")

        self.gridLayout.addWidget(self.id_spinBox, 0, 2, 1, 1)

        self.destino_y_spinBox = QSpinBox(self.particle_groupBox)
        self.destino_y_spinBox.setObjectName(u"destino_y_spinBox")
        self.destino_y_spinBox.setMaximum(500)

        self.gridLayout.addWidget(self.destino_y_spinBox, 4, 1, 1, 2)

        self.green_spinBox = QSpinBox(self.particle_groupBox)
        self.green_spinBox.setObjectName(u"green_spinBox")
        self.green_spinBox.setMaximum(255)

        self.gridLayout.addWidget(self.green_spinBox, 7, 1, 1, 2)

        self.agregar_inicio_pushButton = QPushButton(self.particle_groupBox)
        self.agregar_inicio_pushButton.setObjectName(u"agregar_inicio_pushButton")

        self.gridLayout.addWidget(self.agregar_inicio_pushButton, 9, 0, 1, 2)

        self.red_spinBox = QSpinBox(self.particle_groupBox)
        self.red_spinBox.setObjectName(u"red_spinBox")
        self.red_spinBox.setMaximum(255)

        self.gridLayout.addWidget(self.red_spinBox, 6, 1, 1, 2)

        self.origen_x_spinBox = QSpinBox(self.particle_groupBox)
        self.origen_x_spinBox.setObjectName(u"origen_x_spinBox")

        self.gridLayout.addWidget(self.origen_x_spinBox, 1, 2, 1, 1)

        self.velocidad_spinBox = QSpinBox(self.particle_groupBox)
        self.velocidad_spinBox.setObjectName(u"velocidad_spinBox")

        self.gridLayout.addWidget(self.velocidad_spinBox, 5, 2, 1, 1)

        self.id_label = QLabel(self.particle_groupBox)
        self.id_label.setObjectName(u"id_label")

        self.gridLayout.addWidget(self.id_label, 0, 0, 1, 1)

        self.origen_y_label = QLabel(self.particle_groupBox)
        self.origen_y_label.setObjectName(u"origen_y_label")

        self.gridLayout.addWidget(self.origen_y_label, 2, 0, 1, 1)

        self.agregar_final_pushButton = QPushButton(self.particle_groupBox)
        self.agregar_final_pushButton.setObjectName(u"agregar_final_pushButton")

        self.gridLayout.addWidget(self.agregar_final_pushButton, 9, 2, 1, 1)

        self.red_label = QLabel(self.particle_groupBox)
        self.red_label.setObjectName(u"red_label")

        self.gridLayout.addWidget(self.red_label, 6, 0, 1, 1)

        self.origen_y_spinBox = QSpinBox(self.particle_groupBox)
        self.origen_y_spinBox.setObjectName(u"origen_y_spinBox")

        self.gridLayout.addWidget(self.origen_y_spinBox, 2, 2, 1, 1)

        self.mostrar_pushButton = QPushButton(self.particle_groupBox)
        self.mostrar_pushButton.setObjectName(u"mostrar_pushButton")

        self.gridLayout.addWidget(self.mostrar_pushButton, 10, 0, 1, 3)

        self.destino_y_label = QLabel(self.particle_groupBox)
        self.destino_y_label.setObjectName(u"destino_y_label")

        self.gridLayout.addWidget(self.destino_y_label, 4, 0, 1, 1)

        self.green_label = QLabel(self.particle_groupBox)
        self.green_label.setObjectName(u"green_label")

        self.gridLayout.addWidget(self.green_label, 7, 0, 1, 1)

        self.destino_x_label = QLabel(self.particle_groupBox)
        self.destino_x_label.setObjectName(u"destino_x_label")

        self.gridLayout.addWidget(self.destino_x_label, 3, 0, 1, 1)

        self.blue_spinBox = QSpinBox(self.particle_groupBox)
        self.blue_spinBox.setObjectName(u"blue_spinBox")
        self.blue_spinBox.setMaximum(255)

        self.gridLayout.addWidget(self.blue_spinBox, 8, 1, 1, 2)

        self.blue_label = QLabel(self.particle_groupBox)
        self.blue_label.setObjectName(u"blue_label")

        self.gridLayout.addWidget(self.blue_label, 8, 0, 1, 1)

        self.destino_x_spinBox = QSpinBox(self.particle_groupBox)
        self.destino_x_spinBox.setObjectName(u"destino_x_spinBox")
        self.destino_x_spinBox.setMaximumSize(QSize(16777215, 16777215))
        self.destino_x_spinBox.setMaximum(500)

        self.gridLayout.addWidget(self.destino_x_spinBox, 3, 1, 1, 2)


        self.gridLayout_3.addWidget(self.particle_groupBox, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayout_4 = QGridLayout(self.tab_2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.buscar_pushButton = QPushButton(self.tab_2)
        self.buscar_pushButton.setObjectName(u"buscar_pushButton")

        self.gridLayout_4.addWidget(self.buscar_pushButton, 1, 2, 1, 1)

        self.tabla = QTableWidget(self.tab_2)
        self.tabla.setObjectName(u"tabla")

        self.gridLayout_4.addWidget(self.tabla, 0, 1, 1, 3)

        self.mostrar_tabla_pushButton = QPushButton(self.tab_2)
        self.mostrar_tabla_pushButton.setObjectName(u"mostrar_tabla_pushButton")

        self.gridLayout_4.addWidget(self.mostrar_tabla_pushButton, 1, 3, 1, 1)

        self.buscar_lineEdit = QLineEdit(self.tab_2)
        self.buscar_lineEdit.setObjectName(u"buscar_lineEdit")

        self.gridLayout_4.addWidget(self.buscar_lineEdit, 1, 1, 1, 1)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.gridLayout_5 = QGridLayout(self.tab_3)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.graphicsView = QGraphicsView(self.tab_3)
        self.graphicsView.setObjectName(u"graphicsView")

        self.gridLayout_5.addWidget(self.graphicsView, 0, 0, 1, 2)

        self.limpiar = QPushButton(self.tab_3)
        self.limpiar.setObjectName(u"limpiar")

        self.gridLayout_5.addWidget(self.limpiar, 8, 0, 1, 2)

        self.dibujar = QPushButton(self.tab_3)
        self.dibujar.setObjectName(u"dibujar")

        self.gridLayout_5.addWidget(self.dibujar, 3, 0, 1, 2)

        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.verticalLayout = QVBoxLayout(self.tab_4)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout_6 = QGridLayout()
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.graphicsView_2 = QGraphicsView(self.tab_4)
        self.graphicsView_2.setObjectName(u"graphicsView_2")

        self.gridLayout_6.addWidget(self.graphicsView_2, 0, 2, 1, 1)

        self.textBrowser = QTextBrowser(self.tab_4)
        self.textBrowser.setObjectName(u"textBrowser")

        self.gridLayout_6.addWidget(self.textBrowser, 0, 0, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout_6)

        self.pushButton_grafo = QPushButton(self.tab_4)
        self.pushButton_grafo.setObjectName(u"pushButton_grafo")

        self.verticalLayout.addWidget(self.pushButton_grafo)

        self.tabWidget.addTab(self.tab_4, "")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.gridLayout_7 = QGridLayout(self.tab_5)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.Dibujar_Al_pushButton = QPushButton(self.tab_5)
        self.Dibujar_Al_pushButton.setObjectName(u"Dibujar_Al_pushButton")

        self.gridLayout_7.addWidget(self.Dibujar_Al_pushButton, 3, 0, 1, 1)

        self.graphicsView_3 = QGraphicsView(self.tab_5)
        self.graphicsView_3.setObjectName(u"graphicsView_3")

        self.gridLayout_7.addWidget(self.graphicsView_3, 1, 0, 1, 3)

        self.prim_pushButton = QPushButton(self.tab_5)
        self.prim_pushButton.setObjectName(u"prim_pushButton")

        self.gridLayout_7.addWidget(self.prim_pushButton, 4, 2, 1, 1)

        self.spinBox_puntos = QSpinBox(self.tab_5)
        self.spinBox_puntos.setObjectName(u"spinBox_puntos")
        self.spinBox_puntos.setMinimum(2)
        self.spinBox_puntos.setMaximum(1000)

        self.gridLayout_7.addWidget(self.spinBox_puntos, 2, 0, 1, 1)

        self.Dijkstra_pushButton = QPushButton(self.tab_5)
        self.Dijkstra_pushButton.setObjectName(u"Dijkstra_pushButton")

        self.gridLayout_7.addWidget(self.Dijkstra_pushButton, 4, 0, 1, 1)

        self.kruskal_pushButton = QPushButton(self.tab_5)
        self.kruskal_pushButton.setObjectName(u"kruskal_pushButton")

        self.gridLayout_7.addWidget(self.kruskal_pushButton, 4, 1, 1, 1)

        self.puntos_cercanos_al_pushButton = QPushButton(self.tab_5)
        self.puntos_cercanos_al_pushButton.setObjectName(u"puntos_cercanos_al_pushButton")

        self.gridLayout_7.addWidget(self.puntos_cercanos_al_pushButton, 3, 1, 1, 2)

        self.horizontalSlider = QSlider(self.tab_5)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setMinimum(2)
        self.horizontalSlider.setMaximum(1000)
        self.horizontalSlider.setOrientation(Qt.Horizontal)

        self.gridLayout_7.addWidget(self.horizontalSlider, 2, 1, 1, 2)

        self.tabWidget.addTab(self.tab_5, "")

        self.gridLayout_2.addWidget(self.tabWidget, 2, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 943, 22))
        self.menuArchivo = QMenu(self.menubar)
        self.menuArchivo.setObjectName(u"menuArchivo")
        self.menuAlgoritmos = QMenu(self.menubar)
        self.menuAlgoritmos.setObjectName(u"menuAlgoritmos")
        self.menuVer = QMenu(self.menubar)
        self.menuVer.setObjectName(u"menuVer")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        QWidget.setTabOrder(self.destino_x_spinBox, self.destino_y_spinBox)
        QWidget.setTabOrder(self.destino_y_spinBox, self.red_spinBox)
        QWidget.setTabOrder(self.red_spinBox, self.green_spinBox)
        QWidget.setTabOrder(self.green_spinBox, self.blue_spinBox)
        QWidget.setTabOrder(self.blue_spinBox, self.agregar_inicio_pushButton)
        QWidget.setTabOrder(self.agregar_inicio_pushButton, self.agregar_final_pushButton)

        self.menubar.addAction(self.menuArchivo.menuAction())
        self.menubar.addAction(self.menuVer.menuAction())
        self.menubar.addAction(self.menuAlgoritmos.menuAction())
        self.menuArchivo.addAction(self.actionAbrir)
        self.menuArchivo.addAction(self.actionGuardar)
        self.menuArchivo.addSeparator()
        self.menuAlgoritmos.addAction(self.actionOrdenar_por_Id)
        self.menuAlgoritmos.addAction(self.actionOrdenar_por_Distancia_Rev)
        self.menuAlgoritmos.addAction(self.actionOrdenar_por_Velocidad)
        self.menuAlgoritmos.addSeparator()
        self.menuAlgoritmos.addAction(self.actionPuntos_Cercanos)
        self.menuAlgoritmos.addSeparator()
        self.menuAlgoritmos.addAction(self.actionPrim)
        self.menuAlgoritmos.addAction(self.actionGraham)
        self.menuVer.addAction(self.actionPuntos)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionAbrir.setText(QCoreApplication.translate("MainWindow", u"Abrir", None))
#if QT_CONFIG(shortcut)
        self.actionAbrir.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+O", None))
#endif // QT_CONFIG(shortcut)
        self.actionGuardar.setText(QCoreApplication.translate("MainWindow", u"Guardar", None))
#if QT_CONFIG(shortcut)
        self.actionGuardar.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.actionPuntos_Cercanos.setText(QCoreApplication.translate("MainWindow", u"Puntos Cercanos", None))
        self.actionPuntos.setText(QCoreApplication.translate("MainWindow", u"Puntos", None))
        self.actionOrdenar_por_Id.setText(QCoreApplication.translate("MainWindow", u"Ordenar por Id", None))
        self.actionOrdenar_por_Distancia_Rev.setText(QCoreApplication.translate("MainWindow", u"Ordenar por Distancia Rev", None))
        self.actionOrdenar_por_Velocidad.setText(QCoreApplication.translate("MainWindow", u"Ordenar por Velocidad", None))
        self.actionDijkstra.setText(QCoreApplication.translate("MainWindow", u"Dijkstra", None))
        self.actionPrim.setText(QCoreApplication.translate("MainWindow", u"Prim", None))
        self.actionKruskal.setText(QCoreApplication.translate("MainWindow", u"Kruskal", None))
        self.actionGraham.setText(QCoreApplication.translate("MainWindow", u"Graham", None))
        self.particle_groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Particle", None))
        self.velocidad_label.setText(QCoreApplication.translate("MainWindow", u"Velocidad:", None))
        self.origen_x_label.setText(QCoreApplication.translate("MainWindow", u"Origen x:", None))
        self.agregar_inicio_pushButton.setText(QCoreApplication.translate("MainWindow", u"Agregar inicio", None))
        self.id_label.setText(QCoreApplication.translate("MainWindow", u"ID:", None))
        self.origen_y_label.setText(QCoreApplication.translate("MainWindow", u"Origen y:", None))
        self.agregar_final_pushButton.setText(QCoreApplication.translate("MainWindow", u"Agregar final", None))
        self.red_label.setText(QCoreApplication.translate("MainWindow", u"Red:", None))
        self.mostrar_pushButton.setText(QCoreApplication.translate("MainWindow", u"Mostrar", None))
        self.destino_y_label.setText(QCoreApplication.translate("MainWindow", u"Destino y:", None))
        self.green_label.setText(QCoreApplication.translate("MainWindow", u"Green:", None))
        self.destino_x_label.setText(QCoreApplication.translate("MainWindow", u"Destino x:", None))
        self.blue_label.setText(QCoreApplication.translate("MainWindow", u"Blue:", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Agregar", None))
        self.buscar_pushButton.setText(QCoreApplication.translate("MainWindow", u"Buscar", None))
        self.mostrar_tabla_pushButton.setText(QCoreApplication.translate("MainWindow", u"Mostrar", None))
        self.buscar_lineEdit.setInputMask("")
        self.buscar_lineEdit.setText("")
        self.buscar_lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Identificador de part\u00edcula", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Tabla", None))
        self.limpiar.setText(QCoreApplication.translate("MainWindow", u"Limpiar", None))
        self.dibujar.setText(QCoreApplication.translate("MainWindow", u"Dibujar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Gr\u00e1fico", None))
        self.pushButton_grafo.setText(QCoreApplication.translate("MainWindow", u"Obtener Grafos", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"Grafos", None))
        self.Dibujar_Al_pushButton.setText(QCoreApplication.translate("MainWindow", u"Dibujar", None))
        self.prim_pushButton.setText(QCoreApplication.translate("MainWindow", u"Prim", None))
        self.Dijkstra_pushButton.setText(QCoreApplication.translate("MainWindow", u"Dijkstra", None))
        self.kruskal_pushButton.setText(QCoreApplication.translate("MainWindow", u"Kruskal", None))
        self.puntos_cercanos_al_pushButton.setText(QCoreApplication.translate("MainWindow", u"Puntos Cercanos", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), QCoreApplication.translate("MainWindow", u"Puntos Aleatorios", None))
        self.menuArchivo.setTitle(QCoreApplication.translate("MainWindow", u"Archivo", None))
        self.menuAlgoritmos.setTitle(QCoreApplication.translate("MainWindow", u"Algoritmos", None))
        self.menuVer.setTitle(QCoreApplication.translate("MainWindow", u"Ver", None))
    # retranslateUi

