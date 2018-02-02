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
verde_peaton = 14
rojo_peaton = 15

pulsador = 22

tiempoCambio = 0
tiempoCruce = 3


def cambioSemaforo():
	print "Parando el tráfico ..."
	GPIO.output(verde, False)
	GPIO.output(amarillo, True)
	time.sleep(2)
	
	GPIO.output(amarillo, False)
	GPIO.output(rojo, True)
	time.sleep(1)
	
	GPIO.output(rojo_peaton, False)
	GPIO.output(verde_peaton, True)
	time.sleep(tiempoCruce)
	
	for i in range(10):
		GPIO.output(verde_peaton, True)
		time.sleep(0.25)
		GPIO.output(verde_peaton, False)
		time.sleep(0.25)
		
	GPIO.output(rojo_peaton, True)
	time.sleep(0.5)
	
	GPIO.output(amarillo, True)
	GPIO.output(rojo, False)
	time.sleep(1)
	
	GPIO.output(verde, True)
	GPIO.output(amarillo, False)
	
	tiempoCambio = time.clock()
	return tiempoCambio 
		
		
        
         
# Código principal desde el que usamos todas las funciones
GPIO.output(verde,True)
GPIO.output(amarillo, False)
GPIO.output(rojo,False)

GPIO.output(verde_peaton,False)
GPIO.output(rojo_peaton,True)

while True:
    estado = GPIO.input(pulsador)

    if (estado == 1 and (time.clock() - tiempoCambio) > 5):
		tiempoCambio=cambioSemaforo()

print("Limpiando la configuración de los GPIO")
GPIO.cleanup() ## Hago una limpieza de los GPIO
