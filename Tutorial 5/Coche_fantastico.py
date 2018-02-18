# -*- coding: utf-8 -*-

''' Copyright (C) 2017 Iván Rodríguez Méndez
This software is distributed under the GNU General Public
Licence (version 3 or later); please refer to the file
Licence.txt, included with the software, for details.
'''
# Tutorial creado para el canal de YouTube Piensa 3D

# Tutorial 5: Coche fantástico

#importamos los módulos necesarios para nuestro código 
import RPi.GPIO as GPIO
import time
import numpy as np

GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.OUT) ## GPIO 4 
GPIO.setup(17, GPIO.OUT) ## GPIO 17 
GPIO.setup(27, GPIO.OUT) ## GPIO 27 
GPIO.setup(14, GPIO.OUT) ## GPIO 14 
GPIO.setup(15, GPIO.OUT) ## GPIO 15 

Leds = np.array
Leds = [27,17,4,15,14]


def Apagar_Leds():
	for i in range(len(Leds)):
		GPIO.output(Leds[i],False)
	return 0
		
def Encender_Leds():
	for i in range(len(Leds)):
		GPIO.output(Leds[i],True)
		time.sleep(0.05)
		GPIO.output(Leds[i],False)
	for i in range(len(Leds)):
		GPIO.output(Leds[len(Leds)-i-1],True)
		time.sleep(0.05)
		GPIO.output(Leds[len(Leds)-i-1],False)
	        
# Código principal desde el que usamos todas las funciones
Apagar_Leds()

for j in range(50):
	Encender_Leds()

print("Limpiando la configuración de los GPIO")
GPIO.cleanup() ## Hago una limpieza de los GPIO
