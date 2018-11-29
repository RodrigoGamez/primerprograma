import pickle
from tkinter import *
from tkinter import ttk

from time import sleep

ACTION_ADD_CONTACT = 1
ACTION_REMOVE_CONTACT = 2
ACTION_FIND_CONTACT = 3
ACTION_EXPORT_CONTACT = 4
ACTION_EXIT = 5

SAVE_FILE_NAME = "contacts.save"

MENU_OPTIONS = [ACTION_ADD_CONTACT, ACTION_REMOVE_CONTACT, ACTION_FIND_CONTACT, ACTION_EXPORT_CONTACT, ACTION_EXIT]



def ask_until_option_expected(options):
    selected_action = ""

    while not selected_action.isdigit() or (selected_action.isdigit() and int(selected_action) not in options):
        selected_action = input("¿Qué opción deseas? ")

    return int(selected_action)


def show_menu():
    print("Acciones disponinbles: ")
    print("1 - Añadir contacto")
    print("2 - Eliminar contacto")
    print("3 - Buscar un contacto")
    print("4 - Exportar contactos a un CSV")
    print("5 - Salir")
    return ask_until_option_expected(MENU_OPTIONS)


def add_contact(contacts, name, phone, email):

    contact = {
        "name": name,
        "phone": phone,
        "email": email
    }

    contacts.append(contact)
    print(contacts)
    return contact



def ask_new_contact(contacts):
    print("\n\nAñadir contacto\n")
    add_contact(contacts, input("Nombre: "), input("Teléfono: "), input("Teléfono: "))

    print("Se ha añadido el contacto {} correctamente\n".format(contact["name"]))
    sleep(2)


def remove_contact(contact, contact_index):
    del contact["name"]
    print("\n\n\n\n")
    print(contact_index)


def find_contact(contacts, search_text, print_info):
    print("\n\n" + search_text + "\n")
    search_term = input("Introducir el nombre del contacto o parte de él: ")
    found_contacts = []

    print("He encontrado los siguientes contactos:")
    contact_indexes = []
    contact_counter = 0

    for contact in contacts:
        if contact["name"].find(search_term) >= 0:
            found_contacts.append(contact)
            print("{} - {}".format(contact_counter, contact["name"]))
            contact_indexes.append(contact_counter)
            contact_counter += 1

    contact_index = 0

    if len(contact_indexes) > 1:
        contact_index = ask_until_option_expected(contact_indexes)
    elif len(contact_indexes) == 0:
        print("No se ha encontrado ninguno.")
        return

    if print_info == 1:
        print_information(found_contacts, contact_index)
    elif print_info == 0:
        remove_contact(found_contacts, contact_index)


def export_contacts():
    pass



def load_contacts():
    try:
        return pickle.load(open(SAVE_FILE_NAME, "rb"))
    except FileNotFoundError:
        return []


def save_contacts(contacts):
    with open(SAVE_FILE_NAME, "wb") as save_file:
        pickle.dump(contacts, save_file)
    print("Datos guardados correctamente.")


def print_information(list, list_index):
    print("\nInformación sobre {}\n".format(list[list_index]["name"]))
    print("Nombre: {name}, Telefono: {phone}, Email: {email}\n\n".format(**list[list_index]))
    sleep(2)


def main():

    contacts = []

    root = Tk()
    frame_add_contact = ttk.Frame(root, padding="30 12 3 12")
    frame_add_contact.grid()

    frame_contact_list = ttk.Frame(root, padding="30 12 30 12")
    frame_contact_list.grid()



    name = StringVar()
    email = StringVar()
    phone = StringVar()


    ttk.Label(frame_add_contact, text = "Nombre").grid(column = 1, row = 1)
    ttk.Label(frame_add_contact, text = "Email").grid(column = 2, row = 1)
    ttk.Label(frame_add_contact, text = "Telefono").grid(column = 3, row = 1)


    ttk.Entry(frame_add_contact, width=7, textvariable=name).grid(column=1, row=2)
    ttk.Entry(frame_add_contact, width=7, textvariable=email).grid(column=2, row=2)
    ttk.Entry(frame_add_contact, width=7, textvariable=phone).grid(column=3, row=2)

    ttk.Button(frame_add_contact,
               text="Añadir",
               comand=lambda: add_contact(contacts, name.get(), phone.get(), email.get())).grid(column=3, row=3)

    root.mainloop()



if __name__ == "__main__":
    main()