

lista_datos = [2, 4, 4.5, "Hola", False, [], 9]
lista_tipos = []


for dato in lista_datos:
    lista_tipos.append(type(dato))

print(lista_tipos)