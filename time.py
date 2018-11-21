

from time import sleep
from random import choice

FRASES_ALEGRES = ["jaja saludos", "el cielo es verde", "he aprobado"]
NOMBRES_MUEBLES = ["silla", "mesa", "cajon", "armario"]
NOMBRES_BEBIDAS = ["cocacola", "fanta", "fanta limon", "que rica el aguita"]
FRASES_ODIO = ["me cago en tus muertos pisoteados a caballos cojos", "pos a mi no me hace ni puta gracia so puto maricon de mierda que como te vea por la calle te parto la cabeza a patadas voladoras chinas y luego me follo los riñones hijo de puta"]



for second in range(1,5):
    if second == 1:
        print(choice(FRASES_ALEGRES))

    elif second == 2:
        print(choice(NOMBRES_MUEBLES))

    elif second == 3:
        print(choice(NOMBRES_BEBIDAS))

    elif second == 4:
        print(choice(FRASES_ODIO))