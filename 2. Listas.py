"""
En Python, podrá usar una función de lista que 
crea un grupo que será manipulado para su análisis. 
Esta colección de datos se denomina objeto de lista.
"""
print("#########FUNCIONES DE LAS LISTAS########")

"""
Es el recipiente común principal y, sin duda, el más importante.

Una lista se define como una colección de objetos ordenada, mutable y heterogénea.
- Para aclarar: el orden implica que la recolección de objetos sigue un orden particular.
- Mutable significa que la lista se puede mutar o cambiar, y heterogéneo implica que podrá
 mezclar y hacer coincidir cualquier tipo de objeto o tipo de datos dentro de una lista (int, float o string).
- Las listas están contenidas en una colección de corchetes [ ].
"""
"""
El método sort () es un método de Python integrado que, 
de forma predeterminada, ordena la lista en orden ascendente. 
Sin embargo, modificará el orden de ascendente a descendente 
especificando los criterios de clasificación.
"""
prices = [589.36, 237.81, 230.87, 463.98, 453.42] 
prices.sort() 
prices
personas = ["Veronica","Paulina","Chimbo", "Coronel"] 
sorted(personas)
sorted(personas, reverse=True)

"""función type ()
Para la función type (), devuelve el tipo de clase de un objeto.
"""
fam = ["abs", 1.57, "egfrma", 1.768, "mom", 1.71, "dad"]
type(fam)

"""
método append ()
El método append () agregará algunos elementos que ingrese al 
final de los elementos que especificó.
"""
months = ['January', 'February', 'March'] 
months.append('April') 
months

"""
método extend ()
El método extend () aumenta la longitud de la lista 
en el número de elementos que se proporcionan a la estrategia, 
por lo que si usted preferir agregar varios elementos a la lista, 
usted será capaz de utilice este método.
"""
list = [1, 2, 3] 
list.extend([4, 5, 6]) 
list

"""
método index ()
El método index () devuelve el primario Apariencia de el valor requerido.
"""
months = ['January', 'February', 'March', 'April', 'May'] 
months.index('March')

"""
función max ()
La función max () devolverá el valor más alto de los valores ingresados.
"""
prices = [589.36, 237.81, 230.87, 463.98, 453.42] 
price_max = max(prices) 
price_max
"""
función min ()
La función min () devolverá el punto mas bajo valor de los valores ingresados.
"""
months = ['January', 'February', 'March'] 
prices = [238.11, 237.81, 238.91]
# Identificar el precio minímo
min_price = min(prices) 
min_price
 # Identificar el indice del precio mínimo
min_index = prices.index(min_price) 
min_index
 # Identificar el mes con precio mínimo
min_month = months[1] 
min_month

"""
función len ()
La función len () devuelve el número de elementos en una lista especificada.
"""

list_1 = [50.29] 
list_2 = [76.14, 89.64, 167.28] 
len(list_1)
len(list_2)

"""
función clear ()
El método clear () elimina todos los elementos de una lista específica 
y los convierte en una lista vacía.
"""
months = ['January', 'February', 'March', 'April', 'May'] 
months.clear()
months

"""
función de inserción
El método insert () inserta lo requerido valor en la posición deseada.
"""
fruits = ['apple', 'banana', 'cherry']
fruits.insert(1, "pineapple")
fruits

"""
función count ()
El método count () devuelve el número de elementos con el deseado valor.
"""
fruits = ['cherry', 'apple', 'cherry', 'banana', 'cherry']
x = fruits.count("cherry")
x

"""
función pop ()
El método pop () elimina el elemento en la posición requerida.
"""
fruits = ['apple', 'banana', 'cherry', 'orange', 'pineapple']
fruits.pop(2)
fruits

"""
función remove ()
El método remove () elimina el primero ocurrencia del elemento con el especificado valor.
"""
fruits = ['apple', 'banana', 'cherry', 'banana','orange', 'pineapple']
fruits.remove("banana")
fruits

"""
función reverse ()
El método reverse () invierte el orden de los elementos.
"""
fruits = ['apple', 'banana', 'cherry', 'orange', 'pineapple']
fruits.reverse()
fruits

"""
función copiar ()
El método copy () devuelve una copia de la lista especificada y crea la nueva lista.
"""
fruits = ['apple', 'banana', 'cherry', 'orange']
x = fruits.copy()
x

#Lista con objetos
#Creamos la clase mascota
class Mascota:
    def __init__(self, nombre ,edad):
        self.nombre=nombre
        self.edad=edad
    #repr es usada para crear una cadena que representa el estado del objeto
    def __repr__(self):
        return f"\nMi mascota {self.nombre} y su edad {self.edad}"
#creamos una lista de mascotas
misMascotas=[
        Mascota("Nemo",2),
        Mascota("Michi",3),
        Mascota("Lomito",2),
        Mascota("Lombri",7)
        ]
#Mostrar antes de ordenar
print(repr(misMascotas))
#Hacemos el sort pasando una funcion lambda que obtenga el dato sobre el cual ordenar
misMascotas.sort(key=lambda x:x.nombre)
#Mostrar despues de ordenar
print(repr(misMascotas))
#Ordenamos por edad
misMascotas.sort(key=lambda x:x.edad)
#Mostrar despues de ordenar
print(repr(misMascotas))
#Mostrar el tamaño de la lista
print(len(misMascotas))
#Agregar un objeto a la lista
print(misMascotas.append(Mascota("Lucas",3)))
#Insertamos un objeto a la lista
print(misMascotas.insert(0,Mascota("Lucas",3)))
#Mostrar lista
print(repr(misMascotas))
#Mostrar el Maximo de la lista
print(max(misMascotas,key=lambda x:x.edad))
#Mostrar el Mínimo de la lista
print(min(misMascotas,key=lambda x:x.edad))
#Eliminar el segundo objeto de la lista
misMascotas.pop(2)
#Mostrar lista
print(repr(misMascotas))