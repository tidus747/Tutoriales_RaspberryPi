#! /usr/bin/env python
#  -*- coding: utf-8 -*-

'''
Interfaz gráfica para el control de LED RGB con Raspberry Pi
Tutorial creado para el canal de YouTube Piensa 3D

Iván Rodríguez 2018
'''

import sys

try:
    from Tkinter import *
except ImportError:
    from tkinter import *

import Tkinter as tk
import GUI_support
import ledFun as led

# Inicializamos los GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(14, GPIO.OUT) ## Color Rojo
GPIO.setup(15, GPIO.OUT) ## Color Verde
GPIO.setup(18, GPIO.OUT) ## Color Azul

# Definimos los colores del led
Colores = np.array([14,15,18]) # Es importante que el orden sea RGB

def App():

    global val, w, root
    root = Tk()
    GUI_support.set_Tk_var()
    top = RGB_LED_Mixer (root)
    GUI_support.init(root, top)
    root.mainloop()

class RGB_LED_Mixer:
    def __init__(self, top=None):

        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#d9d9d9' # X11 color: 'gray85'

        top.geometry("255x165+530+213")
        top.title("RGB LED Mixer")
        top.configure(background="#ffffff")
        top.configure(highlightcolor="black")
        top.resizable(False, False)

        self.Frame1 = Frame(top)
        self.Frame1.place(relx=0.04, rely=0.06, relheight=0.88, relwidth=0.92)
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(background="#ffffff")
        self.Frame1.configure(width=235)

        self.Label1 = Label(self.Frame1)
        self.Label1.place(relx=0.55, rely=0.14, height=79, width=86)
        self.Label1.configure(activebackground="#f9f9f9")
        self._img1 = PhotoImage(file="./Images/led_rojo.png")
        self.Label1.configure(image=self._img1)
        self.Label1.configure(text='''Led''')

        self.Button1 = Button(self.Frame1)
        self.Button1.place(relx=0.04, rely=0.76, height=27, width=217)
        self.Button1.configure(activebackground="#d9d9d9")
        self.Button1.configure(text='''Aplicar''')
        self.Button1.configure(command=self.applyCallback)

        self.Checkbutton1 = Checkbutton(self.Frame1)
        self.Checkbutton1.place(relx=0.04, rely=0.07, relheight=0.14
                , relwidth=0.44)
        self.Checkbutton1.configure(activebackground="#d9d9d9")
        self.Checkbutton1.configure(background="#ffffff")
        self.Checkbutton1.configure(highlightthickness="0")
        self.Checkbutton1.configure(justify=LEFT)
        self.Checkbutton1.configure(text='''Led Rojo''')
        self.Checkbutton1.configure(variable=GUI_support.che44)
        self.Checkbutton1.select()

        self.Checkbutton2 = Checkbutton(self.Frame1)
        self.Checkbutton2.place(relx=0.04, rely=0.28, relheight=0.14
                , relwidth=0.48)
        self.Checkbutton2.configure(activebackground="#d9d9d9")
        self.Checkbutton2.configure(background="#ffffff")
        self.Checkbutton2.configure(highlightthickness="0")
        self.Checkbutton2.configure(justify=LEFT)
        self.Checkbutton2.configure(text='''Led Verde''')
        self.Checkbutton2.configure(variable=GUI_support.che45)
        self.Checkbutton2.select()

        self.Checkbutton3 = Checkbutton(self.Frame1)
        self.Checkbutton3.place(relx=0.04, rely=0.48, relheight=0.13
                , relwidth=0.45)
        self.Checkbutton3.configure(activebackground="#d9d9d9")
        self.Checkbutton3.configure(background="#ffffff")
        self.Checkbutton3.configure(highlightthickness="0")
        self.Checkbutton3.configure(justify=LEFT)
        self.Checkbutton3.configure(text='''Led Azul''')
        self.Checkbutton3.configure(variable=GUI_support.che46)
        self.Checkbutton3.select()


    def applyCallback(self):
        print("Aplicando configuracion...")
        print("Rojo "+GUI_support.che44.get())
        print("Verde "+GUI_support.che45.get())
        print("Azul "+GUI_support.che46.get())
        self.applyColors(int(GUI_support.che44.get()),int(GUI_support.che45.get()),int(GUI_support.che46.get()))
        return

    def applyColors(self,r,g,b):
        if (r == 0 and g == 0 and b == 0 ):
            self.changeImage("apagado")
            led.led_off()
        if (r == 0 and g == 0 and b == 1 ):
            self.changeImage("azul")
            led.led_off_red()
            led.led_off_green()
            led.led_on_blue()
        if (r == 0 and g == 1 and b == 0 ):
            self.changeImage("verde")
            led.led_off_red()
            led.led_on_green()
            led.led_off_blue()
        if (r == 0 and g == 1 and b == 1 ):
            self.changeImage("cyan")
            led.led_off_red()
            led.led_on_green()
            led.led_on_blue()
        if (r == 1 and g == 0 and b == 0 ):
            self.changeImage("rojo")
            led.led_on_red()
            led.led_off_green()
            led.led_off_blue()
        if (r == 1 and g == 0 and b == 1 ):
            self.changeImage("violeta")
            led.led_on_red()
            led.led_off_green()
            led.led_on_blue()
        if (r == 1 and g == 1 and b == 0 ):
            self.changeImage("amarillo")
            led.led_on_red()
            led.led_on_green()
            led.led_off_blue()
        if (r == 1 and g == 1 and b == 1 ):
            self.changeImage("blanco")
            led.led_on_red()
            led.led_on_green()
            led.led_on_blue()
        return

    def changeImage(self,name):
        self._img1 = PhotoImage(file="./Images/led_"+name+".png")
        self.Label1.configure(image=self._img1)
        return


if __name__ == '__main__':
    App()
