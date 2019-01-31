
agenda = {'laura': '437675645365', 'celia': '654376547', 'yony': '3263466345'}
nombre = input("Nombre: ")

while nombre != "*":
    if nombre in agenda:
        print("Ya existe, el numero de telefono es " + agenda.get(nombre))
        if input("¿Quieres cambiarlo??") == "si":
            agenda.update({nombre: input("telefono modificado: ")})
        else :
            exit()
    else:
        if input("¿deseas agregar, " + nombre +"?") == "si":
            agenda.update({nombre: input("telefono: ")})

        else :
            exit()
