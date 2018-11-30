from tkinter import *
from tkinter import ttk


def plus(first_number, second_number):
    return first_number + second_number


def main():
    root = Tk()
    root.title("Calculadora")

    frame_keypad = ttk.Frame(root, padding = "30 12 30 12")
    frame_keypad.grid()


    for column in range(1, 4):
        for row in range(2, 6):
            for text in range(1, 10):
                ttk.Button(frame_keypad, text=text).grid(column=column, row=row)

    root.mainloop()


if __name__ == "__main__":
    main()