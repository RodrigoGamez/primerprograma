import random

columna1 = [0, 11, 0, False]
columna2 = [0, 6, 1, 0, False]
columna3 = [0, 8, 0, 7, 0, False]
columna4 = [13, 0, 0, 0, False]
columna5 = [0, 0, 0, False]

fila1 = [columna1[0], columna2[0], columna3[0], False]
fila2 = [columna1[1], columna2[1], columna3[1], columna4[0], False]
fila3 = [columna1[2], columna2[2], columna3[2], columna4[1], columna5[0], False]
fila4 = [columna2[3], columna3[3], columna4[2], columna5[1], False]
fila5 = [columna3[4], columna4[3], columna5[2], False]


numeros = [0, 2, 3, 4, 5, 9, 10, 12, 14, 15, 16, 17, 18, 19]


def completar(lista):
    total = 0
    while total != 38:
        for index in range(0, len(lista)-1):
            if lista[index] in numeros:
                lista[index] = random.choice(numeros)
            total += lista[index]
        print("{}           {}".format(lista, total))
        if total == 38:
            lista[-1] = True
            break
        total = 0


def mostrar():
    print("\n")

    print(columna1)
    print(columna2)
    print(columna3)
    print(columna4)
    print(columna5)

    print("\n")

    print(fila1)
    print(fila2)
    print(fila3)
    print(fila4)
    print(fila5)


def main():
    completar(columna1)
    completar(columna2)
    completar(columna3)
    completar(columna4)
    completar(columna5)


    mostrar()


if __name__ == "__main__":
    main()