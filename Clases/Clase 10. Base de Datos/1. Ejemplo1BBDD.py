import sqlite3
#1.Crear la conexion
miConexion=sqlite3.connect("PrimeraBase")
#2. Crear el cursor
cursor=miConexion.cursor()
#3. Ejecutar Query
#cursor.execute("CREATE TABLE PRODUCTOS(NOMBRE_ARTICULO VARCHAR(50),PRECIO INTEGER,SECCION VARCHAR(20))")
#4. Insertar Datos
cursor.execute("INSERT INTO PRODUCTOS VALUES ('PC',5,'TECNOLOGIA')")

miConexion.commit()
miConexion.close()