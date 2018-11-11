#Este programa consiste en transformar de grados farenheit a grados celsius


#Recogemos el valor a transformar
temperatura_farenheit = float(input("Introduce la temperatura a transformar: "))


#Realizamos los calculos
temperatura_celsius = temperatura_farenheit * 9 / 5 - 32

#Mostramos el resultado
print("La temperatura en celsius es de: {}".format(temperatura_celsius))