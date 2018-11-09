
numeros_usuario = []
numeros_del_usuario = ""

while len(numeros_usuario) < 10:
    while not numeros_del_usuario.isdigit():
        numeros_del_usuario = input("Dime un numero: ")
    numeros_usuario.append(int(numeros_del_usuario))
    numeros_del_usuario = ""

    print("Se ha añadido un numero")

numero_grande = numeros_usuario[0]

for numero in numeros_usuario:
    if numero < numero_grande:
        numero_grande = numero