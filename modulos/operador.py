### Módulo de Operador ###################################################
##########################################################################
## Autor: Facundo Barreto ### facubrt@gmail.com ##########################
##
## BCI basada en P300 para rehabilitación cognitiva ######################
##
## Proyecto Final de Bioingeniería ### 2020 ##############################

### LICENCIA GPL #########################################################
## This file is part of Cognitask. #######################################
##
##  Cognitask is free software: you can redistribute it and/or modify ####
##  it under the terms of the GNU General Public License as published by #
##  the Free Software Foundation, either version 3 of the License, or ####
##  (at your option) any later version. ##################################
##
##  Cognitask is distributed in the hope that it will be useful, #########
##  but WITHOUT ANY WARRANTY; without even the implied warranty of #######
##  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the ########
##  GNU General Public License for more details. #########################
##
##  You should have received a copy of the GNU General Public License ####
##  along with Cognitask.  If not, see <https://www.gnu.org/licenses/>. ##


from PyQt5 import QtCore, QtGui, QtWidgets
from utils import rec


class Ui_Operador(object):
    def setupUi(self, Operador):
        Operador.setObjectName("Operador")
        Operador.resize(800, 512)
        Operador.setMinimumSize(QtCore.QSize(800, 512))
        Operador.setMaximumSize(QtCore.QSize(800, 512))
        Operador.setStyleSheet("background-color: rgb(38, 43, 50);\n"
                               "border-radius:6px;")
        self.centralwidget = QtWidgets.QWidget(Operador)
        self.centralwidget.setStyleSheet("border-radius:6px;\n"
                                         "")
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setContentsMargins(6, 6, 6, 6)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.left_frame = QtWidgets.QFrame(self.centralwidget)
        self.left_frame.setMinimumSize(QtCore.QSize(150, 500))
        self.left_frame.setMaximumSize(QtCore.QSize(150, 500))
        self.left_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.left_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.left_frame.setObjectName("left_frame")
        self.isotipo_imagen = QtWidgets.QLabel(self.left_frame)
        self.isotipo_imagen.setGeometry(QtCore.QRect(20, 30, 100, 100))
        self.isotipo_imagen.setMinimumSize(QtCore.QSize(100, 100))
        self.isotipo_imagen.setMaximumSize(QtCore.QSize(100, 100))
        self.isotipo_imagen.setText("")
        self.isotipo_imagen.setPixmap(QtGui.QPixmap("img/isotipo.png"))
        self.isotipo_imagen.setScaledContents(True)
        self.isotipo_imagen.setObjectName("isotipo_imagen")
        self.seleccion_nueva_sesion_frame = QtWidgets.QFrame(self.left_frame)
        self.seleccion_nueva_sesion_frame.setGeometry(
            QtCore.QRect(144, 170, 10, 51))
        self.seleccion_nueva_sesion_frame.setMinimumSize(QtCore.QSize(10, 0))
        self.seleccion_nueva_sesion_frame.setMaximumSize(
            QtCore.QSize(10, 16777215))
        self.seleccion_nueva_sesion_frame.setStyleSheet(
            "background-color: rgb(255, 255, 255);")
        self.seleccion_nueva_sesion_frame.setFrameShape(
            QtWidgets.QFrame.StyledPanel)
        self.seleccion_nueva_sesion_frame.setFrameShadow(
            QtWidgets.QFrame.Raised)
        self.seleccion_nueva_sesion_frame.setObjectName(
            "seleccion_nueva_sesion_frame")
        self.seleccion_calibracion_frame = QtWidgets.QFrame(self.left_frame)
        self.seleccion_calibracion_frame.setGeometry(
            QtCore.QRect(144, 230, 10, 51))
        self.seleccion_calibracion_frame.setMinimumSize(QtCore.QSize(10, 0))
        self.seleccion_calibracion_frame.setMaximumSize(
            QtCore.QSize(10, 16777215))
        self.seleccion_calibracion_frame.setStyleSheet("")
        self.seleccion_calibracion_frame.setFrameShape(
            QtWidgets.QFrame.StyledPanel)
        self.seleccion_calibracion_frame.setFrameShadow(
            QtWidgets.QFrame.Raised)
        self.seleccion_calibracion_frame.setObjectName(
            "seleccion_calibracion_frame")
        self.seleccion_terapia_frame = QtWidgets.QFrame(self.left_frame)
        self.seleccion_terapia_frame.setGeometry(
            QtCore.QRect(144, 290, 10, 51))
        self.seleccion_terapia_frame.setMinimumSize(QtCore.QSize(10, 0))
        self.seleccion_terapia_frame.setMaximumSize(QtCore.QSize(10, 16777215))
        self.seleccion_terapia_frame.setStyleSheet("")
        self.seleccion_terapia_frame.setFrameShape(
            QtWidgets.QFrame.StyledPanel)
        self.seleccion_terapia_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.seleccion_terapia_frame.setObjectName("seleccion_terapia_frame")
        self.nueva_sesion_boton = QtWidgets.QPushButton(self.left_frame)
        self.nueva_sesion_boton.setGeometry(QtCore.QRect(-10, 170, 151, 51))
        font = QtGui.QFont()
        font.setFamily("Gilroy-Bold")
        font.setPointSize(12)
        self.nueva_sesion_boton.setFont(font)
        self.nueva_sesion_boton.setStyleSheet("QPushButton{color: rgb(242, 242, 242);border-radius:0px;"
                                              "} QPushButton:hover{background-color: rgb(46, 51, 58);color: rgb(242, 242, 242);"
                                              "}")
        self.nueva_sesion_boton.setFlat(True)
        self.nueva_sesion_boton.setObjectName("nueva_sesion_boton")
        self.calibracion_boton = QtWidgets.QPushButton(self.left_frame)
        self.calibracion_boton.setGeometry(QtCore.QRect(0, 230, 151, 51))
        font = QtGui.QFont()
        font.setFamily("Gilroy-Bold")
        font.setPointSize(12)
        self.calibracion_boton.setFont(font)
        self.calibracion_boton.setStyleSheet("QPushButton{color: rgb(242, 242, 242);border-radius:0px;text-align: left;"
                                             "padding: 15px;} QPushButton:hover{background-color: rgb(46, 51, 58);color: rgb(242, 242, 242);"
                                             "}")
        self.calibracion_boton.setFlat(True)
        self.calibracion_boton.setObjectName("calibracion_boton")
        self.terapia_boton = QtWidgets.QPushButton(self.left_frame)
        self.terapia_boton.setGeometry(QtCore.QRect(0, 290, 151, 51))
        font = QtGui.QFont()
        font.setFamily("Gilroy-Bold")
        font.setPointSize(12)
        self.terapia_boton.setFont(font)
        self.terapia_boton.setStyleSheet("QPushButton{color: rgb(242, 242, 242);border-radius:0px;text-align: left;"
                                         "padding: 15px;} QPushButton:hover{background-color: rgb(46, 51, 58);color: rgb(242, 242, 242);"
                                         "}")
        self.terapia_boton.setFlat(True)
        self.terapia_boton.setObjectName("terapia_boton")
        self.salir_boton = QtWidgets.QPushButton(self.left_frame)
        self.salir_boton.setGeometry(QtCore.QRect(0, 450, 141, 51))
        font = QtGui.QFont()
        font.setFamily("Gilroy-Bold")
        font.setPointSize(12)
        self.salir_boton.setFont(font)
        self.salir_boton.setStyleSheet("QPushButton{color: rgb(242, 242, 242);border-radius:0px;text-align: left;\n"
                                       "padding: 15px;}QPushButton:hover{border-bottom-left-radius:6px;background-color: rgb(234, 86, 61); color: rgb(242, 242, 242);"
                                       "}")
        self.salir_boton.setFlat(True)
        self.salir_boton.setObjectName("salir_boton")
        self.terapia_boton.raise_()
        self.calibracion_boton.raise_()
        self.nueva_sesion_boton.raise_()
        self.isotipo_imagen.raise_()
        self.seleccion_nueva_sesion_frame.raise_()
        self.seleccion_calibracion_frame.raise_()
        self.seleccion_terapia_frame.raise_()
        self.salir_boton.raise_()
        self.horizontalLayout.addWidget(self.left_frame)
        self.rigth_frame = QtWidgets.QFrame(self.centralwidget)
        self.rigth_frame.setMinimumSize(QtCore.QSize(0, 500))
        self.rigth_frame.setMaximumSize(QtCore.QSize(16777215, 500))
        self.rigth_frame.setStyleSheet("background-color: rgb(244, 244, 248);\n"
                                       "border-radius: 6px;")
        self.rigth_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.rigth_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.rigth_frame.setObjectName("rigth_frame")
        self.configuracion_frame = QtWidgets.QFrame(self.rigth_frame)
        self.configuracion_frame.setGeometry(QtCore.QRect(0, 0, 381, 501))
        self.configuracion_frame.setStyleSheet(
            "background-color: rgb(255, 255, 255); border-radius: 0px")
        self.configuracion_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.configuracion_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.configuracion_frame.setObjectName("configuracion_frame")
        self.configuracion_stacked_widget = QtWidgets.QStackedWidget(
            self.configuracion_frame)
        self.configuracion_stacked_widget.setGeometry(
            QtCore.QRect(10, 10, 361, 481))
        font = QtGui.QFont()
        font.setFamily("Gilroy-Regular")
        self.configuracion_stacked_widget.setFont(font)
        self.configuracion_stacked_widget.setObjectName(
            "configuracion_stacked_widget")
        self.nueva_sesion_pagina = QtWidgets.QWidget()
        self.nueva_sesion_pagina.setObjectName("nueva_sesion_pagina")
        self.nueva_sesion_titulo = QtWidgets.QLabel(self.nueva_sesion_pagina)
        self.nueva_sesion_titulo.setGeometry(QtCore.QRect(50, 40, 261, 61))
        font = QtGui.QFont()
        font.setFamily("Gilroy-Light")
        font.setPointSize(30)
        font.setBold(False)
        font.setWeight(50)
        self.nueva_sesion_titulo.setFont(font)
        self.nueva_sesion_titulo.setStyleSheet("color:  rgb(38, 43, 50);")
        self.nueva_sesion_titulo.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.nueva_sesion_titulo.setObjectName("nueva_sesion_titulo")
        self.nombre_texto = QtWidgets.QLabel(self.nueva_sesion_pagina)
        self.nombre_texto.setGeometry(QtCore.QRect(50, 130, 250, 21))
        self.nombre_texto.setMinimumSize(QtCore.QSize(250, 0))
        self.nombre_texto.setMaximumSize(QtCore.QSize(250, 16777215))
        font = QtGui.QFont()
        font.setFamily("Gilroy-Regular")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.nombre_texto.setFont(font)
        self.nombre_texto.setStyleSheet("color: rgb(38, 43, 50);")
        self.nombre_texto.setObjectName("nombre_texto")
        self.nombre_entrada = QtWidgets.QLineEdit(self.nueva_sesion_pagina)
        self.nombre_entrada.setGeometry(QtCore.QRect(50, 160, 261, 25))
        font = QtGui.QFont()
        font.setFamily("Gilroy-Regular")
        font.setPointSize(10)
        self.nombre_entrada.setFont(font)
        self.nombre_entrada.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                          "border-radius:4px;\n"
                                          "border-style: solid;\n"
                                          "border-width:1px;\n"
                                          "border-color:  rgb(38, 43, 50);")
        self.nombre_entrada.setText("")
        self.nombre_entrada.setAlignment(QtCore.Qt.AlignCenter)
        self.nombre_entrada.setObjectName("nombre_entrada")
        self.directorio_entrada = QtWidgets.QLineEdit(self.nueva_sesion_pagina)
        self.directorio_entrada.setGeometry(QtCore.QRect(50, 240, 200, 25))
        self.directorio_entrada.setMinimumSize(QtCore.QSize(0, 25))
        self.directorio_entrada.setMaximumSize(QtCore.QSize(200, 25))
        font = QtGui.QFont()
        font.setFamily("Gilroy-Regular")
        font.setPointSize(10)
        self.directorio_entrada.setFont(font)
        self.directorio_entrada.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                              "border-radius:4px;\n"
                                              "border-style: solid;\n"
                                              "border-width:1px;\n"
                                              "border-color:  rgb(38, 43, 50);")
        self.directorio_entrada.setText("")
        self.directorio_entrada.setAlignment(QtCore.Qt.AlignCenter)
        self.directorio_entrada.setReadOnly(True)
        self.directorio_entrada.setClearButtonEnabled(False)
        self.directorio_entrada.setObjectName("directorio_entrada")
        self.directorio_texto = QtWidgets.QLabel(self.nueva_sesion_pagina)
        self.directorio_texto.setGeometry(QtCore.QRect(50, 210, 180, 21))
        self.directorio_texto.setMinimumSize(QtCore.QSize(180, 0))
        self.directorio_texto.setMaximumSize(QtCore.QSize(180, 16777215))
        font = QtGui.QFont()
        font.setFamily("Gilroy-Regular")
        font.setPointSize(12)
        self.directorio_texto.setFont(font)
        self.directorio_texto.setStyleSheet("color: rgb(38, 43, 50);")
        self.directorio_texto.setObjectName("directorio_texto")
        self.directorio_boton = QtWidgets.QPushButton(self.nueva_sesion_pagina)
        self.directorio_boton.setGeometry(QtCore.QRect(260, 240, 50, 25))
        self.directorio_boton.setMinimumSize(QtCore.QSize(50, 25))
        self.directorio_boton.setMaximumSize(QtCore.QSize(50, 25))
        font = QtGui.QFont()
        font.setFamily("Gilroy-Regular")
        font.setPointSize(10)
        self.directorio_boton.setFont(font)
        self.directorio_boton.setStyleSheet("QPushButton {background-color: rgb(244, 244, 248);color: rgb(38, 43, 50);"
                                            "border-radius:4px;border-style: solid;border-width:1px;border-color:  rgb(38, 43, 50);}"
                                            "QPushButton:hover{border-radius:4px;background-color: rgb(252, 252, 252);color: rgb(38, 43, 50);"
                                            "border-style: solid;border-width:1px;border-color:  rgb(38, 43, 50);} QPushButton:disabled{color:rgb(116,123,141);"
                                            "border-radius:4px;border-style: solid;border-width:1px; border-color:  rgb(116, 123, 141);}")
        self.directorio_boton.setObjectName("directorio_boton")
        self.iniciar_sesion_boton = QtWidgets.QPushButton(
            self.nueva_sesion_pagina)
        self.iniciar_sesion_boton.setGeometry(QtCore.QRect(50, 390, 111, 50))
        self.iniciar_sesion_boton.setMinimumSize(QtCore.QSize(111, 0))
        self.iniciar_sesion_boton.setMaximumSize(QtCore.QSize(111, 16777215))
        font = QtGui.QFont()
        font.setFamily("Gilroy-Regular")
        font.setPointSize(10)
        self.iniciar_sesion_boton.setFont(font)
        self.iniciar_sesion_boton.setStyleSheet("QPushButton{color: rgb(242, 242, 242);border-radius:4px;"
                                                "background-color: rgb(35, 181, 156);border-style: solid;border-width:1px;border-color:  rgb(38, 43, 50);}"
                                                "QPushButton:hover{background-color: rgb(47, 193, 165);color: rgb(242, 242, 242);border-radius:4px;}"
                                                "QPushButton:disabled{color:rgb(116,123,141); border-radius:4px;border-style: solid;"
                                                "border-width:1px; border-color:  rgb(116, 123, 141); background-color: rgb(244, 244, 248);}")
        self.iniciar_sesion_boton.setObjectName("iniciar_sesion_boton")
        self.configuracion_stacked_widget.addWidget(self.nueva_sesion_pagina)
        self.calibracion_pagina = QtWidgets.QWidget()
        self.calibracion_pagina.setObjectName("calibracion_pagina")
        self.calibracion_titulo = QtWidgets.QLabel(self.calibracion_pagina)
        self.calibracion_titulo.setGeometry(QtCore.QRect(50, 40, 261, 61))
        font = QtGui.QFont()
        font.setFamily("Gilroy-Light")
        font.setPointSize(30)
        font.setBold(False)
        font.setWeight(50)
        self.calibracion_titulo.setFont(font)
        self.calibracion_titulo.setStyleSheet("color:  rgb(38, 43, 50);")
        self.calibracion_titulo.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.calibracion_titulo.setObjectName("calibracion_titulo")
        #font = QtGui.QFont()
        # font.setFamily("Gilroy-Regular")
        # font.setPointSize(10)
        # font.setBold(False)
        # font.setWeight(50)

        #font = QtGui.QFont()
        # font.setFamily("Gilroy-Regular")
        # font.setPointSize(12)
        # font.setBold(False)
        # font.setWeight(50)
        self.widget = QtWidgets.QWidget(self.calibracion_pagina)
        self.widget.setGeometry(QtCore.QRect(50, 130, 261, 111))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(10)
        self.gridLayout.setObjectName("gridLayout")
        self.calibracion_completada_1 = QtWidgets.QLabel(self.widget)
        self.calibracion_completada_1.setMinimumSize(QtCore.QSize(22, 22))
        self.calibracion_completada_1.setMaximumSize(QtCore.QSize(22, 22))
        self.calibracion_completada_1.setText("")
        self.calibracion_completada_1.setPixmap(
            QtGui.QPixmap("img/completado_d.png"))
        self.calibracion_completada_1.setScaledContents(True)
        self.calibracion_completada_1.setObjectName("calibracion_completada_1")
        self.gridLayout.addWidget(self.calibracion_completada_1, 0, 0, 1, 1)
        self.calibracion_estado_1 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Gilroy-Regular")
        font.setPointSize(10)
        self.calibracion_estado_1.setFont(font)
        self.calibracion_estado_1.setObjectName("calibracion_estado_1")
        self.gridLayout.addWidget(self.calibracion_estado_1, 0, 1, 1, 1)
        self.calibracion_completada_2 = QtWidgets.QLabel(self.widget)
        self.calibracion_completada_2.setMinimumSize(QtCore.QSize(22, 22))
        self.calibracion_completada_2.setMaximumSize(QtCore.QSize(22, 22))
        self.calibracion_completada_2.setText("")
        self.calibracion_completada_2.setPixmap(
            QtGui.QPixmap("img/completado_d.png"))
        self.calibracion_completada_2.setScaledContents(True)
        self.calibracion_completada_2.setObjectName("calibracion_completada_2")
        self.gridLayout.addWidget(self.calibracion_completada_2, 1, 0, 1, 1)
        self.calibracion_estado_2 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Gilroy-Regular")
        font.setPointSize(10)
        self.calibracion_estado_2.setFont(font)
        self.calibracion_estado_2.setObjectName("calibracion_estado_2")
        self.gridLayout.addWidget(self.calibracion_estado_2, 1, 1, 1, 1)
        self.calibracion_completada_3 = QtWidgets.QLabel(self.widget)
        self.calibracion_completada_3.setMinimumSize(QtCore.QSize(22, 22))
        self.calibracion_completada_3.setMaximumSize(QtCore.QSize(22, 22))
        self.calibracion_completada_3.setText("")
        self.calibracion_completada_3.setPixmap(
            QtGui.QPixmap("img/completado_d.png"))
        self.calibracion_completada_3.setScaledContents(True)
        self.calibracion_completada_3.setObjectName("calibracion_completada_3")
        self.gridLayout.addWidget(self.calibracion_completada_3, 2, 0, 1, 1)
        self.calibracion_estado_3 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Gilroy-Regular")
        font.setPointSize(10)
        self.calibracion_estado_3.setFont(font)
        self.calibracion_estado_3.setObjectName("calibracion_estado_3")
        self.gridLayout.addWidget(self.calibracion_estado_3, 2, 1, 1, 1)
        #font = QtGui.QFont()
        # font.setFamily("Gilroy-Regular")
        # font.setPointSize(10)

        self.clasificador_texto = QtWidgets.QLabel(self.calibracion_pagina)
        self.clasificador_texto.setGeometry(QtCore.QRect(50, 290, 180, 21))
        self.clasificador_texto.setMinimumSize(QtCore.QSize(180, 0))
        self.clasificador_texto.setMaximumSize(QtCore.QSize(180, 16777215))
        font = QtGui.QFont()
        font.setFamily("Gilroy-Regular")
        font.setPointSize(12)
        self.clasificador_texto.setFont(font)
        self.clasificador_texto.setStyleSheet("color: rgb(38, 43, 50);")
        self.clasificador_texto.setObjectName("clasificador_texto")
        self.clasificador_boton = QtWidgets.QPushButton(
            self.calibracion_pagina)
        self.clasificador_boton.setGeometry(QtCore.QRect(50, 320, 261, 25))
        font = QtGui.QFont()
        font.setFamily("Gilroy-Regular")
        font.setPointSize(10)
        self.clasificador_boton.setFont(font)
        self.clasificador_boton.setStyleSheet("QPushButton {background-color: rgb(244, 244, 248);color: rgb(38, 43, 50);"
                                              "border-radius:4px;border-style: solid;border-width:1px;border-color:  rgb(38, 43, 50);}"
                                              "QPushButton:hover{border-radius:4px;background-color: rgb(252, 252, 252);color: rgb(38, 43, 50);border-style: solid;"
                                              "border-width:1px;border-color:  rgb(38, 43, 50);} QPushButton:disabled{color:rgb(116,123,141);"
                                              "border-radius:4px;border-style: solid;border-width:1px;border-color:  rgb(116, 123, 141);}")
        self.clasificador_boton.setObjectName("clasificador_boton")
        self.preparar_calibracion_boton = QtWidgets.QPushButton(
            self.calibracion_pagina)
        self.preparar_calibracion_boton.setGeometry(
            QtCore.QRect(50, 390, 111, 50))
        self.preparar_calibracion_boton.setMinimumSize(QtCore.QSize(111, 0))
        self.preparar_calibracion_boton.setMaximumSize(
            QtCore.QSize(111, 16777215))
        font = QtGui.QFont()
        font.setFamily("Gilroy-Regular")
        font.setPointSize(10)
        self.preparar_calibracion_boton.setFont(font)
        self.preparar_calibracion_boton.setStyleSheet("QPushButton {background-color: rgb(244, 244, 248);color: rgb(38, 43, 50);"
                                                      "border-radius:4px;border-style: solid;border-width:1px;border-color:  rgb(38, 43, 50);} QPushButton:hover{"
                                                      "border-radius:4px;background-color: rgb(252, 252, 252);color: rgb(38, 43, 50);border-style: solid;border-width:1px;"
                                                      "border-color:  rgb(38, 43, 50);} QPushButton:disabled{color:rgb(116,123,141); border-radius:4px;border-style: solid;"
                                                      "border-width:1px; border-color:  rgb(116, 123, 141);}")
        self.preparar_calibracion_boton.setObjectName(
            "preparar_calibracion_boton")
        self.comenzar_calibracion_boton = QtWidgets.QPushButton(
            self.calibracion_pagina)
        self.comenzar_calibracion_boton.setGeometry(
            QtCore.QRect(170, 390, 111, 50))
        self.comenzar_calibracion_boton.setMinimumSize(QtCore.QSize(111, 0))
        self.comenzar_calibracion_boton.setMaximumSize(
            QtCore.QSize(111, 16777215))
        font = QtGui.QFont()
        font.setFamily("Gilroy-Regular")
        font.setPointSize(10)
        self.comenzar_calibracion_boton.setFont(font)
        self.comenzar_calibracion_boton.setStyleSheet("QPushButton{color: rgb(242, 242, 242);border-radius:4px;"
                                                      "background-color: rgb(35, 181, 156);border-style: solid;border-width:1px;border-color:  rgb(38, 43, 50);}"
                                                      "QPushButton:hover{background-color: rgb(47, 193, 165);color: rgb(242, 242, 242);border-radius:4px;"
                                                      "} QPushButton:disabled{color:rgb(116,123,141); border-radius:4px;border-style: solid;border-width:1px;"
                                                      "border-color:  rgb(116, 123, 141); background-color: rgb(244, 244, 248);}")
        self.comenzar_calibracion_boton.setObjectName(
            "comenzar_calibracion_boton")
        self.configuracion_stacked_widget.addWidget(self.calibracion_pagina)
        self.terapia_pagina = QtWidgets.QWidget()
        self.terapia_pagina.setObjectName("terapia_pagina")
        self.modo_terapia_opciones = QtWidgets.QComboBox(self.terapia_pagina)
        self.modo_terapia_opciones.setGeometry(QtCore.QRect(50, 160, 201, 25))
        self.modo_terapia_opciones.setMinimumSize(QtCore.QSize(0, 25))
        self.modo_terapia_opciones.setMaximumSize(QtCore.QSize(16777215, 25))
        font = QtGui.QFont()
        font.setFamily("Gilroy-Regular")
        font.setPointSize(10)
        self.modo_terapia_opciones.setFont(font)
        self.modo_terapia_opciones.setStyleSheet("QComboBox {background-color: rgb(255, 255, 255);border-radius:4px;border-style: solid;"
                                                 "border-width:1px;border-color:  rgb(38, 43, 50);} QComboBox::drop-down {background-color: rgb(255, 255, 255);"
                                                 "color:rgb(242,242,242);width: 32px;border-top-right-radius: 3px; border-bottom-right-radius: 3px;}"
                                                 "QComboBox::down-arrow {image: url(:/icon/arrow.png);width: 14;height: 14;"
                                                 "} QComboBox QAbstractItemView {background-color: rgb(255, 255, 255);border: 1px solid; border-color:rgb(38, 43, 50);"
                                                 "border-radius: 0px;selection-background-color: rgb(35, 181, 156);}")
        self.modo_terapia_opciones.setObjectName("modo_terapia_opciones")
        self.modo_terapia_opciones.addItem("")
        self.modo_terapia_opciones.addItem("")
        self.modo_terapia_opciones.addItem("")
        self.terapia_titulo = QtWidgets.QLabel(self.terapia_pagina)
        self.terapia_titulo.setGeometry(QtCore.QRect(50, 40, 261, 61))
        font = QtGui.QFont()
        font.setFamily("Gilroy-Light")
        font.setPointSize(30)
        font.setBold(False)
        font.setWeight(50)
        self.terapia_titulo.setFont(font)
        self.terapia_titulo.setStyleSheet("color:  rgb(38, 43, 50);")
        self.terapia_titulo.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.terapia_titulo.setObjectName("terapia_titulo")
        self.aplicar_terapia_boton = QtWidgets.QPushButton(self.terapia_pagina)
        self.aplicar_terapia_boton.setGeometry(QtCore.QRect(50, 390, 111, 50))
        self.aplicar_terapia_boton.setMinimumSize(QtCore.QSize(111, 0))
        self.aplicar_terapia_boton.setMaximumSize(QtCore.QSize(111, 16777215))
        font = QtGui.QFont()
        font.setFamily("Gilroy-Regular")
        font.setPointSize(10)
        self.aplicar_terapia_boton.setFont(font)
        self.aplicar_terapia_boton.setStyleSheet("QPushButton {background-color: rgb(244, 244, 248);color: rgb(38, 43, 50);"
                                                 "border-radius:4px;border-style: solid;border-width:1px;border-color:  rgb(38, 43, 50);}"
                                                 "QPushButton:hover{border-radius:4px;background-color: rgb(252, 252, 252);color: rgb(38, 43, 50);border-style: solid;\n"
                                                 "border-width:1px;border-color:  rgb(38, 43, 50);} QPushButton:disabled{color:rgb(116,123,141); border-radius:4px;border-style: solid;"
                                                 "border-width:1px; border-color:  rgb(116, 123, 141);}")
        self.aplicar_terapia_boton.setObjectName("aplicar_terapia_boton")
        self.archivo_calibracion_texto = QtWidgets.QLabel(self.terapia_pagina)
        self.archivo_calibracion_texto.setGeometry(
            QtCore.QRect(50, 290, 180, 21))
        self.archivo_calibracion_texto.setMinimumSize(QtCore.QSize(180, 0))
        self.archivo_calibracion_texto.setMaximumSize(
            QtCore.QSize(180, 16777215))
        font = QtGui.QFont()
        font.setFamily("Gilroy-Regular")
        font.setPointSize(12)
        self.archivo_calibracion_texto.setFont(font)
        self.archivo_calibracion_texto.setStyleSheet("color: rgb(38, 43, 50);")
        self.archivo_calibracion_texto.setObjectName(
            "archivo_calibracion_texto")
        self.comenzar_terapia_boton = QtWidgets.QPushButton(
            self.terapia_pagina)
        self.comenzar_terapia_boton.setGeometry(
            QtCore.QRect(170, 390, 111, 50))
        self.comenzar_terapia_boton.setMinimumSize(QtCore.QSize(111, 0))
        self.comenzar_terapia_boton.setMaximumSize(QtCore.QSize(111, 16777215))
        font = QtGui.QFont()
        font.setFamily("Gilroy-Regular")
        font.setPointSize(10)
        self.comenzar_terapia_boton.setFont(font)
        self.comenzar_terapia_boton.setStyleSheet("QPushButton{color: rgb(242, 242, 242);border-radius:4px;"
                                                  "background-color: rgb(35, 181, 156);border-style: solid;border-width:1px;border-color:  rgb(38, 43, 50);"
                                                  "} QPushButton:hover{background-color: rgb(47, 193, 165);color: rgb(242, 242, 242);border-radius:4px;"
                                                  "} QPushButton:disabled{color:rgb(116,123,141); border-radius:4px;border-style: solid;border-width:1px;"
                                                  "border-color:  rgb(116, 123, 141); background-color: rgb(244, 244, 248);}")
        self.comenzar_terapia_boton.setObjectName("comenzar_terapia_boton")
        self.archivo_calibracion_boton = QtWidgets.QPushButton(
            self.terapia_pagina)
        self.archivo_calibracion_boton.setGeometry(
            QtCore.QRect(260, 320, 51, 25))
        font = QtGui.QFont()
        font.setFamily("Gilroy-Regular")
        font.setPointSize(10)
        self.archivo_calibracion_boton.setFont(font)
        self.archivo_calibracion_boton.setStyleSheet("QPushButton {background-color: rgb(244, 244, 248);color: rgb(38, 43, 50);"
                                                     "border-radius:4px;border-style: solid;border-width:1px;border-color:  rgb(38, 43, 50);} QPushButton:hover{"
                                                     "border-radius:4px;background-color: rgb(252, 252, 252);color: rgb(38, 43, 50);border-style: solid;border-width:1px;"
                                                     "border-color:  rgb(38, 43, 50);} QPushButton:disabled{color:rgb(116,123,141); border-radius:4px;border-style: solid;"
                                                     "border-width:1px; border-color:  rgb(116, 123, 141);}")
        self.archivo_calibracion_boton.setObjectName(
            "archivo_calibracion_boton")
        self.modo_terapia_texto = QtWidgets.QLabel(self.terapia_pagina)
        self.modo_terapia_texto.setGeometry(QtCore.QRect(50, 130, 250, 21))
        self.modo_terapia_texto.setMinimumSize(QtCore.QSize(250, 0))
        self.modo_terapia_texto.setMaximumSize(QtCore.QSize(250, 16777215))
        font = QtGui.QFont()
        font.setFamily("Gilroy-Regular")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.modo_terapia_texto.setFont(font)
        self.modo_terapia_texto.setStyleSheet("color: rgb(38, 43, 50);")
        self.modo_terapia_texto.setObjectName("modo_terapia_texto")
        self.nivel_texto = QtWidgets.QLabel(self.terapia_pagina)
        self.nivel_texto.setGeometry(QtCore.QRect(50, 210, 250, 21))
        self.nivel_texto.setMinimumSize(QtCore.QSize(250, 0))
        self.nivel_texto.setMaximumSize(QtCore.QSize(250, 16777215))
        font = QtGui.QFont()
        font.setFamily("Gilroy-Regular")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.nivel_texto.setFont(font)
        self.nivel_texto.setStyleSheet("color: rgb(38, 43, 50);")
        self.nivel_texto.setObjectName("nivel_texto")
        self.nivel_opciones = QtWidgets.QComboBox(self.terapia_pagina)
        self.nivel_opciones.setGeometry(QtCore.QRect(50, 240, 101, 25))
        self.nivel_opciones.setMinimumSize(QtCore.QSize(0, 25))
        self.nivel_opciones.setMaximumSize(QtCore.QSize(16777215, 25))
        font = QtGui.QFont()
        font.setFamily("Gilroy-Regular")
        font.setPointSize(10)
        self.nivel_opciones.setFont(font)
        self.nivel_opciones.setStyleSheet("QComboBox {background-color: rgb(255, 255, 255);border-radius:4px;border-style: solid;"
                                          "border-width:1px;border-color:  rgb(38, 43, 50);} QComboBox::drop-down {background-color: rgb(255, 255, 255);"
                                          "color:rgb(242,242,242);width: 32px;border-top-right-radius: 3px; border-bottom-right-radius: 3px;}"
                                          "QComboBox::down-arrow {image: url(:/icon/arrow.png);width: 14;height: 14;"
                                          "} QComboBox QAbstractItemView {background-color: rgb(255, 255, 255);border: 1px solid; border-color:rgb(38, 43, 50);"
                                          "border-radius: 0px;selection-background-color: rgb(35, 181, 156);}")
        self.nivel_opciones.setObjectName("nivel_opciones")
        self.nivel_opciones.addItem("")
        self.nivel_opciones.addItem("")
        self.nivel_opciones.addItem("")
        self.modo_terapia_boton = QtWidgets.QPushButton(self.terapia_pagina)
        self.modo_terapia_boton.setGeometry(QtCore.QRect(260, 160, 50, 25))
        self.modo_terapia_boton.setMinimumSize(QtCore.QSize(50, 25))
        self.modo_terapia_boton.setMaximumSize(QtCore.QSize(50, 25))
        font = QtGui.QFont()
        font.setFamily("Gilroy-Regular")
        font.setPointSize(10)
        self.modo_terapia_boton.setFont(font)
        self.modo_terapia_boton.setStyleSheet("QPushButton {background-color: rgb(244, 244, 248);color: rgb(38, 43, 50);"
                                              "border-radius:4px;border-style: solid;border-width:1px;border-color:  rgb(38, 43, 50);}"
                                              "QPushButton:hover{border-radius:4px;background-color: rgb(252, 252, 252);color: rgb(38, 43, 50);border-style: solid;"
                                              "border-width:1px;border-color:  rgb(38, 43, 50);} QPushButton:disabled{color:rgb(116,123,141); border-radius:4px;"
                                              "border-style: solid; border-width:1px; border-color:  rgb(116, 123, 141);}")
        self.modo_terapia_boton.setObjectName("modo_terapia_boton")
        self.archivo_calibracion_entrada = QtWidgets.QLineEdit(
            self.terapia_pagina)
        self.archivo_calibracion_entrada.setGeometry(
            QtCore.QRect(50, 320, 200, 25))
        self.archivo_calibracion_entrada.setMinimumSize(QtCore.QSize(0, 25))
        self.archivo_calibracion_entrada.setMaximumSize(QtCore.QSize(200, 25))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        self.archivo_calibracion_entrada.setFont(font)
        self.archivo_calibracion_entrada.setStyleSheet("background-color: rgb(255, 255, 255);border-radius:4px;"
                                                       "border-style: solid;border-width:1px;border-color:  rgb(38, 43, 50);")
        self.archivo_calibracion_entrada.setText("")
        self.archivo_calibracion_entrada.setAlignment(QtCore.Qt.AlignCenter)
        self.archivo_calibracion_entrada.setReadOnly(True)
        self.archivo_calibracion_entrada.setPlaceholderText("")
        self.archivo_calibracion_entrada.setClearButtonEnabled(False)
        self.archivo_calibracion_entrada.setObjectName(
            "archivo_calibracion_entrada")
        # AGREGADO GUIA INICIAL
        self.guia_inicial_texto = QtWidgets.QLabel(self.terapia_pagina)
        self.guia_inicial_texto.setGeometry(QtCore.QRect(210, 210, 100, 21))
        self.guia_inicial_texto.setMinimumSize(QtCore.QSize(100, 0))
        self.guia_inicial_texto.setMaximumSize(QtCore.QSize(250, 16777215))
        font = QtGui.QFont()
        font.setFamily("Gilroy-Regular")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.guia_inicial_texto.setFont(font)
        self.guia_inicial_texto.setToolTip("")
        self.guia_inicial_texto.setToolTipDuration(-1)
        self.guia_inicial_texto.setStatusTip("")
        self.guia_inicial_texto.setWhatsThis("")
        self.guia_inicial_texto.setStyleSheet("color: rgb(38, 43, 50);")
        self.guia_inicial_texto.setObjectName("guia_inicial_texto")
        self.guia_inicial_opciones = QtWidgets.QComboBox(self.terapia_pagina)
        self.guia_inicial_opciones.setGeometry(QtCore.QRect(210, 240, 101, 25))
        self.guia_inicial_opciones.setMinimumSize(QtCore.QSize(0, 25))
        self.guia_inicial_opciones.setMaximumSize(QtCore.QSize(16777215, 25))
        font = QtGui.QFont()
        font.setFamily("Gilroy-Regular")
        font.setPointSize(10)
        self.guia_inicial_opciones.setFont(font)
        self.guia_inicial_opciones.setStyleSheet("QComboBox {background-color: rgb(255, 255, 255);border-radius:4px;border-style: solid;"
                                                 "border-width:1px;border-color:  rgb(38, 43, 50);} QComboBox::drop-down {background-color: rgb(255, 255, 255);"
                                                 "color:rgb(242,242,242);width: 32px;border-top-right-radius: 3px; border-bottom-right-radius: 3px;}"
                                                 "QComboBox::down-arrow {image: url(:/icon/arrow.png);width: 14;height: 14;"
                                                 "} QComboBox QAbstractItemView {background-color: rgb(255, 255, 255);border: 1px solid; border-color:rgb(38, 43, 50);"
                                                 "border-radius: 0px;selection-background-color: rgb(35, 181, 156);}")
        self.guia_inicial_opciones.setObjectName("guia_inicial_opciones")
        self.guia_inicial_opciones.addItem("")
        self.guia_inicial_opciones.addItem("")
        # AGREGADO GUIA INICIAL
        self.configuracion_stacked_widget.addWidget(self.terapia_pagina)
        self.informacion_stacked_widget = QtWidgets.QStackedWidget(
            self.rigth_frame)
        self.informacion_stacked_widget.setGeometry(
            QtCore.QRect(380, 100, 251, 401))
        self.informacion_stacked_widget.setObjectName(
            "informacion_stacked_widget")
        self.informacion_nueva_sesion = QtWidgets.QWidget()
        self.informacion_nueva_sesion.setObjectName("informacion_nueva_sesion")
        self.como_empezar_nueva_sesion = QtWidgets.QLabel(
            self.informacion_nueva_sesion)
        self.como_empezar_nueva_sesion.setGeometry(
            QtCore.QRect(20, 20, 221, 331))
        font = QtGui.QFont()
        font.setFamily("Gilroy-Regular")
        font.setPointSize(10)
        font.setItalic(False)
        self.como_empezar_nueva_sesion.setFont(font)
        self.como_empezar_nueva_sesion.setStyleSheet(
            "color: rgb(116, 123, 141);")
        self.como_empezar_nueva_sesion.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.como_empezar_nueva_sesion.setObjectName(
            "como_empezar_nueva_sesion")
        self.informacion_stacked_widget.addWidget(
            self.informacion_nueva_sesion)
        self.informacion_calibracion = QtWidgets.QWidget()
        self.informacion_calibracion.setObjectName("informacion_calibracion")
        self.como_empezar_calibracion = QtWidgets.QLabel(
            self.informacion_calibracion)
        self.como_empezar_calibracion.setGeometry(
            QtCore.QRect(20, 20, 221, 351))
        font = QtGui.QFont()
        font.setFamily("Gilroy-Regular")
        font.setPointSize(10)
        font.setItalic(False)
        self.como_empezar_calibracion.setFont(font)
        self.como_empezar_calibracion.setStyleSheet(
            "color: rgb(116, 123, 141);")
        self.como_empezar_calibracion.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.como_empezar_calibracion.setObjectName("como_empezar_calibracion")
        self.informacion_stacked_widget.addWidget(self.informacion_calibracion)
        self.informacion_terapia = QtWidgets.QWidget()
        self.informacion_terapia.setObjectName("informacion_terapia")
        self.como_empezar_terapia = QtWidgets.QLabel(self.informacion_terapia)
        self.como_empezar_terapia.setGeometry(QtCore.QRect(20, 20, 231, 361))
        font = QtGui.QFont()
        font.setFamily("Gilroy-Regular")
        font.setPointSize(10)
        font.setItalic(False)
        self.como_empezar_terapia.setFont(font)
        self.como_empezar_terapia.setStyleSheet("color: rgb(116, 123, 141);")
        self.como_empezar_terapia.setText("<html><head/><body><p><span style=\" font-weight:600;\">Paso 1</span><br/>Seleccione un tipo de tarea y<br/>busque la carpeta de imágenes<br/>que desee utilizar.<br/><br/><span style=\" font-weight:600;\">Paso 2</span><br/>Seleccione un nivel. El nivel inicial<br/>es recomendable para las primeras<br/>sesiones. Un nivel superior requerirá<br/>una mayor concentración por parte <br/>del paciente.<br/><br/><span style=\" font-weight:600;\">Paso 3</span><br/>Cargue el archivo de calibración<br/>generado por BCI2000 - P3Classifier<br/><br/><span style=\" font-weight:600;\">Paso 4</span><br/>Aplique la configuración y compruebe<br/>el correcto funcionamiento de los<br/>electrodos. Cuando esté listo, inicie<br/>la sesión con el botón &quot;Comenzar&quot;</p></body></html>")
        self.como_empezar_terapia.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.como_empezar_terapia.setObjectName("como_empezar_terapia")
        self.informacion_stacked_widget.addWidget(self.informacion_terapia)
        # AGREGADO
        self.informacion_resumen = QtWidgets.QWidget()
        font = QtGui.QFont()
        font.setFamily("Gilroy-Regular")
        font.setPointSize(10)
        self.informacion_resumen.setFont(font)
        self.informacion_resumen.setObjectName("informacion_resumen")
        self.widget = QtWidgets.QWidget(self.informacion_resumen)
        self.widget.setGeometry(QtCore.QRect(20, 10, 221, 145))
        self.widget.setObjectName("widget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_2.setContentsMargins(6, 10, 6, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        # SESION RESUMEN
        self.sesion_resumen_titulo = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Gilroy-Bold")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.sesion_resumen_titulo.setFont(font)
        self.sesion_resumen_titulo.setStyleSheet("color: rgb(35, 181, 156);")
        self.sesion_resumen_titulo.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.sesion_resumen_titulo.setObjectName("sesion_resumen_titulo")
        self.gridLayout_2.addWidget(self.sesion_resumen_titulo, 0, 0, 1, 2)
        ###
        self.modo_resumen_titulo = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Gilroy-Bold")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.modo_resumen_titulo.setFont(font)
        self.modo_resumen_titulo.setStyleSheet("color: rgb(116, 123, 141);")
        self.modo_resumen_titulo.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.modo_resumen_titulo.setObjectName("modo_resumen_titulo")
        self.gridLayout_2.addWidget(self.modo_resumen_titulo, 1, 0, 1, 1)
        self.modo_resumen_texto = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Gilroy-Regular")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.modo_resumen_texto.setFont(font)
        self.modo_resumen_texto.setStyleSheet("color: rgb(35, 181, 156);")
        self.modo_resumen_texto.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.modo_resumen_texto.setObjectName("modo_resumen_texto")
        self.gridLayout_2.addWidget(self.modo_resumen_texto, 1, 1, 1, 1)
        self.actividad_resumen_titulo = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Gilroy-Bold")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.actividad_resumen_titulo.setFont(font)
        self.actividad_resumen_titulo.setStyleSheet(
            "color: rgb(116, 123, 141);")
        self.actividad_resumen_titulo.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.actividad_resumen_titulo.setObjectName("actividad_resumen_titulo")
        self.gridLayout_2.addWidget(self.actividad_resumen_titulo, 2, 0, 1, 1)
        self.actividad_resumen_texto = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Gilroy-Regular")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.actividad_resumen_texto.setFont(font)
        self.actividad_resumen_texto.setStyleSheet("color: rgb(35, 181, 156);")
        self.actividad_resumen_texto.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.actividad_resumen_texto.setObjectName("actividad_resumen_texto")
        self.gridLayout_2.addWidget(self.actividad_resumen_texto, 2, 1, 1, 1)
        self.nivel_resumen_titulo = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Gilroy-Bold")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.nivel_resumen_titulo.setFont(font)
        self.nivel_resumen_titulo.setStyleSheet("color: rgb(116, 123, 141);")
        self.nivel_resumen_titulo.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.nivel_resumen_titulo.setObjectName("nivel_resumen_titulo")
        self.gridLayout_2.addWidget(self.nivel_resumen_titulo, 3, 0, 1, 1)
        self.nivel_resumen_texto = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Gilroy-Regular")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.nivel_resumen_texto.setFont(font)
        self.nivel_resumen_texto.setStyleSheet("color: rgb(35, 181, 156);")
        self.nivel_resumen_texto.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.nivel_resumen_texto.setObjectName("nivel_resumen_texto")
        self.gridLayout_2.addWidget(self.nivel_resumen_texto, 3, 1, 1, 1)
        self.widget1 = QtWidgets.QWidget(self.informacion_resumen)
        self.widget1.setGeometry(QtCore.QRect(20, 160, 221, 111))
        self.widget1.setObjectName("widget1")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.widget1)
        self.gridLayout_3.setContentsMargins(6, 10, 6, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        # SELECCIONES RESUMEN
        self.selecciones_resumen_titulo = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setFamily("Gilroy-Bold")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.selecciones_resumen_titulo.setFont(font)
        self.selecciones_resumen_titulo.setStyleSheet(
            "color: rgb(35, 181, 156);")
        self.selecciones_resumen_titulo.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.selecciones_resumen_titulo.setObjectName(
            "selecciones_resumen_titulo")
        self.gridLayout_3.addWidget(
            self.selecciones_resumen_titulo, 0, 0, 1, 1)
        self.selecciones_resumen_texto = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setFamily("Gilroy-Regular")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.selecciones_resumen_texto.setFont(font)
        self.selecciones_resumen_texto.setStyleSheet(
            "color: rgb(35, 181, 156);")
        self.selecciones_resumen_texto.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.selecciones_resumen_texto.setObjectName(
            "selecciones_resumen_texto")
        self.gridLayout_3.addWidget(self.selecciones_resumen_texto, 0, 1, 1, 1)
        ###
        self.correctas_resumen_titulo = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setFamily("Gilroy-Bold")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.correctas_resumen_titulo.setFont(font)
        self.correctas_resumen_titulo.setStyleSheet(
            "color: rgb(116, 123, 141);")
        self.correctas_resumen_titulo.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.correctas_resumen_titulo.setObjectName("correctas_resumen_titulo")
        self.gridLayout_3.addWidget(self.correctas_resumen_titulo, 1, 0, 1, 1)
        self.correctas_resumen_texto = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setFamily("Gilroy-Regular")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.correctas_resumen_texto.setFont(font)
        self.correctas_resumen_texto.setStyleSheet(
            "color:  rgb(35, 181, 156);")
        self.correctas_resumen_texto.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.correctas_resumen_texto.setObjectName("correctas_resumen_texto")
        self.gridLayout_3.addWidget(self.correctas_resumen_texto, 1, 1, 1, 1)
        self.incorrectas_resumen_titulo = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setFamily("Gilroy-Bold")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.incorrectas_resumen_titulo.setFont(font)
        self.incorrectas_resumen_titulo.setStyleSheet(
            "color: rgb(116, 123, 141);")
        self.incorrectas_resumen_titulo.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.incorrectas_resumen_titulo.setObjectName(
            "incorrectas_resumen_titulo")
        self.gridLayout_3.addWidget(
            self.incorrectas_resumen_titulo, 2, 0, 1, 1)
        self.incorrectas_resumen_texto = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setFamily("Gilroy-Regular")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.incorrectas_resumen_texto.setFont(font)
        self.incorrectas_resumen_texto.setStyleSheet(
            "color: rgb(35, 181, 156);")
        self.incorrectas_resumen_texto.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.incorrectas_resumen_texto.setObjectName(
            "incorrectas_resumen_texto")
        self.gridLayout_3.addWidget(self.incorrectas_resumen_texto, 2, 1, 1, 1)
        self.widget2 = QtWidgets.QWidget(self.informacion_resumen)
        self.widget2.setGeometry(QtCore.QRect(20, 280, 221, 81))
        self.widget2.setObjectName("widget2")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.widget2)
        self.gridLayout_4.setContentsMargins(6, 10, 6, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        # TIEMPO RESUMEN
        self.tiempo_resumen_titulo = QtWidgets.QLabel(self.widget2)
        font = QtGui.QFont()
        font.setFamily("Gilroy-Bold")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.tiempo_resumen_titulo.setFont(font)
        self.tiempo_resumen_titulo.setStyleSheet("color: rgb(35, 181, 156);")
        self.tiempo_resumen_titulo.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.tiempo_resumen_titulo.setObjectName("tiempo_resumen_titulo")
        self.gridLayout_4.addWidget(self.tiempo_resumen_titulo, 0, 0, 1, 1)
        self.tiempo_resumen_texto = QtWidgets.QLabel(self.widget2)
        font = QtGui.QFont()
        font.setFamily("Gilroy-Regular")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.tiempo_resumen_texto.setFont(font)
        self.tiempo_resumen_texto.setStyleSheet("color: rgb(35, 181, 156);")
        self.tiempo_resumen_texto.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.tiempo_resumen_texto.setObjectName("tiempo_resumen_texto")
        self.gridLayout_4.addWidget(self.tiempo_resumen_texto, 0, 1, 1, 1)
        ###
        self.estado_resumen_titulo = QtWidgets.QLabel(self.widget2)
        font = QtGui.QFont()
        font.setFamily("Gilroy-Bold")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.estado_resumen_titulo.setFont(font)
        self.estado_resumen_titulo.setStyleSheet("color: rgb(35, 181, 156);")
        self.estado_resumen_titulo.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.estado_resumen_titulo.setObjectName("estado_resumen_titulo")
        self.gridLayout_4.addWidget(self.estado_resumen_titulo, 1, 0, 1, 1)
        self.estado_resumen_texto = QtWidgets.QLabel(self.widget2)
        font = QtGui.QFont()
        font.setFamily("Gilroy-Regular")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.estado_resumen_texto.setFont(font)
        self.estado_resumen_texto.setStyleSheet("color: rgb(35, 181, 156);")
        self.estado_resumen_texto.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.estado_resumen_texto.setObjectName("estado_resumen_texto")
        self.gridLayout_4.addWidget(self.estado_resumen_texto, 1, 1, 1, 1)
        self.informacion_stacked_widget.addWidget(self.informacion_resumen)
        self.informacion_titulo = QtWidgets.QLabel(self.rigth_frame)
        self.informacion_titulo.setGeometry(QtCore.QRect(390, 50, 231, 61))
        font = QtGui.QFont()
        font.setFamily("Gilroy-Regular")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.informacion_titulo.setFont(font)
        self.informacion_titulo.setStyleSheet("color: rgb(116, 123, 141);")
        self.informacion_titulo.setAlignment(QtCore.Qt.AlignCenter)
        self.informacion_titulo.setObjectName("informacion_titulo")
        self.informacion_titulo.raise_()
        # AGREGADO
        self.configuracion_frame.raise_()
        self.informacion_stacked_widget.raise_()
        self.horizontalLayout.addWidget(self.rigth_frame)
        self.rigth_frame.raise_()
        self.left_frame.raise_()
        Operador.setCentralWidget(self.centralwidget)

        self.calibracion_completada = (
            self.calibracion_completada_1, self.calibracion_completada_2, self.calibracion_completada_3)
        self.calibracion_estado = (
            self.calibracion_estado_1, self.calibracion_estado_2, self.calibracion_estado_3)
        self.ConfiguracionInicial()
        self.retranslateUi(Operador)
        QtCore.QMetaObject.connectSlotsByName(Operador)

    def retranslateUi(self, Operador):
        _translate = QtCore.QCoreApplication.translate
        Operador.setWindowTitle(_translate("Operador", "MainWindow"))
        self.nueva_sesion_boton.setText(_translate("Operador", "Nueva sesión"))
        self.calibracion_boton.setText(_translate("Operador", "Calibración"))
        self.terapia_boton.setText(_translate("Operador", "Terapia"))
        self.salir_boton.setText(_translate("Operador", "Salir"))
        self.nueva_sesion_titulo.setText(
            _translate("Operador", "Nueva sesión"))
        self.nombre_texto.setText(_translate(
            "Operador", "Nombre y apellido del paciente"))
        self.nombre_entrada.setPlaceholderText(
            _translate("Operador", "Julio Cortazar"))
        self.directorio_entrada.setPlaceholderText(
            _translate("Operador", "C:/Focus/Pacientes"))
        self.directorio_texto.setText(_translate(
            "Operador", "Ubicación de guardado"))
        self.directorio_boton.setText(_translate("Operador", "Buscar"))
        self.iniciar_sesion_boton.setText(
            _translate("Operador", "Iniciar sesión"))
        self.calibracion_titulo.setText(_translate("Operador", "Calibración"))

        self.calibracion_estado_1.setText(_translate(
            "Operador", "Realizar tarea de calibración Nro. 1"))
        self.calibracion_estado_2.setText(_translate(
            "Operador", "Realizar tarea de calibración Nro. 2"))
        self.calibracion_estado_3.setText(_translate(
            "Operador", "Realizar tarea de calibración Nro. 3"))

        self.clasificador_texto.setText(_translate(
            "Operador", "BCI2000 - P300Classifier"))
        self.clasificador_boton.setText(_translate("Operador", "Abrir"))
        self.preparar_calibracion_boton.setText(
            _translate("Operador", "Preparar"))
        self.comenzar_calibracion_boton.setText(
            _translate("Operador", "Comenzar"))
        self.modo_terapia_opciones.setItemText(
            0, _translate("Operador", "Rompecabezas"))
        self.modo_terapia_opciones.setItemText(
            1, _translate("Operador", "Sucesiones"))
        self.modo_terapia_opciones.setItemText(
            2, _translate("Operador", "Palabras"))
        self.terapia_titulo.setText(_translate("Operador", "Terapia"))
        self.aplicar_terapia_boton.setText(_translate("Operador", "Aplicar"))
        self.archivo_calibracion_texto.setText(
            _translate("Operador", "Archivo de calibración"))
        self.comenzar_terapia_boton.setText(_translate("Operador", "Comenzar"))
        self.archivo_calibracion_boton.setText(
            _translate("Operador", "Cargar"))
        self.modo_terapia_texto.setText(
            _translate("Operador", "Tipo de tarea"))
        self.nivel_texto.setText(_translate("Operador", "Nivel"))
        self.nivel_opciones.setItemText(0, _translate("Operador", "Inicial"))
        self.nivel_opciones.setItemText(
            1, _translate("Operador", "Intermedio"))
        self.nivel_opciones.setItemText(2, _translate("Operador", "Avanzado"))
        self.modo_terapia_boton.setText(_translate("Operador", "Buscar"))
        # AGREGADO GUIA INICIAL
        self.guia_inicial_texto.setText(_translate("Operador", "Guía inicial"))
        self.guia_inicial_opciones.setItemText(
            0, _translate("Operador", "Habilitada"))
        self.guia_inicial_opciones.setItemText(
            1, _translate("Operador", "Deshabilitada"))
        # AGREGADO GUIA INICIAL
        self.como_empezar_nueva_sesion.setText(_translate("Operador", "<html><head/><body><p align=\"justify\"><span style=\" font-weight:600;\">Paso 1</span><br/>Ingrese nombre y apellido del<br/>paciente para comenzar una<br/>nueva sesión.<br/><br/><span style=\" font-weight:600;\">Paso 2</span><br/>Seleccione dónde desea guardar<br/>los datos del paciente. Si en esta<br/>ubicación ya existe una carpeta<br/>del paciente, los datos de la<br/>nueva sesión se incluirán dentro<br/>de la misma. En caso contrario, se<br/>creará una carpeta nueva.<br/><br/><span style=\" font-weight:600;\">Paso 3</span><br/>Por último, presione &quot;Iniciar sesión&quot;<br/>para abrir la configuración de la<br/>sesión.</p></body></html>"))
        self.como_empezar_calibracion.setText(_translate("Operador", "<html><head/><body><p><span style=\" font-weight:600;\">Paso 1</span><br/>Indique al paciente que deberá<br/>concentrarse para completar la<br/>tarea indicada</p><p><span style=\" font-weight:600;\">Paso 2</span><br/>Presione &quot;Preparar&quot; y compruebe<br/>el correcto funcionamiento de los<br/>electrodos.</p><p><span style=\" font-weight:600;\">Paso 3</span><br/>Presione &quot;Comenzar&quot; para iniciar<br/>con la primera tarea de calibración.<br/>Cuando termine, regrese al paso 2<br/>para completar las demás tareas.</p><p><span style=\" font-weight:600;\">Paso 4</span><br/>Una vez que todas las tareas se<br/>hayan completado, abra el software<br/>BCI2000 - P3Classifier y cargue los<br/>archivos generados para obtener<br/>un archivo de calibración</p></body></html>"))
        # AGREGADO
        self.modo_resumen_titulo.setText(_translate("Operador", "Tipo"))
        self.modo_resumen_texto.setText(_translate("Operador", ""))
        self.actividad_resumen_titulo.setText(
            _translate("Operador", "Actividad"))
        self.actividad_resumen_texto.setText(_translate("Operador", ""))
        self.nivel_resumen_titulo.setText(_translate("Operador", "Nivel"))
        self.nivel_resumen_texto.setText(_translate("Operador", ""))
        self.selecciones_resumen_titulo.setText(
            _translate("Operador", "Selecciones"))
        self.selecciones_resumen_texto.setText(_translate("Operador", ""))
        self.correctas_resumen_titulo.setText(
            _translate("Operador", "Correctas"))
        self.correctas_resumen_texto.setText(_translate("Operador", ""))
        self.incorrectas_resumen_titulo.setText(
            _translate("Operador", "Incorrectas"))
        self.incorrectas_resumen_texto.setText(_translate("Operador", ""))
        self.sesion_resumen_titulo.setText(_translate("Operador", "Sesión"))
        self.tiempo_resumen_titulo.setText(_translate("Operador", "Tiempo"))
        self.tiempo_resumen_texto.setText(
            _translate("Operador", "00 min 00 s"))
        self.estado_resumen_titulo.setText(_translate("Operador", "Estado"))
        self.estado_resumen_texto.setText(_translate("Operador", ""))

        self.informacion_titulo.setText(
            _translate("Operador", "¿Cómo empezar?"))
        # AGREGADO

    def ConfiguracionInicial(self):
        self.configuracion_stacked_widget.setCurrentIndex(0)
        self.informacion_stacked_widget.setCurrentIndex(0)
        self.nueva_sesion_boton.setEnabled(False)
        self.calibracion_boton.setEnabled(False)
        self.terapia_boton.setEnabled(False)
        self.comenzar_calibracion_boton.setEnabled(False)
        self.comenzar_terapia_boton.setEnabled(False)
        self.clasificador_boton.setEnabled(False)


class BCIOperador(Ui_Operador):

    def __init__(self):
        super(BCIOperador, self).__init__()
        self.setupUi(self)

        # Eliminacion de la barra de titulo por defecto
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        def moveWindow(event):
            if event.buttons() == QtCore.Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()

        self.left_frame.mouseMoveEvent = moveWindow

       # funcion que permite mover la ventana desde left_frame

    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()

    def deshabilitarCambios(self):
        self.comenzar_calibracion_boton.setText("Suspender")
        self.comenzar_terapia_boton.setText("Suspender")
        self.aplicar_terapia_boton.setEnabled(False)
        self.preparar_calibracion_boton.setEnabled(False)
        self.terapia_boton.setEnabled(False)
        self.calibracion_boton.setEnabled(False)
        self.salir_boton.setEnabled(False)
        self.nueva_sesion_boton.setEnabled(False)
        self.iniciar_sesion_boton.setEnabled(False)
        self.nombre_entrada.setEnabled(False)
        self.directorio_entrada.setEnabled(False)
        self.directorio_boton.setEnabled(False)
        self.clasificador_boton.setEnabled(False)
        self.modo_terapia_opciones.setEnabled(False)
        self.modo_terapia_boton.setEnabled(False)
        self.nivel_opciones.setEnabled(False)
        self.archivo_calibracion_entrada.setEnabled(False)
        self.archivo_calibracion_boton.setEnabled(False)
        self.guia_inicial_opciones.setEnabled(False)

    def habilitarCambios(self):
        self.comenzar_calibracion_boton.setText("Comenzar")
        self.comenzar_terapia_boton.setText("Comenzar")
        self.aplicar_terapia_boton.setEnabled(True)
        self.preparar_calibracion_boton.setEnabled(True)
        self.terapia_boton.setEnabled(True)
        self.calibracion_boton.setEnabled(True)
        self.salir_boton.setEnabled(True)
        self.nueva_sesion_boton.setEnabled(True)
        self.iniciar_sesion_boton.setEnabled(True)
        self.nombre_entrada.setEnabled(True)
        self.directorio_entrada.setEnabled(True)
        self.directorio_boton.setEnabled(True)
        self.modo_terapia_opciones.setEnabled(True)
        self.modo_terapia_boton.setEnabled(True)
        self.nivel_opciones.setEnabled(True)
        self.archivo_calibracion_entrada.setEnabled(True)
        self.archivo_calibracion_boton.setEnabled(True)
        self.guia_inicial_opciones.setEnabled(True)

    def restablecerConfiguracion(self):
        # Pagina Nueva Sesion
        self.nombre_entrada.setText("")

        # Pagina Calibracion
        self.calibracion_tarea = 1
        self.calibracion_estado_1.setText(
            "Realizar tarea de calibración Nro. 1")
        self.calibracion_estado_2.setText(
            "Realizar tarea de calibración Nro. 2")
        self.calibracion_estado_3.setText(
            "Realizar tarea de calibración Nro. 3")
        p = QtGui.QPixmap("img/completado_d.png")
        pr = p.scaled(80, 80, QtCore.Qt.KeepAspectRatio,
                      QtCore.Qt.SmoothTransformation)
        self.calibracion_completada_1.setPixmap(QtGui.QPixmap(pr))
        self.calibracion_completada_2.setPixmap(QtGui.QPixmap(pr))
        self.calibracion_completada_3.setPixmap(QtGui.QPixmap(pr))
        self.comenzar_calibracion_boton.setEnabled(False)
        self.clasificador_boton.setEnabled(False)

        # Pagina Terapia
        self.comenzar_terapia_boton.setEnabled(False)
