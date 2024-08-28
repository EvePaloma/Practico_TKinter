from tkinter import *
import random
from tkinter import messagebox


class GeneradorNumeros(Frame):
    def __init__(self,master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs, bg="plum4")
        self.master = master
        self.grid()
        self.resultado = StringVar()
        self.createWidgets()


    def generarNumero(self):
        try:
           num_min = int(self.num_min.get())
           num_max = int(self.num_max.get())
           self.resultado.set("")
           if num_min > num_max:
              messagebox.showwarning("Error","Número 1 no puede ser mayor a número 2")
              self.resultado.set("")
           elif num_min == num_max:
               messagebox.showwarning("Error","Número 1 y número 2 no pueden ser iguales")
               self.resultado.set("")
           else:
               num_generado = random.randint(num_min,num_max)
               self.resultado.set(str(num_generado))
        except ValueError:
            messagebox.showwarning("Error","Ingrese valores enteros")
            self.resultado.set("")        
               
         
    def createWidgets(self):
        frame = LabelFrame(self, text="Generador de números", bg="plum3", fg="black",font=("Times New Roman", 12))
        frame.grid(row=0, column=0, padx=10, pady=10, columnspan=3, sticky="ew")  

        label1 = Label(frame, text="Número 1",bg="plum3",font=("Times New Roman", 12))
        label1.grid(row=1, column=0, padx=5, pady=5)

        label2 = Label(frame, text="Número 2",bg="plum3",font=("Times New Roman", 12))
        label2.grid(row=2, column=0, padx=5, pady=5)   

        label3 = Label(frame, text="Número generado",bg="plum3",font=("Times New Roman", 12))
        label3.grid(row=0, column=0, padx=5, pady=5)  

        self.num_min = Spinbox(frame, from_=0, to=99999,relief = "raised", font=("Times New Roman", 12)) 
        self.num_min.grid(row=1, column=1, padx=5, pady=5)   

        self.num_max = Spinbox(frame, from_=0, to=99999,relief = "raised", font=("Times New Roman", 12)) 
        self.num_max.grid(row=2, column=1, padx=5, pady=5)  

        self.num_resultado = Entry(frame, textvariable=self.resultado, state="readonly", font=("Times New Roman", 12))
        self.num_resultado.grid(row=3, column=1, padx=5, pady=5)

        boton = Button(frame, text="Generar", command=self.generarNumero, bg="plum2", relief = "raised", font=("Times New Roman",12))
        boton.grid(row="4", column="1", padx=5,pady=5)
           

if __name__ == "__main__":
    ventana = Tk()
    ventana.title("")
    ventana.resizable(False,False)
    root = GeneradorNumeros(ventana)
    ventana.mainloop()    