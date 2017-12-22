# -*- coding: utf-8 -*-

''' Copyright (C) 2017 Iván Rodríguez Méndez
This software is distributed under the GNU General Public
Licence (version 3 or later); please refer to the file
Licence.txt, included with the software, for details.
'''
# Tutorial creado para el canal de YouTube Piensa 3D

# Tutorial 3: Semáforo simple

#importamos los módulos necesarios para nuestro código 
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.OUT) ## GPIO 4 ROJO
GPIO.setup(17, GPIO.OUT) ## GPIO 17 AMARILLO
GPIO.setup(27, GPIO.OUT) ## GPIO 27 VERDE
rojo = 4
amarillo = 17
verde = 27

tiempoCambio = 5


def semaforo():
        print "Ejecución de la función de semaforo..."
        GPIO.output(rojo, True)
        time.sleep(tiempoCambio)
        
        GPIO.output(verde,True)
        GPIO.output(rojo, False)
        time.sleep(tiempoCambio)
        
        GPIO.output(amarillo,True)
        time.sleep(2)
        
        GPIO.output(amarillo,False)
        GPIO.output(verde,False)
         
# Código principal desde el que usamos todas las funciones
for b in range(3):
    semaforo()

print("Limpiando la configuración de los GPIO")
GPIO.cleanup() ## Hago una limpieza de los GPIO
