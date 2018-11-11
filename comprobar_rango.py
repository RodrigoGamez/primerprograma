

def range_mum(number, min, max):
    if number > min:
        if number < max:
            return True
        else:
            return False
    else:
        return False


print(range_mum(30, 15, 20))