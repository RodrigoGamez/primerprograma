
def ask (ask):
    confirmacion = False
    while not confirmacion:
        dato = input(ask)
        seguro = input("Has dicho {}, ¿Estas seguro? [SI / NO]".format(dato)).upper()
        if seguro == "SI":
            confirmacion = True
    return dato


print(ask("¿Como te llamas?: "))

print(ask("Dime un numero"))