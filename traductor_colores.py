

colores = {"rojo": "red",
           "azul": "blue",
           "amarillo": "yellow",
           "verde": "green",
           "negro": "black",}

salir = False

while not salir:
    color = input("¿Que color quieres traducir? [S para salir]: ")

    if color == "S":
        salir = True

    if color != "S":
        print(colores[color])
