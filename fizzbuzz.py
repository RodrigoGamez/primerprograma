
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 90, 10, 11, 12, 14, 15, 30, 60, 70]
numero_grande = numeros[0]

for indice in range(len(numeros)):
    if numero_grande < numeros[indice]:
        numero_grande = numeros[indice]


print(numero_grande)