import sqlite3

miConexion=sqlite3.connect("GestionProductos3")

miCursor=miConexion.cursor()

miCursor.execute('''
    CREATE TABLE PRODUCTOS(
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        NOMBRE_ARTICULO VARCHAR(50),
        PRECIO INTEGER,
        SECCION VARCHAR(20)
    )
''')


productos=[
("Camiseta",10,"Deportes"),
("Pc",30,"Tecnologia"),
("Camión",10,"Juguetería"),
("Mouse",10,"Tecnologia")
]
miCursor.executemany("INSERT INTO PRODUCTOS VALUES(NULL,?,?,?)",productos)

miConexion.commit()
miConexion.close()