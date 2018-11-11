
def reverse_string (string_to_revrese):
    string_reversed = ""
    index = len(string_to_revrese) - 1
    while index >= 0:
        string_reversed += string_to_revrese[index]
        index -= 1
    return string_reversed

print("Esta es la palabra dada la vuelta: " + reverse_string(input("Intrduce una palabra: ")))