#Programa para alamacenar una lista

mi_lista = []
input_usuario = input("¿Que necesitas comprar (Escribe  para salir) ?: ")


#Preguntamos al usuario, que necesita comprar
while input_usuario != "FIN":
    mi_lista.append(input_usuario)
    input_usuario = input("¿Que necesitas comprar (Escribe FIN para salir) ?: ")


#Mostramos en la consola la lista de la compra, que previamente el uuario ha definido
for posicion in mi_lista:
    print("Tengo que comprar: {}".format(posicion))


print("Esta es la lista de la compra")