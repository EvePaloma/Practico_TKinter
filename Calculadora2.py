from tkinter import *
from tkinter import messagebox 

class Calculadora2(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs, bg="ivory4")
        self.master = master
        self.grid()
        self.operacion = StringVar()
        self.createWidgets()

    
    def valNum(self):
        try:
            num1 = float(self.num1.get())
            num2 = float(self.num2.get())
            return num1, num2
        except ValueError:
            messagebox.showerror("Error","Ingrese solo números")
            self.num1.delete(0,END)
            self.num2.delete(0,END)
            return False
    

    def Calcular(self):
        numeros = self.valNum()
        if not numeros:
            return
        
        num1, num2 = numeros
        operacion = self.operacion.get()

        if operacion == "Sumar":
            resultado = num1 + num2
        elif operacion == "Restar":
            resultado = num1 - num2
        elif operacion == "Multiplicar":
            resultado = num1 * num2   
        elif operacion == "Dividir":
            resultado = num1 / num2 if num2 != 0 else "Error"  

        self.resultado.config(state="normal")
        self.resultado.delete(0,END)
        self.resultado.insert(0,str(resultado))
        self.resultado.config(state="readonly")           

    def createWidgets(self):
        frame = LabelFrame(self, text="Calculadora 2", bg="wheat3", fg="black",font=("Times New Roman", 12))
        frame.grid(row=0, column=0, padx=10, pady=10, columnspan=3, sticky="ew") 


        Label1 = Label(frame, text="Valor 1",  bg= "wheat3", font=("Times New Roman", 12))   
        Label1.grid(row=1, column=0, padx=10, pady=10)

        Label2 = Label(frame, text="Valor 2", bg= "wheat3", font=("Times New Roman", 12))   
        Label2.grid(row=2, column=0, padx=10, pady=10)

        Label3 = Label(frame, text="Resultado", bg= "wheat3", font=("Times New Roman", 12))   
        Label3.grid(row=3, column=0, padx=10, pady=10)   

        Label4 = Label(frame, text="Operaciones", bg= "wheat3", font=("Times New Roman", 12))   
        Label4.grid(row=0, column=2, padx=10, pady=10, sticky="w") 

        self.num1 = Entry(frame, relief = "raised",  font=("Times New Roman", 12))
        self.num1.grid(row=1, column=1, padx=10, pady=10)

        self.num2 = Entry(frame, relief = "raised", font=("Times New Roman", 12))
        self.num2.grid(row=2, column=1, padx=10, pady=10)

        self.resultado = Entry(frame,state="readonly", relief = "raised", font=("Times New Roman", 12))
        self.resultado.grid(row=3, column=1, padx=10, pady=10) 

        opcion1 = Radiobutton(frame, text="Sumar",bg="wheat3",font=("Times New Roman", 12),variable=self.operacion, value="Sumar")
        opcion1.grid(row=1, column=2, sticky="w")

        opcion2 = Radiobutton(frame, text="Restar",bg="wheat3",font=("Times New Roman", 12),variable=self.operacion, value="Restar")
        opcion2.grid(row=2, column=2,sticky="w")

        opcion3 = Radiobutton(frame, text="Multiplicar",bg="wheat3",font=("Times New Roman", 12),variable=self.operacion, value="Multiplicar")
        opcion3.grid(row=3, column=2,sticky="w")

        opcion4 = Radiobutton(frame, text="Dividir",bg="wheat3",font=("Times New Roman", 12),variable=self.operacion, value="Dividir")
        opcion4.grid(row=4, column=2,sticky="w")

        boton = Button(frame, text="Calcular", command=self.Calcular, bg="wheat2", relief = "raised", font=("Times New Roman",12))
        boton.grid(row="5", column="1", padx=10,pady=10,sticky="ew")




if __name__ == "__main__":
    ventana = Tk()
    ventana.title("Calculadora 2")
    ventana.resizable(False,False)
    root = Calculadora2  (ventana)
    ventana.mainloop()          