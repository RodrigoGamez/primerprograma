

def max_of_three(first, second, third):
    max_num = 0
    if max_num < first:
        max_num = first
    if max_num < second:
        max_num = second
    if max_num < third:
        max_num = third
    return  max_num

print(max_of_three(2, 5, 4))