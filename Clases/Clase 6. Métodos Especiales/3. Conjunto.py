"""
Un conjunto es una lista de elementos donde ninguno 
de ellos está repetido. A partir de una lista, 
en la que pueden haber elementos repetidos, 
con set es posible crear otra lista con todos 
los elementos pero sin repetir ninguno. 
"""
print("Métodos de los conjuntos")
c = set()
#add(): Añade un ítem a un conjunto, si ya existe no lo añade
c.add(1)
c.add(2)
c.add(3)
c

#discard(): Borra un ítem de un conjunto
c.discard(1)
c

c.add(1)
c2 = c
c2.add(4)
c

#copy(): Crea una copia de un conjunto
#Recordar que los tipos compuestos no se pueden copiar, son como accesos directos por referencia

c2 = c.copy()
c2
c

c2.discard(4)
c2
c


#clear(): Borra todos los ítems de un conjunto
c2.clear()
c2

#Comparación de conjuntos
c1 = {1,2,3}
c2 = {3,4,5}
c3 = {-1,99}
c4 = {1,2,3,4,5}
"""isdisjoint(): Comprueba si el conjunto es disjunto de otro conjunto
Si no hay ningún elemento en común entre ellos
"""
c1.isdisjoint(c2)

#issubset(): Comprueba si el conjunto es subconjunto de otro conjunto
#Si sus ítems se encuentran todos dentro de otro

c3.issubset(c4)

#issuperset(): Comprueba si el conjunto es contenedor de otro subconjunto
#Si contiene todos los ítems de otro

c3.issuperset(c1)

#Métodos avanzados
"""Se utilizan para realizar uniones, diferencias y otras operaciones 
avanzadas entre conjuntos.
Suelen tener dos formas, la normal que devuelve el resultado,
 y otra que hace lo mismo pero actualiza el propio resultado.
"""
c1 = {1,2,3}
c2 = {3,4,5}
c3 = {-1,99}
c4 = {1,2,3,4,5}
#union(): Une un conjunto a otro y devuelve el resultado en un nuevo conjunto
c1.union(c2) == c4

c1.union(c2)

c1

c2

#update(): Une un conjunto a otro en el propio conjunto
c1.update(c2)
c1

#difference(): Encuentra los elementos no comunes entre dos conjuntos
c1 = {1,2,3}
c2 = {3,4,5}
c3 = {-1,99}
c4 = {1,2,3,4,5}
c1.difference(c2)

#difference_update(): Guarda en el conjunto los elementos no comunes entre dos conjuntos
c1.difference_update(c2)
c1

#intersection(): Devuelve un conjunto con los elementos comunes en dos conjuntos
c1 = {1,2,3}
c2 = {3,4,5}
c3 = {-1,99}
c4 = {1,2,3,4,5}
c1.intersection(c2)

#intersection_update(): Guarda en el conjunto los elementos comunes entre dos conjuntos
c1.intersection_update(c2)
c1

"""symmetric_difference(): Devuelve los elementos simétricamente diferentes 
entre dos conjuntos
Todos los elementos que no concuerdan entre los dos conjuntos
"""
c1 = {1,2,3}
c2 = {3,4,5}
c3 = {-1,99}
c4 = {1,2,3,4,5}
c1.symmetric_difference(c2)
