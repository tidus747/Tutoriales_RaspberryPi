# -*- coding: utf-8 -*-

''' Copyright (C) 2017 Iván Rodríguez Méndez
This software is distributed under the GNU General Public
Licence (version 3 or later); please refer to the file
Licence.txt, included with the software, for details.
'''
# Tutorial creado para el canal de YouTube Piensa 3D

# Tutorial 1: Blink con el GPIO 18

#importamos los módulos necesarios para nuestro código 
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT) ## GPIO 18 como salida

def blink():
        print "Ejecución de la función blink..."
        iteracion = 0
        for iteracion in range(10): ## Segundos que durara la funcion
                GPIO.output(18, True) ## Enciendo el 18
                time.sleep(0.5) ## Esperamos 1 segundo
                GPIO.output(18, False) ## Apago el 18
                time.sleep(0.5) ## Esperamos 1 segundo
                iteracion = iteracion + 1 
                print(iteracion)
        print "Ejecucion de la función blink finalizada"
        GPIO.cleanup() ## Hago una limpieza de los GPIO

# Código principal desde el que usamos todas las funciones        
blink()
