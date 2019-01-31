"""2. Escribir las funciones necesarias para que, dadas dos cadenas de
caracteres:
- Indique si la segunda cadena es una subcadena de la primera. Por
ejemplo, ’cadena’ es una subcadena de ’subcadena’.
- Devuelva la que sea anterior en orden alfabético. Por ejemplo, si recibe
’kde’ y ’gnome’ debe devolver ’gnome’. """

def func1():
    cadena1 = input("Primera cadena: ")
    cadena2 = input("Segunda cadena: ")

    if cadena1.find(cadena2) > -1:
        print("Es subcadena")
    else:
        print("No es subcadena")


def func2():
    cadena1 = input("Primera cadena: ")
    cadena2 = input("Segunda cadena: ")

    if cadena1 < cadena2:
        print(cadena1)
    else:
        print(cadena2)

func2()