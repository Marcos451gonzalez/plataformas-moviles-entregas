#!/usr/bin/env python
# Server.py of 'Remote Desktop'
import socket  # For network connections
import tkinter
import tkinter as tk  # To create a graphical user interface
from random import randint  # To pick a random number
from tkinter.messagebox import showinfo  # To give alerts
from tkinter import Entry,Button,Label,Tk,Text,StringVar
from tkinter import *
from setuptools import Command
import random
from PIL import ImageTk, Image


port = randint(1000, 10000)
k = tk.Tk()
showinfo('Control Data','Host = '+socket.gethostbyname(socket.gethostname())+'\nPort = '+str(port))
k.destroy()
root = tk.Tk()

root.title('Escritorio Remoto Tkinter Python')

image=Image.open("logo.jpg")
image=image.resize((100,100),Image.ANTIALIAS)

img=ImageTk.PhotoImage(image)
lbl_img=Label(root,image=img)
lbl_img.pack()

def helpus():
   print('...')


def changeBG():
    colors = ["black","#ffffff"]
    random_colors = random.choice(colors)
    root.config(background = random_colors)

def agregar():
    lista_elementos.insert(END, entrada.get())
    with open('datos.txt','a') as file:
        file.write(entrada.get() + '\n')
    lista_nombre.insert(END, entrada2.get())
    with open('name.txt','a') as file:
        file.write(entrada2.get() + '\n')

def cargar_datos():
    file = open('datos.txt','r')
    for i in file:
        lista_elementos.insert(END,i)
        print(i)
        file.close
    file = open('name.txt','r')
    for i in file:
        lista_nombre.insert(END,i)
        print(i)
        file.close

root.geometry('700x450')
global x, y, data
host = socket.gethostname()
lista_elementos=Listbox(root, width=50)
lista_elementos.place(x=209,y=210)
lista_nombre=Listbox(root, width=50)
lista_nombre.place(x=279,y=210)
lista_etiq=Label(root,text=" Chat: ",bg="light blue").place(x=210,y=180)
entrada=StringVar()
entrada2=StringVar()
entrada_elementos=Entry(root,text=entrada,width=40).place(x=210,y=380)
entrada_nombre=Entry(root,text=entrada2,width=40).place(x=280,y=380)
boton_añadir=Button(root,text="Enviar",heigh=1,width=18,command=agregar,bg="green").place(x=530,y=380)
boton_bg=Button(root,text="Fondo",heigh=1,width=18,command=changeBG,bg="grey").place(x=10,y=10)
datos = cargar_datos()


server_socket = socket.socket()
server_socket.bind((host, port))
server_socket.listen(2)
conn, address = server_socket.accept()
print("Connection from: " + str(address))
x = 10
y = 10

menubar = tk.Menu(root)
menubar.add_command(label="Salir", command=root.quit)
menubar.add_command(label="Ayuda",command=helpus)

root.config(menu = menubar)
root.mainloop()
# Created by vismodo: https://github.com/vismodo/
# Email: vismaya.atreya@outlook.com
# Repository: https://github.com/vismodo/Remote-Desktop (Remote Desktop)
# Python Version: 3.9
