

palabras = dict()

palabra = ""
numero_aparicion = 1

texto = input("Introduce un texto: ")

for caracter in texto:
    if caracter != " ":
        palabra += caracter
    else:
        palabras[palabra]
        palabra = ""

print(palabras)
