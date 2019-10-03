# Tp7 – Capa Presentacion Socios

# Crear en Python usando Tkinter un formulario para gestionar los datos de Socios usando la Clase de la Capa de Negocio Socios .

# El Formulario principal tiene que mostrar todos los socios en Treeview y tener los siguientes botones Alta , Baja , Modificar .

# Apretar el Boton Alta se tiene que abrir un formulario con los campos para ingresar los datos de socio .
# Incluye  2 botones Guardar y Cancelar.

# Apretar el Boton Baja se tiene que dar de baja el socio seleccionado .

# Apretar el Boton Modificar se tiene que abrir un formulario con los campos con los datos del socio seleccionado .
# Incluye 2 botones Aceptar y Cancelar .

from tkinter import *
from tkinter import ttk, messagebox
from practico_06.capa_negocio import NegocioSocio
from practico_05.ejercicio_01 import Socio


class UISocio(Frame):
    def __init__(self, root=None):

        super().__init__(root)

        self.grid(row=0, column=0, ipady=5, ipadx=5)
        self.treeSocios = ttk.Treeview(self, columns=("nombre", "apellido", "dni"))
        self.treeSocios.grid(column=0, row=0)
        self.treeSocios.heading("#0", text="Id")
        self.treeSocios.heading("#1", text="Nombre")
        self.treeSocios.heading("#2", text="Apellido")
        self.treeSocios.heading("#3", text="DNI")

        frameControles = Frame(self)
        frameControles.grid(column=0, row=1, sticky='w')
        btnAlta = ttk.Button(frameControles, text='Alta', command=self.altaUI)
        btnEliminar = ttk.Button(frameControles, text='Baja', command=self.eliminarUI)
        btnModificar = ttk.Button(frameControles, text='Modificar', command=self.modificacionUI)

        btnAlta.grid(column=0)
        btnEliminar.grid(column=1, row=0)
        btnModificar.grid(column=2, row=0)

        # instancia reglas de negocio
        self.capa_negocio = NegocioSocio()

        self.llenarTreeSocios()

    def llenarTreeSocios(self):

        listSocio = self.capa_negocio.todos()
        for socio in listSocio:
            self.treeSocios.insert("", END, text=socio.id, values=(socio.nombre, socio.apellido, socio.dni))


    def vaciarTreeSocios(self):
        self.treeSocios.delete(*self.treeSocios.get_children())

    def limpiarTreeSocios(self):
        for i in self.treeSocios.get_children():
            self.treeSocios.delete(i)

    def actualizarTreeSocios(self):
        self.limpiarTreeSocios()
        self.llenarTreeSocios()

    def getSocio(root):
        socio = Socio()
        socio.nombre = root.txtNombre
        socio.apellido = root.txtApelido
        socio.dni = root.txtDni

    def altaUI(self):
        alta = Toplevel()
        HandlerSocio(root=alta, form=self, status="A")

    def eliminarUI(self):
        for socio in self.treeSocios.selection():
            self.capa_negocio.baja(self.treeSocios.item(socio)['text'])
        self.actualizarTreeSocios()

    def modificacionUI(self):
        for socio in self.treeSocios.selection():
            s = self.capa_negocio.buscar(self.treeSocios.item(socio)['text'])
            if s is not None:
                modificacion = Toplevel()
                HandlerSocio(root=modificacion, form= self , status="M", socio=s)
            else:
                messagebox.showerror('ERROR', ' Por favor seleccione un socio')

    def negocioagregar(self, socio):
        return self.capa_negocio.alta(socio)

    def negociomodificar(self, socio):
        return self.capa_negocio.modificacion(socio)

    def negociobuscar(self, dni):
        return self.capa_negocio.buscar_dni(dni)


class HandlerSocio:
    def __init__(self, root, form, status, socio=None):
        self.root = root
        self.form = form
        self.status = status
        self.frameDatos = Frame(root)
        self.frameDatos.grid(column=0, row=0)


        self.strDNI = StringVar()
        self.strNombre = StringVar()
        self.strApellido = StringVar()
        self.strError = StringVar(value='')

        lblDni = ttk.Label(self.frameDatos, text="DNI")
        lblNombre = ttk.Label(self.frameDatos, text='Nombre')
        lblApellido = ttk.Label(self.frameDatos, text='Apellido')
        lblErr = ttk.Label(self.frameDatos, textvariable=self.strError)

        # ubicamos los labels
        lblDni.grid(row=1, column=0)
        lblNombre.grid(row=2, column=0)
        lblApellido.grid(row=3, column=0)

        lblErr.grid(row=4, column=0, padx=8, pady=8, columnspan=2)

        # textbox
        self.txtDNI = ttk.Entry(self.frameDatos, textvariable=self.strDNI)
        self.txtNombre = ttk.Entry(self.frameDatos, textvariable=self.strNombre)
        self.txtApellido = ttk.Entry(self.frameDatos, textvariable=self.strApellido)

        # ubicacion text
        self.txtDNI.grid(column=1, row=1)
        self.txtNombre.grid(column=1, row=2)
        self.txtApellido.grid(column=1, row=3)

        if self.status == "M":
            self.socio = socio
            self.strDNI.set(socio.dni)
            self.strApellido.set(socio.apellido)
            self.strNombre.set(socio.nombre)



        #if self.status == "A":
        #self.strID.set('0')

        self.frameDatos = Frame(root)
        self.frameDatos.grid(column=0, row=1)
        if self.status == "A":
            btnGuardar = ttk.Button(self.frameDatos, text='Guardar', command=lambda: self.guardarSocio())
        else:
            btnGuardar = ttk.Button(self.frameDatos, text='Modificar' , command = lambda : self.guardarSocio(socio))
        btnCancel = ttk.Button(self.frameDatos, text='Cancelar', command=root.destroy)

        # Posicion botones

        btnGuardar.grid(row=0, column=0)
        btnCancel.grid(row=0, column=1)

    # Accion de los botones
    def guardarSocio(self, s=None):

        if self.status == 'A':
            socio = Socio()
            socio.dni = self.txtDNI.get()
            socio.nombre = self.txtNombre.get()
            socio.apellido = self.txtApellido.get()
            try:
                agrega = self.form.negocioagregar(socio)
                if agrega:
                    messagebox.showinfo('INFORMACION', 'Socio Agregado con exito')
                    self.root.destroy()
                    self.form.actualizarTreeSocios()
            except Exception as ex:
                messagebox.showerror('ERROR', 'No se pudo modificar el socio contacte al administrador del sistema')
                print(ex)
                self.root.destroy()
                self.form.actualizarTreeSocios()
        elif self.status == 'M':
            socio = self.form.negociobuscar(s.dni)
            socio.nombre = str(self.strNombre.get())
            socio.dni = str(self.strDNI.get())
            socio.apellido = str(self.strApellido.get())
            try:
                modifica = self.form.negociomodificar(socio)
                if modifica:
                    messagebox.showinfo('INFORMACION', 'Socio modificado con exito')
                    self.root.destroy()
                    self.form.actualizarTreeSocios()
            except Exception as ex:
                messagebox.showerror('ERROR', 'No se pudo modificar el socio contacte al administrador del sistema')
                print(ex)
                self.root.destroy()
                self.form.actualizarTreeSocios()


if __name__ == "__main__":
    ui = Tk()
    ui.title('ABM Socios')
    app = UISocio(root=ui)
    ui.mainloop()
    exit()
