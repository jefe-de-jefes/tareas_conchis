import tkinter as tkt
from tkinter import messagebox

def generar_campos():
    try:
        n = int(entry_n.get())
        if n <= 0:
            raise ValueError
    except ValueError:
        messagebox.showerror('Error', 'Introduzca un numero > 0')
        return
    for 
