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

Colores = np.array([14,15,18])

def Apagar_led():
    for i in range(len(Leds)):
        GPIO.output(Leds[i],False)
    return 0

def Encender_leds():
	for i in range(len(Leds)):
		GPIO.output(Leds[i],True)
		time.sleep(0.05)
		GPIO.output(Leds[i],False)
	for i in range(len(Leds)):
		GPIO.output(Leds[len(Leds)-i-1],True)
		time.sleep(0.05)
		GPIO.output(Leds[len(Leds)-i-1],False)

# Código principal desde el que usamos todas las funciones
Apagar_led()

for j in range(50):
	Encender_leds()

print("Limpiando la configuración de los GPIO")
GPIO.cleanup() ## Hago una limpieza de los GPIO
