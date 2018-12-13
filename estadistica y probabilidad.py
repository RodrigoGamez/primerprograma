
print("Calculadora estadistica por Rodrigo Gámez Triviño 1C")
print("----------------------------------------------------\n\n\n\n")

Xiin = input("Introduce los valores de la variable separados por comas (1,2,15,etc,): ")
fiin = input("Introduce los valores de la encuesta elaborada separados por comas (0,3,4,etc,): ")

Xi = []
fi = []
fr = []
fr_percentage = []
Fi = []
n = 0

Xi_value = ""
fi_value = ""

for value_ask in Xiin:
    if not value_ask == ",":
        Xi_value += value_ask
    else:
        Xi.append(Xi_value)
        Xi_value = ""


for value_ask in fiin:
    if not value_ask == ",":
        fi_value += value_ask
        n += int(fi_value)
    else:
        fi.append(fi_value)
        fi_value = ""



length = len(fi)

for index in range(0, length):
    fr.append(int(fi[index]) / n)
    fr_percentage.append(fr[index] * 100)
    Fi.append(int(Fi[index - 1]) + int(fi[index]))


print(Xi)
print(fi)
print(fr)
print(fr_percentage)
print(Fi)







