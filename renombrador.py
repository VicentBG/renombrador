from tkinter import *

from tkinter import scrolledtext, messagebox

import sys

import os

import datetime as dt

PATH = os.getcwd()

def leer_ficheros():
    with os.scandir(PATH) as ficheros:
        ficheros = [fichero.name for fichero in ficheros if fichero.is_file and (fichero.name.endswith('pdf') or fichero.name.endswith('PDF'))]
    return ficheros

def renombrar(num: int):
    hoy = dt.datetime.now()
    fecha = hoy.strftime('%y%m%d%H%M')
    for i, f in enumerate(ficheros):
        archivo = f'{PATH}\\{f}'
        nuevo = f'{PATH}\\FP{fecha}_{num+i}.pdf'
        os.rename(archivo, nuevo)

window = Tk()

window.geometry('600x700')

window.title("Bienvenida a la app para renombrar ficheros PDF")

lbl_files = Label(window, text="LISTA DE ARCHIVOS PDF", font=("Arial Bold", 15))

lbl_files.grid(column=1, row=0)

txt_files = scrolledtext.ScrolledText(window,width=40,height=40)

txt_files.grid(column=1,row=1)

def fill_files(ficheros):
    txt_files.delete(1.0,END)
    for f in ficheros:
        txt_files.insert(INSERT, f + '\n')

ficheros = leer_ficheros()

fill_files(ficheros)

def clicked_can():
    sys.exit()

btn_can = Button(window, text="Cancelar", command=clicked_can)

btn_can.grid(column=1, row=2)

lbl_number = Label(window, text="SIGUIENTE Nº ESCANER", font=("Arial Bold", 15))

lbl_number.grid(column=2, row=0)

txt_number = Entry(window,width=10)

txt_number.grid(column=2,row=1)

txt_number.focus()

def clicked_ren():
    num = txt_number.get()
    ok = messagebox.askyesno('ATENCION','El número ' + num + ' indicado, ¿es correcto?')
    if ok and num.isdigit():
        renombrar(int(num))
        ficheros = leer_ficheros()
        fill_files(ficheros)
        messagebox.showwarning('ATENCION', 'Los archivos han sido renombrados.')

btn_ren = Button(window, text="Renombrar", command=clicked_ren)

btn_ren.grid(column=2, row=2)

window.mainloop()