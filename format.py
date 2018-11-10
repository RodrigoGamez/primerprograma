#Haciendo un format con el metodo replace


valores_sustituir = [1, 2, "hola", "adios"]
string_cambiar = "Hola, numero {}, numero {}, {} y {}"
cuenta_atras = [4, 3, 2, 1]


for valor in valores_sustituir:
    string_cambiar = string_cambiar.replace("{}", str(valor), 1)

print(string_cambiar)