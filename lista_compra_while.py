#Programa para definir una lista de cosas

mi_lista = []
input_usuario = ""


#Preguntamos al usuario, que necesita comprar
while input_usuario != "FIN":
    input_usuario = input("¿Que necesitas comprar (Escribe FIN para salir) ?: ")
    mi_lista.append(input_usuario)


#Definimos algunas variables, para el siguiente while
largo_lista = len(mi_lista)
indice_actual = 0


#Mostramos en la consola la lista de la compra, que previamente el uuario ha definido
while indice_actual < largo_lista:
    print("Tengo que comprar: {}".format(mi_lista[indice_actual]))
    indice_actual += 1


print("Esta es la lista de la compra")