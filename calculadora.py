#Calculadora mediante el terminal

numero1 = 0
numero2 = 0


#Preguntamos los valores

operacion = input("¿Qué operación quiere realizar (Suma / Resta / Division / Multiplicacion)?: ").upper()

numero1 = int(input("Introduzca el valor 1: "))
numero2 = int(input("Introduzca el valor 2: "))


#Realizamos las operaciones
if operacion == "SUMA":
    resultado = numero1 + numero2
elif operacion == "RESTA":
    resultado = numero1 - numero2
elif operacion == "DIVISION":
    resultado = numero1 / numero2
elif operacion == "MULTIPLICACION":
    resultado = numero1 * numero2


#Mostramos en pantalla el resultado
print("Resultado : {}".format(resultado))