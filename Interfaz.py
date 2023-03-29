import tkinter as tk
from tkinter import font as tkfont
from tkinter import ttk

from config.interfaz_config import *
import os
from tkinter import messagebox
#from PIL import ImageTk, Image

from functools import partial

from interfaces.branches import add_branch_window, update_branch_window, delete_branch_window
from interfaces.loans import add_loan_window, update_loan_window, delete_loan_window


import operaciones as op
import datetime as dt

class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.minsize(600, 800)
        self.title("Banco UACH")
        op.conexion(self)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic",)

        self.photo = tk.PhotoImage(file = os.getcwd()+"\\images\\uach.png")
        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        

        self.frames = {}
        for F in (StartPage, Branch, Loan, ShowLoans, ShowBranches, LoansOnBranch):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class StartPage(tk.Frame):
    
    def __init__(self, parent, controller):

        self.b_width = 20
        self.controller = controller

        ##INICIA LO QUE METI
        #-----------------------------------------------------------------------------------
        tk.Frame.__init__(self, parent,bg=color_1)
        

        # Botones frame
        frame_2 = tk.Frame(self, bg = color_2)
        frame_2.place(x=0, y=0, width=200, height = 100)
        frame_2.pack(fill =tk.BOTH,side=tk.BOTTOM,expand=False, padx=5, pady=5,anchor=tk.S)

        mini_frame_1 = tk.Frame(frame_2, bg = color_2)
        mini_frame_1.pack(padx=10,pady=10, side=tk.LEFT, fill=tk.BOTH, expand=True)

        mini_frame_2 = tk.Frame(frame_2, bg = color_2)
        mini_frame_2.pack(padx=10,pady=10,side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Datos del equipo
        titulo_consulta2 = tk.Label(self, text="Proyecto Primer Parcial", bg = color_1, fg = color_4, font='Helvetica 18 bold')
        titulo_consulta2.pack()
        titulo = tk.Label(self, text="Bases de datos distribuidas\n En este programa se simula\n un sistema de banco el cual \ntrabaja sobre bases de datos distribuidas SQL", bg = color_1, fg = color_4, font='Helvetica 16')
        titulo.pack()
        titulo_consulta = tk.Label(self, text="Integrantes", bg = color_1, fg = color_4, font='Helvetica 18 bold')
        titulo_consulta.pack()
        integrantes = tk.Label(self, text="José Carlos Chaparro Morales - 329613\nJuan Luis Del Valle Sotelo - 338912\nDante Yahir Rodriguez Herrera - 338725", bg = color_1, fg = color_4, font='Helvetica 16')
        integrantes.pack()
        resultado_sulta = tk.Label(self, text="Docente", bg = color_1, fg = color_4, font='Helvetica 18 bold')
        resultado_sulta.pack()
        profe = tk.Label(self, text="M. A. José Saúl De Lira Miramontes", bg = color_1, fg = color_4, font='Helvetica 16')
        profe.pack()

        label1 = tk.Label(self, image = controller.photo)
        label1.pack(pady=40)

        #-----------------------------------------------------------------------------------
        ##TERMINA LO QUE METI
        branches_window = tk.Button(mini_frame_1, text='Sucursal', font=(font_1, 12), bd=2, command=lambda: controller.show_frame("Branch") , cursor="hand2", bg=color_b,fg=color_3,width=self.b_width).pack( padx=5, pady=5, side=tk.TOP, anchor=tk.CENTER)

        loans_window = tk.Button(mini_frame_1, text='Préstamo', font=(font_1, 12), bd=2, command=lambda: controller.show_frame("Loan") , cursor="hand2", bg=color_b,fg=color_3,width=self.b_width).pack( padx=5, pady=5, side=tk.TOP, anchor=tk.CENTER)

        all_branches_window = tk.Button(mini_frame_2, text='Ver sucursales', font=(font_1, 12), bd=2, command=lambda: controller.show_frame("ShowBranches"), cursor="hand2", bg=color_b,fg=color_3,width=self.b_width).pack( padx=5, pady=5, side=tk.TOP, anchor=tk.CENTER)

        loans_branch_window = tk.Button(mini_frame_1, text='Préstamos por sucursal', font=(font_1, 12), bd=2, command=lambda: controller.show_frame("LoansOnBranch") , cursor="hand2", bg=color_b,fg=color_3,width=self.b_width).pack( padx=5, pady=5, side=tk.TOP, anchor=tk.CENTER)

        all_loans_window = tk.Button(mini_frame_2, text='Ver préstamos', font=(font_1, 12), bd=2, command=lambda: controller.show_frame("ShowLoans") , cursor="hand2", bg=color_b,fg=color_3,width=self.b_width).pack( padx=5, pady=5, side=tk.TOP, anchor=tk.CENTER)


class Branch(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg=color_1)
        self.controller = controller
        label = tk.Label(self, text="Dar de alta Sucursales", font=controller.title_font, bg=color_1, fg=color_4)
        label.pack(side=tk.TOP, fill="x", pady=10)
        

        add_branch_bt = tk.Button(self, text='Añadir sucursal', font=(font_1, 12), bd=2, command=partial(add_branch_window,controller) , cursor="hand2", bg=color_b,fg=color_3,width=25).pack( padx=5, pady=5)

        update_branch_bt = tk.Button(self, text='Modificar sucursal', font=(font_1, 12), bd=2, command=partial(update_branch_window, controller), cursor="hand2", bg=color_b,fg=color_3,width=25).pack( padx=5, pady=5)

        delete_branch_bt = tk.Button(self, text='Borrar sucursal', font=(font_1, 12), bd=2, command=partial(delete_branch_window, controller),cursor="hand2", bg=color_b,fg=color_3,width=25).pack(padx=5, pady=5)

        button = tk.Button(self, text="Atras",font=(font_1, 12),command=lambda: controller.show_frame("StartPage"))
        button.pack()


class Loan(tk.Frame):
    
        def __init__(self, parent, controller):
            tk.Frame.__init__(self, parent, bg=color_1)
            self.controller = controller
            label = tk.Label(self, text="Dar de alta Préstamos", font=controller.title_font, bg=color_1, fg=color_4)
            label.pack(side="top", fill="x", pady=10)

            add_loan_bt = tk.Button(self, text='Añadir préstamo', font=(font_1, 12), bd=2, command=partial(add_loan_window, controller) , cursor="hand2", bg=color_b,fg=color_3,width=25).pack( padx=5, pady=5)

            update_loan_bt = tk.Button(self, text='Modificar préstamo', font=(font_1, 12), bd=2, command=partial(update_loan_window, controller), cursor="hand2", bg=color_b,fg=color_3,width=25).pack(   padx=5, pady=5)
        
            delete_loan_bt = tk.Button(self, text='Borrar préstamo', font=(font_1, 12), bd=2, command=partial(delete_loan_window,controller),cursor="hand2", bg=color_b,fg=color_3,width=25).pack(padx=5, pady=5)

            button = tk.Button(self, text="Atras",font=(font_1, 12),command=lambda: controller.show_frame("StartPage"))
            button.pack()
            
class ShowLoans(tk.Frame):
    
        def __init__(self, parent, controller):
            tk.Frame.__init__(self, parent, bg=color_1)
            self.controller = controller
            label = tk.Label(self, text="Mostrar prestamos", font=controller.title_font, bg=color_1, fg=color_4)
            label.pack(side="top", fill="x", pady=10)

            consultar_prestamos_bt = tk.Button(self, text='Consultar prestamos', command=op.show_all_loans)
            consultar_prestamos_bt.pack( padx=5, pady=5)

            button = tk.Button(self, text="Atras",font=(font_1, 12),command=lambda: controller.show_frame("StartPage"))
            button.pack()

class ShowBranches(tk.Frame):
    
        def __init__(self, parent, controller):
            tk.Frame.__init__(self, parent, bg=color_1)
            self.controller = controller
            label = tk.Label(self, text="Mostrar sucursales", font=controller.title_font, bg=color_1, fg=color_4)
            label.pack(side="top", fill="x", pady=10)

            consultar_sucursal_bt = tk.Button(self, text='Consultar sucursales', command=op.show_all_branches)
            consultar_sucursal_bt.pack( padx=5, pady=5)

            button = tk.Button(self, text="Atras",font=(font_1, 12),command=lambda: controller.show_frame("StartPage"))
            button.pack() 

class LoansOnBranch(tk.Frame):
    
        def __init__(self, parent, controller):
            tk.Frame.__init__(self, parent, bg=color_1)
            self.controller = controller
            label = tk.Label(self, text="Prestamos por sucursal", font=controller.title_font, bg=color_1, fg=color_4)
            label.pack(side="top", fill="x", pady=10)

            consultar_pres_suc_bt = tk.Button(self, text='Consultar prestamos de una sucursal', font=(font_1, 12), bd=2, command=op.show_all_loans_on_branch , cursor="hand2", bg=color_b,fg=color_3,width=30)
            consultar_pres_suc_bt.pack( padx=5, pady=5)

            button = tk.Button(self, text="Atras",font=(font_1, 12),command=lambda: controller.show_frame("StartPage"))
            button.pack()  


if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()