

def numbers_couple(list):
    couple_list = []
    for index_data in list:
        if index_data % 2 == 0:
            couple_list.append(index_data)
    return couple_list

list = [1, 2, 3, 4, 5, 6, 7, 8 ,9]

print(numbers_couple(list))
