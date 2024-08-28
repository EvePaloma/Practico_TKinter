from tkinter import * 
from tkinter import messagebox


class Peliculas(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs, bg="plum4")
        self.master = master
        self.grid()
        self.createWidgets()

    
    def agregarPeliculas(self):
        titulo = self.titulo_pelicula.get().strip()
        #verifica que el campo no este vacio
        if titulo:
            #si titulo no esta vacio, lo agrega al final de la lista
            self.lista_peliculas.insert(END,titulo)  
            #borra el contenido del campo para que este vacio despues de añadir peli
            self.titulo_pelicula.delete(0,END)
        #si el campo de entrada esta vacio muestra un msj    
        else:
            messagebox.showwarning("Error","Escribe el nombre de una película antes de añadirla.")
            


    def createWidgets(self):
        frame = LabelFrame(self, text="Añadir Peliculas", bg="plum3", fg="black",font=("Times New Roman", 12))
        frame.grid(row=0, column=0, padx=10, pady=10, columnspan=3, sticky="ew")  

        label_titulo = Label(frame, text="Escribe el titulo de la película:",bg="plum3",font=("Times New Roman", 12))
        label_titulo.grid(row=0, column=0, padx=5, pady=5)

        label_lista = Label(frame, text= "Peliculas",bg="plum3",font=("Times New Roman", 12))    
        label_lista.grid(row=0, column=1, padx=5, pady=5)
        
        self.titulo_pelicula = Entry(frame, relief = "raised", width=30)
        self.titulo_pelicula.grid(row=2, column=0,padx=5, pady=5, sticky="n")

        self.lista_peliculas = Listbox(frame, relief = "raised",width=30, height=10)
        self.lista_peliculas.grid(row=2, column=1, padx=5, pady=5)

        boton = Button(frame, text="Añadir", command=self.agregarPeliculas, bg="plum2", relief = "raised", font=("Times New Roman",12))
        boton.grid(row="2", column="0", padx=5,pady=5)

if __name__ == "__main__":
    ventana = Tk()
    ventana.title("Peliculas")
    ventana.resizable(False,False)
    root = Peliculas (ventana)
    ventana.mainloop()                  