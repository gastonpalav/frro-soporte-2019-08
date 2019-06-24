## 1 Ejercicio Hacer un formulario tkinter que es una calculadora, tiene 2 entry para ingresar los valores V1 y V2.
## Y 4 botones de operaciones para las operaciones respectivas + , - , * , / ,
## al cliquearlos muestre el resultado de aplicar el operador respectivo en los V1 y V2 . 
 


import tkinter as tk
##from tkinter import *
from tkinter import messagebox , font , Entry , Label , ttk , DoubleVar , LEFT , CENTER , TOP

#defino las operaciones 
def suma():
    try :
        v1 = float(txtNro1.get())
        v2 = float(txtNro2.get())
        resultado = v1 + v2
    except :
        print(messagebox.askretrycancel(message="¿Desea reintentar?", title="ERROR"))
    else:
        print(messagebox.showinfo(message="El resultado de la operación es  %.2f"  %resultado , title="RESULTADO"))

def resta():
    try:
        v1 = float(txtNro1.get())
        v2 = float(txtNro2.get())
        resultado = v1 - v2
    except : 
        print(messagebox.askretrycancel(message="ERROR !!¿Desea reintentar?", title="ERROR"))
    else:
        print(messagebox.showinfo(message="El resultado de la operación es %.2f " %resultado , title="RESULTADO"))
    
def multiplicacion():
    try :
        v1 = float(txtNro1.get())
        v2 = float (txtNro2.get())
        resultado = v1 * v2
    except : 
        print(messagebox.askretrycancel(message="ERROR !!¿Desea reintentar?", title="ERROR"))
    else:
        print(messagebox.showinfo(message="El resultado de la operación es %.2f  " %resultado , title="RESULTADO"))

def division():
    try:
        v1 = float(txtNro1.get())
        v2 = float(txtNro2.get())
        resultado = v1 / v2
        #Division por cero
    except ZeroDivisionError :
        print(messagebox.showerror(title="ERROR", message="DIVISIÓN POR 0 INEXISTENTE"))
    except:
        print(messagebox.askretrycancel(message="ERROR !!¿Desea reintentar?", title="ERROR"))
    else:
        print(messagebox.showinfo(message="El resultado de la operación es %.2f " %resultado , title="RESULTADO"))


## definiendo controles
#Instancia ventana
root = tk.Tk()
root.resizable(width=False, height=False)
#Titulo
root.title("Calculadora")
#Tamaño del root 
root.geometry('500x250')
#Definición variables de ingreso
txtNro1 = DoubleVar()
txtNro2 = DoubleVar()
txtNro1.set(0)
txtNro2.set(0)
#Letra
ft = font.Font(family="Helvetica", size=12, weight="bold")
#Los txt de input
entry1 = Entry(root, textvariable = txtNro1 , justify=tk.CENTER )
entry2 = Entry(root, textvariable  = txtNro2 , justify=tk.CENTER )
#Mensajes
lblOper1 = Label(root , text= "Primer Operando", font = ft)
lblOper2 = Label(root , text= "Segundo Operando" , font = ft)
#Botones
btnSuma = ttk.Button(root, text = "+" , command = suma)
btnResta = ttk.Button(root, text = "-" , command = resta)
btnMultiplicacion = ttk.Button(root, text = "*" , command = multiplicacion)
btnDiv = ttk.Button(root, text="/", command = division)

# a ver
lblOper1.place(x = 50 , y = 25)
lblOper2.place(x= 250 , y = 25)
entry1.place(x = 50 , y = 65)
entry2.place(x=250 , y = 65)
btnSuma.place(x= 50 , y= 150)
btnResta.place(x= 150, y= 150 )
btnMultiplicacion.place(x= 250, y= 150)
btnDiv.place(x= 350, y= 150)

#corriendo
root.mainloop()
