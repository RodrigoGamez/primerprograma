from tkinter import *
from tkinter import ttk


def add_number(frame_to_print, number_to_append = 0, position_number = 1, operation = None):
    frist_number = 0
    second_number = 0
    if position_number == 1:
        frist_number = frist_number * 10 + number_to_append
    else:
        second_number = second_number * 10 + number_to_append

    if operation != None:
        if operation == "+":
            result = frist_number + second_number
        elif operation == "-":
            result = frist_number - second_number
        elif operation == "x":
            result = frist_number * second_number
        elif operation == "/":
            result = frist_number / second_number

        ttk.Label(frame_to_print, text=result).grid(column=1, row=1)


def draw_buttons(frame):
    ttk.Button(frame, text="1", command = lambda: add_number(frame_to_print=frame, number_to_append=1)
               ).grid(column=1, row=2)
    ttk.Button(frame, text="2", command = lambda: add_number(frame_to_print=frame, number_to_append=1)
               ).grid(column=2, row=2)
    ttk.Button(frame, text="3", command = lambda: add_number(frame_to_print=frame, number_to_append=1)
               ).grid(column=3, row=2)
    ttk.Button(frame, text="4", command = lambda: add_number(frame_to_print=frame, number_to_append=1)
               ).grid(column=1, row=3)
    ttk.Button(frame, text="5", command = lambda: add_number(frame_to_print=frame, number_to_append=1)
               ).grid(column=2, row=3)
    ttk.Button(frame, text="6", command = lambda: add_number(frame_to_print=frame, number_to_append=1)
               ).grid(column=3, row=3)
    ttk.Button(frame, text="7", command = lambda: add_number(frame_to_print=frame, number_to_append=1)
               ).grid(column=1, row=4)
    ttk.Button(frame, text="8", command = lambda: add_number(frame_to_print=frame, number_to_append=1)
               ).grid(column=2, row=4)
    ttk.Button(frame, text="9", command = lambda: add_number(frame_to_print=frame, number_to_append=1)
               ).grid(column=3, row=4)
    ttk.Button(frame, text="0", command = lambda: add_number(frame_to_print=frame, number_to_append=1)
               ).grid(column=2, row=5)



    ttk.Button(frame, text="+", command = lambda: add_number(frame_to_print=frame, position_number=2, operation="+")
               ).grid(column=4, row=2)

    ttk.Button(frame, text="-", command = lambda: add_number(frame_to_print=frame, position_number=2, operation="-")
               ).grid(column=4, row=3)

    ttk.Button(frame, text="x", command = lambda: add_number(frame_to_print=frame, position_number=2, operation="x")
               ).grid(column=4, row=4)

    ttk.Button(frame, text="/", command = lambda: add_number(frame_to_print=frame, position_number=2, operation="/")
               ).grid(column=4, row=5)

    ttk.Button(frame, text="=").grid(column=3, row=5)


def main():
    root = Tk()
    root.title("Calculadora")

    frame_keypad = ttk.Frame(root, padding = "30 12 30 12")
    frame_keypad.grid()

    result = 0
    ttk.Label(frame_keypad, text = result).grid(column = 1, row = 1)

    draw_buttons(frame_keypad)



    for child in frame_keypad.winfo_children():
        child.grid_configure(padx = 5, pady = 5)

    root.mainloop()


if __name__ == "__main__":
    main()