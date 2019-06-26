import random
from tkinter import *
from tkinter import ttk

columna1 = [10, 11, 9, False]
columna2 = [0, 6, 1, 0, False]
columna3 = [0, 8, 0, 7, 0, False]
columna4 = [13, 0, 0, 0, False]
columna5 = [0, 0, 0, False]

numeros = [2, 3, 4, 5, 9, 10, 12, 14, 15, 16, 17, 18, 19]



def definir_filas():
    global fila1
    global fila2
    global fila3
    global fila4
    global fila5

    fila1 = [columna1[0], columna2[0], columna3[0], False]
    fila2 = [columna1[1], columna2[1], columna3[1], columna4[0], False]
    fila3 = [columna1[2], columna2[2], columna3[2], columna4[1], columna5[0], False]
    fila4 = [columna2[3], columna3[3], columna4[2], columna5[1], False]
    fila5 = [columna3[4], columna4[3], columna5[2], False]



def completar(lista):
    total = 0
    while total != 38:
        for index in range(0, len(lista)-1):
            if lista[index] in numeros or lista[index] == 0:
                lista[index] = random.choice(numeros)
            total += lista[index]
        print("{}           {}".format(lista, total))
        if total == 38:
            lista[-1] = True
            break
        total = 0



def comprobar(lista):
    total = 0
    for index in range(0, len(lista)-1):
        total += lista[index]
        if total == 38:
            lista[-1] = True



def comprobar_todo():
    total = 1
    lista = [columna1[-1], columna2[-1], columna3[-1], columna4[-1], columna5[-1], fila1[-1], fila2[-1], fila3[-1],
             fila4[-1], fila5[-1]]

    for index in range(0, len(lista)):
        total *= lista[index]
    return total




def mostrar():
    print("\n")

    print(columna1)
    print(columna2)
    print(columna3)
    print(columna4)
    print(columna5)

    print("\n")

    print(fila1)
    print(fila2)
    print(fila3)
    print(fila4)
    print(fila5)


"""
def ventana(columnas, filas):
    global ventana
    ventana = Tk()
    ventana.title("Panel de Abejas")

    def texto(casilla, texto):
        casilla = Label(ventana, text = texto)
        casilla.grid(column = 2, row = 0)

    for index in range(0, len(columnas)):
        for columna in range(0, len(columnas[index])-1):
            cas1 = 0; cas2 = 0; cas3 = 0; cas4 = 0; cas5 = 0; cas6 = 0; cas7 = 0; cas8 = 0; cas9 = 0; cas10 = 0
            cas11 = 0; cas12 = 0; cas13 = 0; cas14 = 0; cas15 = 0; cas16 = 0; cas17 = 0; cas18 = 0; cas19 = 0

            casillas = [cas1, cas2, cas3, cas4, cas5, cas6, cas7, cas8, cas9, cas10, cas11, cas12, cas13, cas14,
                        cas15, cas16, cas17, cas18, cas19]
            for casilla in range(0, len(casillas)):
                texto(casilla, columnas[columna])
                break



class Ventana:

    ventana = Tk()

    def __init__(self, casilla = 0):
        self.casilla = casilla

    def Label(self, columna = 0, fila = 0, texto = "Text not found"):
        marco = ttk.Frame(ventana, padding="30 12 3 12").grid()
        ttk.Label(marco, text = texto).grid(column = columna, row = fila)


    ventana.mainloop()
    
"""



def main():
    #global ventana
    #ventana = Ventana

    definir_filas()
    while comprobar_todo() == 0:
        columnas = [columna1, columna2, columna3, columna4, columna5]
        for index in range(0, len(columnas)):
            completar(columnas[index])

        definir_filas()

        filas = [fila1, fila2, fila3, fila4, fila5]
        for index in range(0, len(filas)):
            comprobar(filas[index])

        #ventana = Ventana(casilla = 1)
        #ventana.Label(columna = 0, fila = 0, texto = str(columna1[0]))

        mostrar()


if __name__ == "__main__":
    main()