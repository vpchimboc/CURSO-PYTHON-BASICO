from tkinter import *
from tkinter import messagebox
#Ventana Emergente
root=Tk()
def infoAdicional():
    messagebox.showinfo("Sistema","Sistema desarrollado por Verónica")

def estadoLicencia():
    messagebox.showwarning("Licencia","Producto bajo licencia GNU")

def estadoSalir():
    """valor=messagebox.askquestion("Salir","Deseas salir de la Aplicación")
    if valor=="yes":
        root.destroy
    """
    valor=messagebox.askokcancel("Salir","Deseas salir de la Aplicación")
    if valor==True:
        root.destroy()
def cerrarDocumento():
    valor=messagebox.askretrycancel("Reintentar","No es posible cerrar documento bloqueado")
    if valor==False:
        root.destroy()

barraMenu=Menu(root)
root.config(menu=barraMenu,width=300,height=300)

archivoMenu=Menu(barraMenu,tearoff=0)
archivoEdicion=Menu(barraMenu,tearoff=0)
archivoHerramientas=Menu(barraMenu,tearoff=0)
archivoAyuda=Menu(barraMenu,tearoff=0)

#menus a la barra
barraMenu.add_cascade(label="Archivo",menu=archivoMenu)
barraMenu.add_cascade(label="Eición",menu=archivoEdicion)
barraMenu.add_cascade(label="Herramientas",menu=archivoHerramientas)
barraMenu.add_cascade(label="Ayuda",menu=archivoAyuda)

#Submenus de menu archivo
archivoMenu.add_command(label="Nuevo")
archivoMenu.add_command(label="Guardar")
archivoMenu.add_command(label="Guardar Como")
archivoMenu.add_separator()
archivoMenu.add_command(label="Cerrar",command=cerrarDocumento)
archivoMenu.add_command(label="Salir",command=estadoSalir)

#Submenus de menu edicion
archivoEdicion.add_command(label="Copiar")
archivoEdicion.add_command(label="Cortar")
archivoEdicion.add_command(label="Pegar")

#Submenus de menu ayuda
archivoAyuda.add_command(label="Licencia",command=estadoLicencia)
archivoAyuda.add_command(label="Acerca de",command=infoAdicional)

root.mainloop()