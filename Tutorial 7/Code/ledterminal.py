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

import numpy as np
from ledFun import *

# Inicializamos los GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(14, GPIO.OUT) ## Color Rojo
GPIO.setup(15, GPIO.OUT) ## Color Verde
GPIO.setup(18, GPIO.OUT) ## Color Azul

# Definimos los colores del led
Colores = np.array([14,15,18]) # Es importante que el orden sea RGB

# Creamos el menu
menu = ConsoleMenu("Menu principal", "Control de un Led RGB por medio de la linea de comandos")

# Creamos los elementos del menu
# Al pulsar llamamos a la función que enciende el led
fi_led_on = FunctionItem("Encender el led", led_on, [Colores, menu])

# Al pulsar llamamos a la función que apaga el led
fi_led_off = FunctionItem("Apagar el led", led_off, [Colores, menu])

# Añadimos los encendidos y apagados de los diferentes colores

# Led rojo
fi_led_on_red = FunctionItem("Encender el led rojo", led_on_red, [Colores, menu])
fi_led_off_red = FunctionItem("Apagar el led rojo", led_off_red, [Colores, menu])

# Led verde
fi_led_on_green = FunctionItem("Encender el led verde", led_on_green, [Colores, menu])
fi_led_off_green = FunctionItem("Apagar el led verde", led_off_green, [Colores, menu])

# Led azul
fi_led_on_blue = FunctionItem("Encender el led azul", led_on_blue, [Colores, menu])
fi_led_off_blue = FunctionItem("Apagar el led azul", led_off_blue, [Colores, menu])

# Colocamos todos los elementos del menu
menu.append_item(fi_led_on)
menu.append_item(fi_led_off)
menu.append_item(fi_led_on_red)
menu.append_item(fi_led_off_red)
menu.append_item(fi_led_on_green)
menu.append_item(fi_led_off_green)
menu.append_item(fi_led_on_blue)
menu.append_item(fi_led_off_blue)

# Mostramos el menu
menu.show()
