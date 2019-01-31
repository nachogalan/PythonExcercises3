"""1. Escribir las funciones necesarias para que, dada una cadena y un
carácter:
- Inserte el carácter entre cada letra de la cadena. Ej: ’separar’ y ’,’
debería devolver : ’s,e,p,a,r,a,r’
- Reemplace todos los espacios por el carácter. Ej: ’mi archivo de
texto.txt’ y ’_’ debería devolver ’mi_archivo_de_texto.txt’
- Reemplace todos los dígitos en la cadena por el carácter. Ej: ’su clave
es: 1540’ y ’X’ debería devolver ’su clave es: XXXX’
- Inserte el caracter cada 3 dígitos en la cadena. Ej. ’2552552550’ y ’.’
debería devolver ’255.255.255.0’"""

def func1():
    cadena=input("Cadena:")
    caracter=input("Carácter:")
    print(caracter.join(cadena))

def func2():
    cadena = input("Escriba frase con espacios:")
    print(cadena.replace(" ","_"))

def func3():
    cadena = input("Escriba frase con algun numero:")
    caracter = input("Carácter:")
    """
    El range(10) indica que coja los numeros en el rango de [0-9]
    """
    for i in range(10):
        cadena = cadena.replace(str(i), caracter)
    print(cadena)

def func4():
    cadena = input("Cadena:")
    caracter = input("Caracter:")
    cadena2 = ""

    for i in range(0,len(cadena)):
        if(i != 0 and i%3==0):
            cadena2 = cadena2 + caracter
        cadena2 = cadena2 + cadena[i]

    print(cadena2)
func4()