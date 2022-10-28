import sqlite3

miConexion=sqlite3.connect("GestionProductos3")

miCursor=miConexion.cursor()
#LECTURA DE INFORMACIÓN
miCursor.execute("SELECT * FROM PRODUCTOS WHERE ID=1")
variosProductos=miCursor.fetchall()
print(variosProductos)
for producto in variosProductos:
    print("Nombre: ",producto[0],"Sección: ",producto[2])

#ACTUALIZACION DE INFORMACIÓN
miCursor.execute("UPDATE PRODUCTOS SET PRECIO =5 WHERE ID=2")
#DELETE DE INFORMACIÓN
miCursor.execute("DELETE FROM PRODUCTOS WHERE ID=3")

miConexion.commit()
miConexion.close()