### CURSO PYTHON BASICO ###
### Strings ###

my_string = "Mi String"
my_other_string = 'Mi otro String'

print(len(my_string))
print(len(my_other_string))
print(my_string + " " + my_other_string)

my_new_line_string = "Este es un String\n con salto de línea"
print(my_new_line_string)

my_tab_string = "\t Este es un String con tabulación"
print(my_tab_string)

my_scape_string = "\t Este es un String \n con salto de línea"
print(my_scape_string)

# Formateo

name, surname, age = "Brais", "Moure", 35
print("Mi nombre es {} {} y mi edad es {}".format(name, surname, age))
print("Mi nombre es %s %s y mi edad es %d" %(name, surname, age))
print("Mi nombre es " + name + " " + surname + " y mi edad es " + str(age))
print(f"Mi nombre es {name} {surname} y mi edad es {age}")

# Desempaqueado de caracteres

language = "python"
a, b, c, d, e, f = language
print(a)
print(e)

# División

language_slice = language[1:3]
print("language[1:3]"+language_slice)

language_slice = language[1:]
print('language[1:]'+language_slice)

language_slice = language[-2]
print("language[-2]"+language_slice)

language_slice = language[0:6:3]
print("language[0:6:3] "+language_slice)

# Reverse

reversed_language = language[::-1]
print("Reverse "+reversed_language)

# Funciones del lenguaje

print(language.capitalize())
print(language.upper())
print(language.count("t"))
print(language.isnumeric())
print("1".isnumeric())
print(language.lower())
print(language.lower().isupper())
print(language.startswith("Py"))
print("Py" == "py") # No es lo mismo