from tkinter import *
import random
from tkinter import messagebox 

class JuegoMatematico(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs,bg="#e2b5f5")
        self.master = master
        self.grid()
        self.juegos = IntVar()
        self.buenos = IntVar()
        self.malos = IntVar()
        self.operador = StringVar()
        self.dificultad = IntVar()
        self.createWidgets()

    def nuevoJuego(self):
        #verificar dificultad seleccionada
        if self.dificultad.get() == 1:
            limite = 10
        elif self.dificultad.get() == 2:
            limite = 100
        elif self.dificultad.get() == 3:
            limite = 1000
        else:
            limite = 10 #por defecto si no elige dificultad 

        #genera 2 num aleatorios
        self.generado1 = random.randint(0,limite)
        self.generado2 = random.randint(1,limite)

        #se le asigna los num generados a las cajas de texto
        self.num1.config(state="normal")
        self.num1.delete(0,END)
        self.num1.insert(0,str(self.generado1))
        self.num1.config(state="readonly")

        self.num2.config(state="normal")
        self.num2.delete(0,END)
        self.num2.insert(0,str(self.generado2))
        self.num2.config(state="readonly")

        #selecciona un operador aleatorio
        operadores = ["+","-","*","/"]
        operador_seleccionado = random.choice(operadores)
        self.operador.set(operador_seleccionado)

        #devuelve el valor actualizado de la etiqueta del operador
        self.signo.config(text=self.operador.get())          

        #limpia campo de resultado
        self.resultado.delete(0,END)

        #limpia el campo de msjs
        self.msj.config(text="")


    def valNum(self,resultado):
        #validar entrada
        if resultado == "":
            messagebox.showerror("Error","Ingrese un resultado")
            return False
        #convierte el valor a float
        try:
            float(resultado)
            return True
        #si no se convierte es porque puede ser letra o caracter
        except ValueError:
            messagebox.showerror("Error","Ingrese solo números válidos:\nSi es decimal, separar con (.)")
            return False


    def verificarResultado(self):
        #validamos entrada
        if self.valNum(self.resultado.get()):
            #convierte el valor de resultado en float y lo asigna a variable resultado_ingresado
            resultado_ingresado = float(self.resultado.get())
                           
        #calcula segun el operador
        if self.operador.get() == "+":
            resultado_correcto = self.generado1 + self.generado2
        elif self.operador.get() == "-":
            resultado_correcto = self.generado1 - self.generado2
        elif self.operador.get() == "*":
            resultado_correcto = self.generado1 * self.generado2
        elif self.operador.get() == "/":
            resultado_correcto = self.generado1 / self.generado2
        else:
            messagebox.showwarning("Error","Operador no válido")
            return
        
        resultado_correcto = round(resultado_correcto,2)
        resultado_ingresado = round(resultado_ingresado,2)

        if resultado_ingresado == resultado_correcto:
            self.buenos.set(self.buenos.get() + 1)
            self.msj.config(text="Correcto!")
        else:
            self.malos.set(self.malos.get() + 1)
            self.msj.config(text=f"Incorrecto. El resultado correcto es:{resultado_correcto}")

        self.juegos.set(self.juegos.get() + 1)

    def reiniciar(self):
        self.juegos.set(0)
        self.buenos.set(0)
        self.malos.set(0)
        self.num1.config(state="normal")
        self.num1.delete(0,END)
        self.num1.config(state="readonly")
        self.num2.config(state="normal")
        self.num2.delete(0,END)
        self.num2.config(state="readonly")
        self.resultado.delete(0,END)
        self.signo.config(text="")
        self.msj.config(text="")       
        
    def createWidgets(self): 
        frame = LabelFrame(self,text="Matemáticas", bg="#f3cbf7", fg="black",font=("Times New Roman", 13),borderwidth=5)
        frame.grid(row=0, column=0, padx=10, pady=10) 

        frame_resultado = LabelFrame(frame, bg="#f3cbf7", fg="black",font=("Times New Roman", 13),borderwidth=5)
        frame_resultado.grid(row=2, column=4, rowspan=2, padx=10, pady=10) 
        
        juegos = Label(frame, text="Juegos:",bg="#f3cbf7",font=("Times New Roman", 13))
        juegos.grid(row=5, column=4, padx=5, pady=5) 

        buenos = Label(frame, text="Buenos:",bg="#f3cbf7",font=("Times New Roman", 13))
        buenos.grid(row=6, column=4, padx=5, pady=5)

        malos = Label(frame, text="Malos:",bg="#f3cbf7",font=("Times New Roman", 13))
        malos.grid(row=7, column=4, padx=5, pady=5) 

        cant_juegos = Label(frame, textvariable=self.juegos,bg="#f3cbf7",font=("Times New Roman", 13))
        cant_juegos.grid(row=5, column=5, padx=5, pady=5) 

        cant_buenos = Label(frame, textvariable=self.buenos,bg="#f3cbf7",font=("Times New Roman", 13))
        cant_buenos.grid(row=6, column=5, padx=5, pady=5)

        cant_malos = Label(frame, textvariable=self.malos,bg="#f3cbf7",font=("Times New Roman", 13), anchor="w")
        cant_malos.grid(row=7, column=5, padx=5, pady=5) 

        self.num1 = Entry(frame, state="readonly", font=("Times New Roman", 13),justify="center")
        self.num1.grid(row=2,column=0, padx=5, pady=5,sticky="e")

        self.num2 = Entry(frame, state="readonly", font=("Times New Roman", 13),justify="center")
        self.num2.grid(row=2,column=2, padx=5, pady=5, sticky="w")

        self.signo = Label(frame, text="?",bg="#f3cbf7",fg="black",font=("Times New Roman", 18))
        self.signo.grid(row=2, column=1,padx=3, pady=3)

        self.resultado = Entry(frame_resultado, state="normal", width=10, font=("Times New Roman", 13))
        self.resultado.grid(row=4,column=4, padx=5, pady=5)

        boton_resultado = Button(frame_resultado, text="Resultado", command=self.verificarResultado, bg="#e2b5f5", relief = "raised", font=("Times New Roman",13))
        boton_resultado.grid(row="5", column="4", padx=10,pady=10,sticky="ew")

        operador_sumar = Radiobutton(frame, text="Sumar", variable=self.operador, value="+",bg="#f3cbf7",font=("Times New Roman", 13), state="disabled")
        operador_sumar.grid(row=5, column=0, padx=20,pady=5,sticky="w")

        operador_restar = Radiobutton(frame, text="Restar", variable=self.operador, value="-",bg="#f3cbf7",font=("Times New Roman", 13), state="disabled")
        operador_restar.grid(row=6, column=0, padx=20,pady=5,sticky="w")

        operador_multiplicar = Radiobutton(frame, text="Multiplicar", variable=self.operador, value="*",bg="#f3cbf7",font=("Times New Roman", 13), state="disabled")
        operador_multiplicar.grid(row=7, column=0, padx=20,pady=5,sticky="w")

        operador_dividir = Radiobutton(frame, text="Dividir", variable=self.operador, value="/",bg="#f3cbf7",font=("Times New Roman", 13), state="disabled")
        operador_dividir.grid(row=8, column=0, padx=20,pady=5,sticky="w")

        dificultad = Radiobutton(frame, text="Fácil", variable=self.dificultad, value=1,bg="#f3cbf7",font=("Times New Roman", 13))
        dificultad.grid(row=1, column=1, padx=5,pady=5,sticky="w")

        dificultad = Radiobutton(frame, text="Medio", variable=self.dificultad, value=2,bg="#f3cbf7",font=("Times New Roman", 13))
        dificultad.grid(row=1, column=2, padx=5,pady=5)

        dificultad = Radiobutton(frame, text="Difícil", variable=self.dificultad, value=3,bg="#f3cbf7",font=("Times New Roman", 13))
        dificultad.grid(row=1, column=3, padx=5,pady=5,sticky="e")

        boton_num_nuevo = Button(frame, text="Nuevo Número", command=self.nuevoJuego, bg="#e2b5f5", relief = "raised", font=("Times New Roman",13))
        boton_num_nuevo.grid(row="5", column="2", padx=10,pady=10,sticky="ew")

        self.msj = Label(frame, text="",bg="#f3cbf7",font=("Times New Roman", 15))
        self.msj.grid(row=9, column=0, columnspan=6, padx=10, pady=10)

        boton_reiniciar = Button(frame, text="Reiniciar Juego", command=self.reiniciar, bg="#e2b5f5", relief = "raised", font=("Times New Roman",13))
        boton_reiniciar.grid(row="6", column="2", padx=10,pady=10,sticky="ew")


if __name__ == "__main__":
    ventana = Tk()
    ventana.title("Juego Matemático")
    ventana.geometry("+400+120")
    ventana.resizable(False,False)
    root = JuegoMatematico (ventana)
    ventana.mainloop()             
            
        


