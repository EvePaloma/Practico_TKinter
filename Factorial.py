from tkinter import *
from math import factorial as calc_factorial

class Factorial(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self,master,*args,**kwargs)
        self.master = master
        self.grid()
        self.n = 0
        self.create_Widgets()
        

    def calcular_Factorial(self):
        self.n += 1 
        
        #actualiza el valor de n y su factorial
        self.entry_n.config(state="normal")#editable para actualizar valor
        self.entry_n.delete(0,END) #borra n actual
        self.entry_n.insert(0, str(self.n))#nuevo valor de n
        self.entry_n.config(state="readonly") #se vuelve a hacer campo no editable

        #calcula factorial de n y lo muestra
        valor_factorial = calc_factorial(self.n)
        self.entry_factorial.config(state="normal")
        self.entry_factorial.delete(0,END)
        self.entry_factorial.insert(0,str(valor_factorial)) 
        self.entry_factorial.config(state="readonly")

    def create_Widgets(self):
        #etiqueta n
        self.label_n = Label(self, text="n", font=("Times New Roman", 12))
        self.label_n.grid(row=0, column=1, padx=10, pady=10)

        #lineEdit no editable para n
        self.entry_n = Entry(self, state="readonly", font=("Times New Roman", 12), justify="center")
        self.entry_n.grid(row=0, column=2, padx=10, pady=10)
        self.entry_n.insert(0,str(self.n))

        #etiqueta factorial(n)
        self.label_factorial = Label(self, text="Factorial", font=("Times New Roman", 12))
        self.label_factorial.grid(row=0, column=3, padx=10, pady=10)

        #lineEdit no editable para factorial
        self.entry_factorial = Entry(self, state="readonly", font=("Times New Roman", 12), justify="center")
        self.entry_factorial.grid(row=0, column=4, padx=10, pady=10)
        self.entry_factorial.insert(0, str(calc_factorial(self.n)))

        #boton
        self.btn_siguiente = Button(self, text="Siguiente", command=self.calcular_Factorial, font=("Times New Roman", 12))
        self.btn_siguiente.grid(row=0, column=5, columnspan=2, pady=10)

if __name__ == "__main__":
    ventana = Tk()
    ventana.title("Factorial")
    ventana.resizable(False,False)
    app = Factorial(ventana)
    ventana.mainloop()

        




