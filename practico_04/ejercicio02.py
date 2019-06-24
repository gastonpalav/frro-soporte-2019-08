## 2 Ejercicio Hacer un formulario en Tkinter una calculadora que tenga 1 entry y 12 botones para los dígitos 0 al 9
## y las operaciones + - / * = , que al apretar cada botón vaya agregando al valor que muestra en el entry el carácter
## que le corresponde ( como se ve imagen ) y cuando se aprieta en = pone el resultado de evaluar la cadena entrada .

import tkinter as tk
##from tkinter import *
from tkinter import messagebox , font , Entry , Label , ttk , StringVar , LEFT , CENTER , TOP

def cls():
    iOperacion.set(str())
def btnceroclick():
    txt =iOperacion.get()
    iOperacion.set(txt+'0')
def btnunoclick():
    txt= iOperacion.get()
    iOperacion.set(txt+'1')
def btndosclick():
    txt=iOperacion.get()
    iOperacion.set(txt+'2')
def btntresclick():
    txt=iOperacion.get()
    iOperacion.set(txt+'3')
def btncuatroclick():
    txt=iOperacion.get()
    iOperacion.set(txt+'4')
def btncincoclick():
    txt=iOperacion.get()
    iOperacion.set(txt+'5')
def btnseisclick():
    txt=iOperacion.get()
    iOperacion.set(txt+'6')
def btnsieteclick():
    txt=iOperacion.get()
    iOperacion.set(txt+'7')
def btnochoclick():
    txt=iOperacion.get()
    iOperacion.set(txt+'8')
def btnnueveclick():
    txt=iOperacion.get()
    iOperacion.set(txt+'9')

def suma():
    txt=iOperacion.get()
    iOperacion.set(txt+'+')
def resta():
    txt=iOperacion.get()
    iOperacion.set(txt+'-')
def division():
    txt=iOperacion.get()
    iOperacion.set(txt+'/')
def multiplicacion():
    txt = iOperacion.get()
    iOperacion.set(txt+'*')

def operacion():
    try:
        txt = iOperacion.get()
        iOperacion.set(eval(txt))
    except ZeroDivisionError :
        print(messagebox.showerror(title="ERROR", message="DIVISIÓN POR 0 INEXISTENTE"))
    except:
        print(messagebox.askretrycancel(message="ERROR !!¿Desea reintentar?", title="ERROR"))


root = tk.Tk()
root.resizable(width=False,height=False)
root.title("Calculadora")
root.geometry("400x275")
ft = font.Font(family="Helvetica", size=12, weight="bold")
iOperacion = StringVar()
txtEntry= Entry(root, textvariable = iOperacion, width=44 ,justify= tk.RIGHT)
btn0 = ttk.Button(root, text="0",command = btnceroclick)
btn1 = ttk.Button(root, text="1", command = btnunoclick)
btn2 = ttk.Button(root, text="2", command = btndosclick)
btn3 = ttk.Button(root, text="3", command = btntresclick)
btn4 = ttk.Button(root, text="4",command = btncuatroclick)
btn5 = ttk.Button(root, text="5", command = btncincoclick)
btn6 = ttk.Button(root, text="6", command = btnseisclick)
btn7 = ttk.Button(root, text="7", command = btnsieteclick)
btn8 = ttk.Button(root, text="8", command = btnochoclick)
btn9 = ttk.Button(root, text="9", command = btnnueveclick)
btnSum = ttk.Button(root, text="+",command = suma )
btnResta = ttk.Button(root, text="-", command = resta)
btnMulti = ttk.Button(root, text="*", command = multiplicacion)
btnDiv = ttk.Button(root, text="/", command = division)
btnOper= ttk.Button(root, text="=", command = operacion)
btnBorrar= ttk.Button(root, text="C", command = cls)
txtEntry.place(x=10, y=20)
btn7.place(x=10, y=70)
btn8.place(x=100, y=70)
btn9.place(x=190, y=70)
btn4.place(x=10, y=120)
btn5.place(x=100, y=120)
btn6.place(x=190, y=120)
btn1.place(x=10, y=170)
btn2.place(x=100, y=170)
btn3.place(x=190, y=170)
btn0.place(x=10, y=220)
btnSum.place(x=280, y= 70)
btnResta.place(x=280, y= 120)
btnMulti.place(x=280, y= 220)
btnDiv.place(x=280, y= 170) 
btnOper.place(x= 100, y=220)
btnBorrar.place(x= 190, y = 220)

root.mainloop()