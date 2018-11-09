#Programa capaz de contar las vocales, consonantes, espacios, puntos, etc de una frase


frase_usuario = input("Introduce, una frase: ")

vocales = ["a", "e", "i", "o", "u"]
consonantes = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]

n_vocales = 0
n_consonantes = 0
n_espacios = 0
n_puntos = 0
n_comas = 0
n_exclamaciones = 0
n_interrogaciones = 0

for letra in frase_usuario:
    if letra in vocales:
        n_vocales += 1
    elif letra in consonantes:
        n_consonantes += 1
    elif letra == " ":
        n_espacios += 1
    elif letra == ",":
        n_comas += 1
    elif letra == "!" or "¡":
        n_exclamaciones += 1
    elif letra == ".":
        n_puntos += 1
    elif letra == "¿" or "?":
        n_interrogaciones += 1


print("Hay {} vocales".format(n_vocales))
print("Hay {} consonantes".format(n_consonantes))
print("Hay {} espacios".format(n_espacios))
print("Hay {} puntos".format(n_puntos))
print("Hay {} comas".format(n_comas))
print("Hay {} excalamaciones".format(n_exclamaciones))
print("Hay {} interrogaciones".format(n_interrogaciones))
