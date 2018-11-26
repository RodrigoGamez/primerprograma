import pickle

from time import sleep

ACTION_ADD_CONTACT = 1
ACTION_REMOVE_CONTACT = 2
ACTION_FIND_CONTACT = 3
ACTION_EXPORT_CONTACT = 4
ACTION_LEAVE = 5

SAVE_FILE_NAME = "contacts.save"

MENU_OPTIONS = [ACTION_ADD_CONTACT, ACTION_REMOVE_CONTACT, ACTION_FIND_CONTACT, ACTION_EXPORT_CONTACT, ACTION_LEAVE]



def ask (options):
    selected_action = ""

    while not selected_action.isdigit() or (selected_action.isdigit() and int(selected_action) not in options):
        selected_action = input("¿Que opcion deseas?")

    return int(selected_action)



def show_menu():
    print("Aciones disponibles: ")
    print("1 - Añadir contacto ")
    print("2 - Eliminar contacto ")
    print("3 - Buscar un contacto ")
    print("4 - Exportar contactos a un CSV ")
    print("5 - Salir ")
    return ask(MENU_OPTIONS)



def add_contact(contacts):
    print("\n\nAñadir contacto\n")
    contact = {
        "name": input("Nombre: "),
        "phone": input("Telefono: "),
        "email": input("Correo: "),
    }
    contacts.append(contact)
    print("Se ha añadido el contacto {} correctamente\n".format(contact["name"]))
    sleep(2)



def remove_contat(contacts):
    pass



def find_contact(contacts):
    print("\n\nBuscar contacto\n")
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
        contact_index = ask(contact_indexes)
    elif len(contact_indexes) == 0:
        print("No se ha encontrado ninguno.")
        return

    print("\nInformación sobre {}\n".format(found_contacts[contact_index]["name"]))
    print("Nombre: {name}, Telefono: {phone}, Email: {email}\n\n".format(**found_contacts[contact_index]))
    sleep(2)




def exprt_contact():
    pass


def load_contacts():
    try:
        contacts = pickle.load(open(SAVE_FILE_NAME, "rb"))
    except FileNotFoundError:
        return []


def save_contacts(contacts):
    with open(SAVE_FILE_NAME, "wb") as save_file:
        pickle.dump(contacts, save_file)
        print("Datos guardados correctamente")


def main():
    contacts = load_contacts()

    action = show_menu()

    while action != ACTION_LEAVE:

        if action == ACTION_ADD_CONTACT:
            add_contact(contacts)
        elif action == ACTION_REMOVE_CONTACT:
            remove_contat(contacts)
        elif action == ACTION_FIND_CONTACT:
            find_contact(contacts)
        elif action == ACTION_EXPORT_CONTACT:
            exprt_contact(contacts)


        action = show_menu()


    save_contacts(contacts)


if __name__ == "__main__":
    main()