from tkinter import Button,Label, Tk, Entry, END

ventana = Tk()
ventana.geometry('270x100')
ventana.title('ContCreciente')
ventana.resizable(0,0)

def contadorDecreciente():
    valor= int(contador.get()) 
    valor_nuevo = valor -1
    contador.config(state="normal")
    contador.delete(0, END)
    contador.insert(0, str(valor_nuevo))
    contador.config(state="readonly")


etiqueta = Label(ventana, text= "Contador", font= ('Times New Roman',12 ))
etiqueta.grid(row=3, column=1, padx=5, pady=5, sticky='e') 


contador = Entry(ventana,  width=12, relief = "raised",font= ('Times New Roman',12 ))
contador.insert(0,88)
contador.config(state="readonly")
contador.grid(row=3, column=2, padx=5, pady=5, sticky='w') 


btn = Button(ventana, text="-", command=contadorDecreciente, width=5, font= ('Times New Roman',12 ))
btn.grid(row=3, column=3, padx=10, pady=10, sticky='w') 


ventana.mainloop()