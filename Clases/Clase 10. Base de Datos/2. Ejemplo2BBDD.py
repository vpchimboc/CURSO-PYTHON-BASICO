import sqlite3
#1.Crear la conexion
miConexion=sqlite3.connect("PrimeraBase")
#2. Crear el cursor
cursor=miConexion.cursor()
#3. Ejecutar Query
#cursor.execute("CREATE TABLE PRODUCTOS(NOMBRE_ARTICULO VARCHAR(50),PRECIO INTEGER,SECCION VARCHAR(20))")
#4. Insertar Datos
#cursor.execute("INSERT INTO PRODUCTOS VALUES ('PC',5,'TECNOLOGIA')")
#Insertar un lote de registros
"""variosProductos=[
("Camiseta",10,"Deportes"),
("Pc",30,"Tecnologia"),
("Camión",10,"Juguetería"),
("Mouse",10,"Tecnologia")
]
cursor.executemany("INSERT INTO PRODUCTOS VALUES(?,?,?)",variosProductos)
miConexion.commit()
"""
cursor.execute("SELECT * FROM PRODUCTOS")
variosProductos=cursor.fetchall()
print(variosProductos)
for producto in variosProductos:
    print("Nombre: ",producto[0],"Sección: ",producto[2])
miConexion.close()