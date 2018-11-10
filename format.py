#Haciendo un format con el metodo replace


texto_cambiar = "aurora boreal"
valor = 1


for dato in texto_cambiar:
    if dato == "a":
        texto_cambiar = texto_cambiar.replace("a", str(valor), 1)
        valor += 1
    elif dato == "e":
        texto_cambiar = texto_cambiar.replace("e", str(valor), 1)
        valor += 1
    elif dato == "i":
        texto_cambiar = texto_cambiar.replace("i", str(valor), 1)
        valor += 1
    elif dato == "o":
        texto_cambiar = texto_cambiar.replace("o", str(valor), 1)
        valor += 1
    elif dato == "u":
        texto_cambiar = texto_cambiar.replace("u", str(valor), 1)
        valor += 1


print(texto_cambiar)
