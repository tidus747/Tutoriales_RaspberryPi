# -*- coding: utf-8 -*-

''' Copyright (C) 2018 Iván Rodríguez Méndez
This software is distributed under the GNU General Public
Licence (version 3 or later); please refer to the file
Licence.txt, included with the software, for details.
'''

# Tutorial creado para el canal de YouTube Piensa 3D
# Tutorial 9: Usar un zumbador como alarma
# Creado por: Iván Rodríguez

from gpiozero import Buzzer
from time import sleep

buzzer = Buzzer(17)

while True:
    buzzer.on()
    sleep(1)
    buzzer.off()
    sleep(1)

'''
while True:
    buzzer.beep()
'''
