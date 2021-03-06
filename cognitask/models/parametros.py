from PyQt5 import QtCore
import random
import os
import cognitask.common.constantes as constantes
from cognitask.common import ubicaciones

# PARAMETROS


def aplicarNivel(self, calibracion):
    # ver si faltan mas configuraciones para definir un nivel. Tal vez duracion de estimulo, etc
    QtCore.QCoreApplication.processEvents()
    fout = open("config/nivel.prm", "wt")

    if  calibracion is False:
        if self.nivel_opciones.currentText() == "Avanzado":
            nivel = constantes.NIVEL_AVANZADO
        elif self.nivel_opciones.currentText() == "Intermedio":
            nivel = constantes.NIVEL_INTERMEDIO
        else:
            nivel = constantes.NIVEL_INICIAL

    elif calibracion is True:
        nivel = constantes.NIVEL_CALIBRACION

    NumberOfSequences = "Application:Sequencing int NumberOfSequences= " + str(nivel) + " 15 1 % // number of sequences in a set of intensifications\n"
    EpochsToAverage = "Filtering:P3TemporalFilter int EpochsToAverage= " + str(nivel) + " 1 0 % // Number of epochs to average"
    fout.write(NumberOfSequences)
    fout.write(EpochsToAverage)
    fout.close()


def aplicarSecuenciaTerapia(self):
    QtCore.QCoreApplication.processEvents()
    orden_secuencia = list(range(1, 10))

    if self.cantidad_pasos < 9:
        for i in range(self.cantidad_pasos, 9):
            orden_secuencia[i] = 0

    # escribimos el archivo de configuracion BCI2000
    # el archivo de configuracion de BCI2000 necesita que los espacios sean indicados con '%20'
    img_path = self.ubicacion_img.replace(' ', '%20')
    install_path = ubicaciones.INSTALL_DIR.replace(' ', '%20')
    fout = open("config/secuencia.prm", "wt")
    fout.write("Application:Speller%20Targets matrix TargetDefinitions= 9 { Display Enter Display%20Size Icon%20File Sound Intensified%20Icon } ")
    lista = ("A A 1 ", "B B 1 ", "C C 1 ", "D D 1 ", "E E 1 ", "F F 1 ", "G G 1 ", "H H 1 ", "I I 1 ")  # necesario para construir el archivo prm
    random.shuffle(orden_secuencia)
    for i in range(0, 9):
        
        if orden_secuencia[i] != 0:
            if os.path.isfile(self.ubicacion_img + "/img" + str(orden_secuencia[i]) + ".png"):
                orden_img = lista[i] + img_path + "/img" + str(orden_secuencia[i]) + ".png % % "
            else:
                orden_img = lista[i] + img_path + "/img" + str(orden_secuencia[i]) + "%20-%20punto.png % % "
        else:
            orden_img = lista[i] + install_path + "/img" + "/img" + str(orden_secuencia[i]) + ".png % % "

        fout.write(orden_img)
        self.orden_secuencia[i] = orden_secuencia[i]

    fout.write("// speller target properties")
    fout.close()


def aplicarSecuenciaCalibracion(self):
    QtCore.QCoreApplication.processEvents()

    fout = open("config/secuencia.prm", "wt")
    fout.write(
        "Application:Speller%20Targets matrix TargetDefinitions= 9 { Display Enter Display%20Size Icon%20File Sound Intensified%20Icon } ")

    if self.calibracion_tarea == 1:
        self.ubicacion_img = ubicaciones.INSTALL_DIR + "/calibracion/tarea 1"
        # esto es necesario para BCI2000, ya que permite conocer como se ordenaran las imagenes en la matriz
        lista = constantes.LISTA_UNO
        orden_sec = constantes.ORDEN_UNO
        text_to_spell = "Application:Speller string TextToSpell= " + constantes.TAREA_UNO + " // character or string to spell in offline copy mode"

    elif self.calibracion_tarea == 2:
        self.ubicacion_img = ubicaciones.INSTALL_DIR + "/calibracion/tarea 2"
        # esto es necesario para BCI2000, ya que permite conocer como se ordenaran las imagenes en la matriz
        lista = constantes.LISTA_DOS
        orden_sec = constantes.ORDEN_DOS
        text_to_spell = "Application:Speller string TextToSpell= " + constantes.TAREA_DOS + " // character or string to spell in offline copy mode"

    else:
        self.ubicacion_img = ubicaciones.INSTALL_DIR + "/calibracion/tarea 3"
        # esto es necesario para BCI2000, ya que permite conocer como se ordenaran las imagenes en la matriz
        lista = constantes.LISTA_TRES
        orden_sec = constantes.ORDEN_TRES
        text_to_spell = "Application:Speller string TextToSpell= " + constantes.TAREA_TRES + " // character or string to spell in offline copy mode"

    ubicacion_img = self.ubicacion_img.replace(' ', '%20')

    # evita que la gui se cuelgue cuando se cargan los parametros
    QtCore.QCoreApplication.processEvents()
    for i in range(0, 9):
        orden_img = lista[i] + ubicacion_img + "/img" + str(orden_sec[i]) + ".png % % "
        fout.write(orden_img)

    fout.write("// speller target properties\n")
    fout.write(text_to_spell)
    fout.close()
    self.orden_secuencia = orden_sec
