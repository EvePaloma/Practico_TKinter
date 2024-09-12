from tkinter import *
from tkinter import messagebox 


class Calculadora(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs, bg="ivory4")
        self.master = master
        self.grid()
        self.createWidgets()

    def valNum(self):
        num1 = self.num1.get()
        num2 = self.num2.get()
        try:
            float(num1)
            float(num2)
            return True
        except ValueError:
            messagebox.showerror("Error","Ingrese solo números")
            self.num1.delete(0,END)
            self.num2.delete(0,END)
            return False

    def sumar(self):
        if self.valNum():
            num1 = float(self.num1.get())
            num2 = float(self.num2.get())
            resultado = num1 + num2
            self.resultado.config(state="normal")
            self.resultado.delete(0, END)
            self.resultado.insert(0, str(resultado))
            self.resultado.config(state="readonly")


    def restar(self):
        if self.valNum():
            num1 = float(self.num1.get())
            num2 = float(self.num2.get())
            resultado = num1 - num2
            self.resultado.config(state="normal")
            self.resultado.delete(0, END)
            self.resultado.insert(0, str(resultado))
            self.resultado.config(state="readonly")


    def multiplicar(self):
        if self.valNum():
            num1 = float(self.num1.get())
            num2 = float(self.num2.get())
            resultado = num1 * num2
            self.resultado.config(state="normal")
            self.resultado.delete(0, END)
            self.resultado.insert(0, str(resultado))
            self.resultado.config(state="readonly")        


    def dividir(self):
        if self.valNum():
            num1 = float(self.num1.get())
            num2 = float(self.num2.get())
            resultado = num1 / num2 if num2 != 0 else "Error" 
            self.resultado.config(state="normal")
            self.resultado.delete(0, END)
            self.resultado.insert(0, str(resultado))
            self.resultado.config(state="readonly")


    def porcentaje(self):
        if self.valNum():
            num1 = float(self.num1.get())
            num2 = float(self.num2.get())
            resultado = num1 % num2
            self.resultado.config(state="normal")
            self.resultado.delete(0, END)
            self.resultado.insert(0, str(resultado))
            self.resultado.config(state="readonly")


    def borrar(self):
        self.num1.delete(0, END)
        self.num2.delete(0, END)
        self.resultado.config(state="normal")
        self.resultado.delete(0, END)
        self.resultado.config(state="readonly")    


    def createWidgets(self):
        frame = LabelFrame(self, text="Calculadora", bg="ivory3", fg="black",font=("Times New Roman", 12))
        frame.grid(row=0, column=0, padx=10, pady=10, columnspan=3, sticky="ew") 


        Label1 = Label(frame, text="Primer número",  bg= "ivory2", font=("Times New Roman", 12))   
        Label1.grid(row=1, column=0, padx=10, pady=10)

        Label2 = Label(frame, text="Segundo número", bg= "ivory2", font=("Times New Roman", 12))   
        Label2.grid(row=2, column=0, padx=10, pady=10)

        Label3 = Label(frame, text="Resultado", bg= "ivory2", font=("Times New Roman", 12))   
        Label3.grid(row=3, column=0, padx=10, pady=10)

        self.num1 = Entry(frame, relief = "raised",  font=("Times New Roman", 12))
        self.num1.grid(row=1, column=1, padx=10, pady=10)

        self.num2 = Entry(frame, relief = "raised", font=("Times New Roman", 12))
        self.num2.grid(row=2, column=1, padx=10, pady=10)

        self.resultado = Entry(frame, relief = "raised", font=("Times New Roman", 12))
        self.resultado.grid(row=3, column=1, padx=10, pady=10)

        #botones
        boton1 = Button(frame, text="+", command=self.sumar, bg="ivory2", relief = "raised", font=("Times New Roman",12))
        boton1.grid(row="4", column="0", padx=10,pady=10,sticky="ew")

        boton2 = Button(frame, text="-", command=self.restar, bg="ivory2", relief = "raised", font=("Times New Roman",12))
        boton2.grid(row="4", column="1", padx=10,pady=10,sticky="ew")

        boton3 = Button(frame, text="*", command=self.multiplicar, bg="ivory2", relief = "raised", font=("Times New Roman",12))
        boton3.grid(row="5", column="0", padx=10,pady=10,sticky="ew")

        boton4 = Button(frame, text="/", command=self.dividir, bg="ivory2", relief = "raised", font=("Times New Roman",12))
        boton4.grid(row="5", column="1", padx=10,pady=10,sticky="ew")

        boton5 = Button(frame, text="%", command=self.porcentaje, bg="ivory2", relief = "raised", font=("Times New Roman",12))
        boton5.grid(row="6", column="0", padx=10,pady=10,sticky="ew")

        boton6 = Button(frame, text="CLEAR", command=self.borrar, bg="ivory2", relief = "raised", font=("Times New Roman",12))
        boton6.grid(row="6", column="1", padx=10,pady=10,sticky="ew")

if __name__ == "__main__":
    ventana = Tk()
    ventana.title("Calculadora")
    ventana.resizable(False,False)
    root = Calculadora  (ventana)
    ventana.mainloop()      