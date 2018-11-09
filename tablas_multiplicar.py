#Este programa calcula la tabla de multiplicar de un numero


numero = int(input("Introduce el numero de la tabla: "))


for multiplo in range(1, 11):
    print("{} x {} = {}".format(numero, multiplo, numero * multiplo))