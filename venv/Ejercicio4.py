
def listaNombres():
    lista_personas = [("Jose", "L", "Alcantara"), ("Ramona", "O", "Perez"), ("Ramiro","C", "Ecuestre")]
    for persona in lista_personas:
        personas = (persona[0] + " " + persona[1] + ". " + persona[2])
        print(personas)

listaNombres()