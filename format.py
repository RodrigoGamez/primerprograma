#Haciendo un format con el metodo replace


texto_usuario = input("Introduce un texto: ")
valor_cambiar = "E"


for letra in texto_usuario:
    if letra == "A":
        texto_usuario = texto_usuario.replace("A", valor_cambiar, 1)
    elif letra == "a":
        texto_usuario = texto_usuario.replace("a", valor_cambiar, 1)

print(texto_usuario)