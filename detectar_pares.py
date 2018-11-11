

def numbers_couple(list):
    couple_list = []
    for index in list:
        if index % 2 == 0:
            couple_list.append(index)
    return couple_list

list = [1, 2, 3, 4, 5, 6, 7, 8 ,9]

print(numbers_couple(list))
