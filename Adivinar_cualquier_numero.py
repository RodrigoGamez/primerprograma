#Adivinar un numero definido por un jugador, para que otro lo adivine


#Recogemos el valor del primer jugador
numero_adivinar = int(input("Introduce un numero para que tu amigo lo adivine: "))


#Le pedimos al segundo jugador que nos diga un numero
intentos = 5
while intentos > 0:
    numero_dicho = int(input("({} Intentos)-Introduce el numero que crees que es: ".format(intentos)))
    intentos -= 1
    if numero_dicho == numero_adivinar:
        print("Has ganado al {} intento".format(intentos + 1))
        intentos = 0


if numero_dicho != numero_adivinar:
    print("Has perdido, el numero era: {}".format(numero_adivinar))

