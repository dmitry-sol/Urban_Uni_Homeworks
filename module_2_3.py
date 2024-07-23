# module_2_3

my_list = [42, 69, 0, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
my_list_length = len(my_list)
i = 0

while i < my_list_length:
    if my_list[i] > 0:
        print(my_list[i])
    elif my_list[i] < 0:
        break
    i += 1
