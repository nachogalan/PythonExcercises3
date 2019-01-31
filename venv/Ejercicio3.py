"""3. Politiqueo.
- Escribir una función que reciba una tupla con nombres, y para cada
nombre imprima el mensaje Estimado <nombre>, vote por mí.
- Escribir una función que reciba una tupla con nombres, una posición de
origen p y una cantidad n, e imprima el mensaje anterior para los n
nombres que se encuentran a partir de la posición p.
- Modificar las funciones anteriores para que tengan en cuenta el género
del destinatario, para ello, deberán recibir una tupla de tuplas,
conteniendo el nombre y el género. """

def func1():
    tuplaNombres = ("Jorge", "Pablo", "Tonto", "Espacial")
    for i in range(0,len(tuplaNombres)):
        print("Estimado " + tuplaNombres[i] + ", vote por mí")

def func2():
    tuplaNombres = ("Jorge", "Pablo", "Tonto", "Espacial")

    nombre = input("Nombre: ")
    repes = input("Repeticiones: ")

    if(nombre in tuplaNombres):
       print((nombre + "\n") * int(repes))
    else:
        print("El nombre no se ha encontrado en la tupla...")

def func3():
    tuplaNombres = (("Jorge","Hombre"), ("Maria","Mujer"), ("Pablo","Hombre"), ("Laura","Mujer"))
    nombre = input("Nombre: ")

    if (nombre in tuplaNombres):
        print(si)
    else:
        print("No")
func3()