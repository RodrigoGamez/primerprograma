#Programa capaz de contar las vocales, consonantes, espacios, puntos, etc de una frase


frase_usuario = input("Introduce, una frase: ")

vocales = [a, e, i, o, u]
consonantes = [b, c, d, f, g, h, j, k, l, m, n, p, q, r, s, t, v, w, x, y, z]

n_vocales = 0
n_consonantes = 0

for letra in frase_usuario:
    if letra in vocales:
        n_vocales += 1
    elif letra in consonantes:
        n_consonantes += 1


print("Hay {} vocales".format(n_vocales))
print("Hay {} consonantes".format(n_consonantes))