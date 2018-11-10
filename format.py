#Haciendo un format con el metodo replace


texto_usuario = input("Introduce un texto: ")
valor_cambiar = "i"


for valor in texto_usuario:
    texto_usuario = texto_usuario.replace("a", valor_cambiar, 1)
    texto_usuario = texto_usuario.replace("e", valor_cambiar, 1)
    texto_usuario = texto_usuario.replace("o", valor_cambiar, 1)
    texto_usuario = texto_usuario.replace("u", valor_cambiar, 1)


print(texto_usuario)
