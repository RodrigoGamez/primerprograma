
lista_datos = [3, 4, "Hola", "Telefono", 3, "Raton"]
lista_enteros = []
lista_string = []


for dato in lista_datos:
    if type(dato) == int:
        lista_enteros.append(dato)
    elif type(dato) == str:
        lista_string.append(dato)

print("Enteros: {}".format(lista_enteros))
print("Strings: {}".format(lista_string))