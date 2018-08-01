# -*- coding: utf-8 -*-

''' Copyright (C) 2018 Iván Rodríguez Méndez
This software is distributed under the GNU General Public
Licence (version 3 or later); please refer to the file
Licence.txt, included with the software, for details.
'''
# Tutorial creado para el canal de YouTube Piensa 3D

# Tutorial 6: Efectos con LED RGB

#importamos los módulos necesarios para nuestro código
import RPi.GPIO as GPIO
import time
import numpy as np

GPIO.setmode(GPIO.BCM)
GPIO.setup(14, GPIO.OUT) ## Color Rojo
GPIO.setup(15, GPIO.OUT) ## Color Verde
GPIO.setup(18, GPIO.OUT) ## Color Azul

Colores = np.array([14,15,18]) # Es importante que el orden sea RGB

def Apagar_led(Leds):
    for i in range(len(Leds)):
        GPIO.output(Leds[i],False)
    return 0

def Encender_leds(Leds):
	for i in range(len(Leds)):
		GPIO.output(Leds[i],True)
		time.sleep(0.05)
		GPIO.output(Leds[i],False)
	for i in range(len(Leds)):
		GPIO.output(Leds[len(Leds)-i-1],True)
		time.sleep(0.05)
		GPIO.output(Leds[len(Leds)-i-1],False)

def Encender_mix_rgb(r,g,b, Colores):
    if (r > 0):
        GPIO.output(Colores[0],True)
    else:
        GPIO.output(Colores[0],False)
    if (g > 0):
        GPIO.output(Colores[1],True)
    else:
        GPIO.output(Colores[1],False)
    if (b > 0):
        GPIO.output(Colores[2],True)
    else:
        GPIO.output(Colores[2],False)
    return 0

# Código principal desde el que usamos todas las funciones
Apagar_led(Colores)

for j in range(10):
	Encender_leds(Colores)

# Encendemos el color Cyan
Encender_mix_rgb(0,1,1, Colores)
time.sleep(3)
# Encendemos el color Amarillo
Encender_mix_rgb(1,1,0, Colores)
time.sleep(3)
# Encendemos el color Magenta
Encender_mix_rgb(1,0,1, Colores)
time.sleep(3)
# Encendemos el color Blanco
Encender_mix_rgb(1,1,1, Colores)
time.sleep(3)

print("Limpiando la configuración de los GPIO")
GPIO.cleanup() ## Hago una limpieza de los GPIO
