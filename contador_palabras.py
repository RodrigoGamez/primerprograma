

palabras = dict()

palabra = ""
numero_aparicion = 0

texto = input("Introduce un texto: ")

for caracter in texto:
    if caracter != " ":
        palabra += caracter
    else:
        palabras = {palabra : numero_aparicion + 1}
        palabra = ""

print(palabras)
