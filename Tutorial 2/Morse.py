# -*- coding: utf-8 -*-

''' Copyright (C) 2017 Iván Rodríguez Méndez
This software is distributed under the GNU General Public
Licence (version 3 or later); please refer to the file
Licence.txt, included with the software, for details.
'''
# Tutorial creado para el canal de YouTube Piensa 3D

# Tutorial 2: Código MORSE con el GPIO 18

#importamos los módulos necesarios para nuestro código 
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT) ## GPIO 18 como salida

def morse():
        print "Ejecución de la función de comunicación morse..."
        for a in range(3): #3 Puntos para la letra S
            GPIO.output(18, True) ## Enciendo el 18
            time.sleep(0.15) ## Esperamos 0.15 segundo
            GPIO.output(18, False) ## Apago el 18
            time.sleep(0.1)
        time.sleep(0.1) #Hacemos el cambio de letra
        for a in range(3): #3 Líneas para la letra O
            GPIO.output(18, True) ## Enciendo el 18
            time.sleep(0.4) ## Esperamos 0.15 segundo
            GPIO.output(18, False) ## Apago el 18
            time.sleep(0.1)
        time.sleep(0.1) #Hacemos el cambio de letra
        for a in range(3): #3 Puntos para la letra S
            GPIO.output(18, True) ## Enciendo el 18
            time.sleep(0.15) ## Esperamos 0.15 segundo
            GPIO.output(18, False) ## Apago el 18
            time.sleep(0.1)
        time.sleep(2)
        print "Comunicación morse finalizada"
        

# Código principal desde el que usamos todas las funciones
for b in range(3):
    morse()

print("Limpiando la configuración de los GPIO")
GPIO.cleanup() ## Hago una limpieza de los GPIO