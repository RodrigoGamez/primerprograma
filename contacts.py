#minuto 33:30 video agenda con pepinillos
from time import sleep

ACTION_ADD_CONTACT = 1
ACTION_REMOVE_CONTACT = 2
ACTION_FIND_CONTACT = 3
ACTION_EXPORT_CONTACT = 4
ACTION_LEAVE = 5

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
    search_term = input("Introducir el nombre del contacto o parte de el: ")
    found_contacts = []

    print("He encontrado los siguientes contactos: ")
    contact_index = []
    contact_counter = 0


    for contact in contacts:
        if contact["name"].find(search_term) >= 0:
            found_contacts.append(contact)
            print("{} - {}".format(contact_counter, contact["name"]))
            contact_index.append(contact_counter)
            contact_counter += 1

    contact_index = 0

    if len(contact_index) > 1:
        contact_index = ask(contact_index)
    elif len(contact_index) == 0:
        print("No se ha encontrado ninguno")
        return


    print("\nInformacion sobre {}\n".format(found_contacts[contact_index]))
    print("Nombre: {name}, Telefono: {phone}, Correo: {email}".format(**found_contacts[contact_index]))




def exprt_contact():
    pass



def main():
    contacts = []

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


if __name__ == "__main__":
    main()