# -*- coding: utf-8 -*-

''' Copyright (C) 2018 Iván Rodríguez Méndez
This software is distributed under the GNU General Public
Licence (version 3 or later); please refer to the file
Licence.txt, included with the software, for details.
'''
# Tutorial creado para el canal de YouTube Piensa 3D
# Tutorial 7: Control de un led por línea de comandos

# Importamos todos los módulos que son necesarios
from consolemenu import *
from consolemenu.items import *
#import RPi.GPIO as GPIO
#import time
import numpy as np
from ledFun import *

# Definimos los colores del led
Colores = np.array([14,15,18]) # Es importante que el orden sea RGB

# Creamos el menu
menu = ConsoleMenu("Menu principal", "Control de un Led RGB por medio de la linea de comandos")

# Creamos los elementos del menu

# Al pulsar llamamos a la función que enciende el led
fi_led_on = FunctionItem("Encender el led", led_on, [Colores, menu])

# Al pulsar llamamos a la función que apaga el led
fi_led_off = FunctionItem("Apagar el led", led_off, [Colores, menu])

# Colocamos todos los elementos del menu
menu.append_item(fi_led_on)
menu.append_item(fi_led_off)

# Mostramos el menu
menu.show()
