import sqlite3

miConexion=sqlite3.connect("GestionProductos")

miCursor=miConexion.cursor()
"""
miCursor.execute('''
    CREATE TABLE PRODUCTOS(
        CODIGO_ARTICULO VARCHAR(4) PRIMARY KEY,
        NOMBRE_ARTICULO VARCHAR(50),
        PRECIO INTEGER,
        SECCION VARCHAR(20)
    )
''')
"""
"""
productos=[
("A001","Camiseta",10,"Deportes"),
("A002","Pc",30,"Tecnologia"),
("A003","Camión",10,"Juguetería"),
("A004","Mouse",10,"Tecnologia")
]
miCursor.executemany("INSERT INTO PRODUCTOS VALUES(?,?,?,?)",productos)

"""
miCursor.execute("INSERT INTO PRODUCTOS VALUES('AR05','Tren',5,'Jugueteria')")
miConexion.commit()
miConexion.close()