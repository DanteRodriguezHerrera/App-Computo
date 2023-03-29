import tkinter as tk
from tkinter import messagebox

global counter_windows
counter_windows = 0
# Colores
color_1 = "#329171"
color_2 = "#4cddac" #"gray95"
color_b = "gray92"
color_3 = "black"
color_4 = "white"
font_1 = "serif"
font_2 = "sans serif"


def callback(ventana):
    global counter_windows
    counter_windows = 0
    #print(counter_windows)
    ventana.destroy()

def handle_focus_in(event):
    event.widget.delete(0, tk.END)
    event.widget.config(fg='black')

def check_window_open():
    global counter_windows
    if counter_windows > 0:
        messagebox.showwarning(message = "Sólo puedes hacer una acción a la vez")
        return True
    else:
        return False
