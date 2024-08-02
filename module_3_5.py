# module_3_5

def get_multiplied_digits(number):
    str_number = str(number)
    if len(str_number) > 1:
        first = int(str_number[:1])
        second = int(str_number[1:])
        multiplication = first * get_multiplied_digits(second)
    else:
        return number
    return multiplication


result = get_multiplied_digits(40203)
print(result)
