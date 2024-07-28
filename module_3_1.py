# module_3_1

str1 = 'Capybara'
str2 = 'Armageddon'
str3 = 'Urban'
str4 = 'cycle'
list3 = ['ban', 'BaNaN', 'urBAN']
list4 = ['recycling', 'cyclic']

calls = 0


def list_in_low(list_):
    list_in_low_ = []
    for i in list_:
        list_in_low_.append(i.lower())
    return list_in_low_


def count_calls():
    global calls
    calls += 1


def string_info(string):
    count_calls()
    length = len(string)
    string_upper = string.upper()
    string_lower = string.lower()
    return length, string_upper, string_lower


def is_contains(string, list_):
    count_calls()
    list_new = list_in_low(list_)
    string_ = string.lower()
    if string_ in list_new:
        flag = True
    else:
        flag = False
    return flag


print(string_info(str1))
print(string_info(str2))
print(is_contains(str3, list3))
print(is_contains(str4, list4))
print(calls)
