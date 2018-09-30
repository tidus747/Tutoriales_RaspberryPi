# -*- coding: utf-8 -*-

''' Copyright (C) 2018 Iván Rodríguez Méndez
This software is distributed under the GNU General Public
Licence (version 3 or later); please refer to the file
Licence.txt, included with the software, for details.
'''

# Tutorial creado para el canal de YouTube Piensa 3D
# Tutorial 8: Control de un led con GUI

import RPi.GPIO as GPIO
import numpy as np

def led_on(Colores):
    for i in range(len(Colores)):
        GPIO.output(Colores[i],True)
    return 0

def led_off(Colores):
    for i in range(len(Colores)):
        GPIO.output(Colores[i],False)
    return 0

def led_on_red(Colores):
    GPIO.output(Colores[0],True)
    return 0

def led_off_red(Colores):
    GPIO.output(Colores[0],False)
    return 0

def led_on_green(Colores):
    GPIO.output(Colores[1],True)
    return 0

def led_off_green(Colores):
    GPIO.output(Colores[1],False)
    return 0

def led_on_blue(Colores):
    GPIO.output(Colores[2],True)
    return 0

def led_off_blue(Colores):
    GPIO.output(Colores[2],False)
    return 0
