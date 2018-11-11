

salida = False
agenda = dict()

while not salida:
    accion = input("¿Que quieres hacer: ? [Añadir numero(A) / Consultar numero(C) / Salir(S]")

    #Añadir
    if accion == "A":
        print("Vamos a añadir un numero de telefono:")
        print("-------------------------------------")
        agenda[input("Nombre: ")] = input("numero: ")


    #Consultar
    elif accion == "C":
        print("Vamos a consultar un numero de telefono:")
        print("----------------------------------------")
        nombre = input("¿Que nombre quieres buscar: ?")
        print(agenda[nombre])

    #Salir
    elif accion == "S":
        salida = True