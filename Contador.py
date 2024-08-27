from tkinter import *

class Contador(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)
        self.parent = master
        self.grid()
        self.contador = 0
        self.createWidgets()
    
    # Función para incrementar el contador
    def incrementar(self):
        self.contador += 1
        self.entryContador.config(state="normal")#hace editable el campo
        self.entryContador.delete(0,END)#borra valor actual
        self.entryContador.insert(0,str(self.contador))#nuevo valor
        self.entryContador.config(state="readonly")#hace no editable el campo
        

# Función para decrementar el contador
    def decrementar(self):
        self.contador -= 1
        self.entryContador.config(state="normal")#hace editable el campo
        self.entryContador.delete(0,END)#borra valor actual
        self.entryContador.insert(0,str(self.contador))#nuevo valor
        self.entryContador.config(state="readonly")#hace no editable el campo
                

# Función para resetear el contador
    def resetear(self):
       self.contador = 0
       self.entryContador.config(state="normal")#hace editable el campo
       self.entryContador.delete(0,END)#borra valor actual
       self.entryContador.insert(0,str(self.contador))#nuevo valor
       self.entryContador.config(state="readonly")#hace no editable el campo
              

    def createWidgets(self):
        self.label = Label(self, text="Contador", font=("Times New Roman", 12))
        self.label.grid(row=0, column=0, pady=10)

        #lineEdit no editable para n
        self.entryContador = Entry(self, state="readonly", font=("Times New Roman", 12), justify="center")
        self.entryContador.grid(row=0, column=1, columnspan=1, padx=10, pady=10)
        self.entryContador.insert(0,str(self.contador))

        self.btn_incrementar = Button(self, text="Count Up", command=self.incrementar, font=("Times New Roman", 12))
        self.btn_incrementar.grid(row=0, column=2, columnspan=1, pady=10)

        self.btn_decrementar = Button(self, text="Count Down", command=self.decrementar, font=("Times New Roman", 12))
        self.btn_decrementar.grid(row=0, column=3, columnspan=1, pady=10)

        self.btn_resetear = Button(self, text="Reset", command=self.resetear, font=("Times New Roman", 12))
        self.btn_resetear.grid(row=0, column=4, columnspan=1, pady=10)
        


if __name__ == "__main__":
    ventana = Tk()
    ventana.title("Contador")
    ventana.geometry("500x100")
    ventana.resizable(False,False)
    root = Contador(ventana)
    ventana.mainloop()