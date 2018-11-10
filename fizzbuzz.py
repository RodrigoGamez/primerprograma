
numeros = [1, 10, 70, 30, 50, 55]
multiplos_dos = []
multiplos_tres = []
multiplos_cinco = []
multiplos_siete = []


for indice in numeros:
    if indice % 2 == 0:
        multiplos_dos.append(indice)

    if indice % 3 == 0:
        multiplos_tres.append(indice)

    if indice % 5 == 0:
        multiplos_cinco.append(indice)

    if indice % 7 == 0:
        multiplos_siete.append(indice)


print("Multiplos de 2: {}".format(multiplos_dos))
print("Multiplos de 3: {}".format(multiplos_tres))
print("Multiplos de 5: {}".format(multiplos_cinco))
print("Multiplos de 7: {}".format(multiplos_siete))