
numeros_usuario = []
numeros_del_usuario = ""
lugar = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
media = 0

while len(numeros_usuario) < 10:
    while not numeros_del_usuario.isdigit():
        numeros_del_usuario = input("Dime un numero: ")
    numeros_usuario.append(int(numeros_del_usuario))
    numeros_del_usuario = ""

    print("Se ha añadido un numero")

for posicion in lugar:
    media = media + numeros_usuario[posicion] / 10


print("La media es: {}".format(media))