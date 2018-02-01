# -*- coding: utf-8 -*-

''' Copyright (C) 2017 Iván Rodríguez Méndez
This software is distributed under the GNU General Public
Licence (version 3 or later); please refer to the file
Licence.txt, included with the software, for details.
'''
# Tutorial creado para el canal de YouTube Piensa 3D

# Tutorial 4: Semáforo completo

#importamos los módulos necesarios para nuestro código 
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.OUT) ## GPIO 4 ROJO COCHES
GPIO.setup(17, GPIO.OUT) ## GPIO 17 AMARILLO COCHES
GPIO.setup(27, GPIO.OUT) ## GPIO 27 VERDE COCHES
GPIO.setup(14, GPIO.OUT) ## GPIO 14 VERDE PEATONES
GPIO.setup(15, GPIO.OUT) ## GPIO 15 ROJO PEATONES
GPIO.setup(22, GPIO.IN) ## ENTRADA PULSADOR

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
while True:
    semaforo()

print("Limpiando la configuración de los GPIO")
GPIO.cleanup() ## Hago una limpieza de los GPIO
