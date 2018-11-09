#Programa capaz de contar las vocales, consonantes, espacios, puntos, etc de una frase


frase_usuario = input("Introduce, una frase: ")

vocales_minus = ["a", "e", "i", "o", "u"]
vocales_mayus = ["A", "E", "I", "O", "U"]
consonantes_minus = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]
consonantes_mayus = ["B", "C", "D", "F", "G", "H", "J", "K", "L", "M", "N", "P", "Q", "R", "S", "T", "V", "W", "X", "Y", "Z"]

n_vocales_minus = 0
n_vocales_mayus = 0
n_consonantes_minus = 0
n_consonantes_mayus = 0
n_espacios = 0
n_puntos = 0
n_comas = 0
n_exclamaciones = 0
n_interrogaciones = 0
n_mayusculas = 0

vocales = []



for letra in frase_usuario:
    if letra in vocales_minus:
        n_vocales_minus += 1
        vocales.append(letra)
    elif letra in vocales_mayus:
        n_vocales_mayus += 1
    elif letra in consonantes_minus:
        n_consonantes_minus += 1
    elif letra in consonantes_mayus:
        n_consonantes_mayus += 1
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


print("Hay {} vocales minusculas".format(n_vocales_minus))
print("Hay {} vocales mayusculas".format(n_vocales_mayus))
print("Hay {} consonantes minusculas".format(n_consonantes_minus))
print("Hay {} consonantes mayusculas".format(n_consonantes_mayus))
print("Hay {} espacios".format(n_espacios))
print("Hay {} puntos".format(n_puntos))
print("Hay {} comas".format(n_comas))
print("Hay {} excalamaciones".format(n_exclamaciones))
print("Hay {} interrogaciones".format(n_interrogaciones))

print("Estas son todas las vocales {}".format(vocales))
