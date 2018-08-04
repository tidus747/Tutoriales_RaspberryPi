# -*- coding: utf-8 -*-

''' Copyright (C) 2018 Iván Rodríguez Méndez
This software is distributed under the GNU General Public
Licence (version 3 or later); please refer to the file
Licence.txt, included with the software, for details.
'''

# Tutorial creado para el canal de YouTube Piensa 3D
# Tutorial 7: Control de un led por línea de comandos

def led_on(Colores, menu):
    menu.epilogue_text = "Hemos encendido el led"
    return 0

def led_off(Colores, menu):
    menu.epilogue_text = "Hemos apagado el led"
    return 0

def led_on_red(Colores):
    GPIO.output(Colores[0],True)
    return 0

def led_off_red(Colores):
    GPIO.output(Colores[0],True)
    return 0

def led_on_green(Colores):
    GPIO.output(Colores[1],True)
    return 0

def led_off_green(Colores):
    GPIO.output(Colores[1],True)
    return 0

def led_on_blue(Colores):
    GPIO.output(Colores[2],True)
    return 0

def led_off_blue(Colores):
    GPIO.output(Colores[2],True)
    return 0
