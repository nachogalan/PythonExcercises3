def agenda(cad_buscar, lista_contactos):
    for contacto in lista_contactos:
        if not contacto[0].find(cad_buscar) == -1 or not contacto[1].find(cad_buscar) == -1 or not contacto[2].find(cad_buscar) == -1:
            print(contacto)

agenda("ce",[("laura","guijarro","1234567"),("celia","montalvez","25634567"),("aaron","griego","634264563")])