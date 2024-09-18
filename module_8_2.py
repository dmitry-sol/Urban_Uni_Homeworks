# module_8_2
# Сложные моменты и исключения в стеке вызовов функции

def personal_sum(numbers):
    result = 0
    incorrect_data = 0
    i = 0
    try:
        while i < len(numbers):
            try:
                result = result + numbers[i]
                i += 1
            except TypeError:
                print(f'Некорректный тип данных для подсчёта суммы - {numbers[i]}')
                incorrect_data += 1
                i += 1
    except TypeError:
        print(f'В numbers записан некорректный тип данных')
        return None
    return result, incorrect_data

def calculate_average(numbers):
    try:
        sum_ = personal_sum(numbers)
        average = sum_[0] / (len(numbers) - sum_[1])
    except TypeError:
        return None
    except ZeroDivisionError:
        return 0
    return average


print(f'Результат 1: {calculate_average("1, 2, 3")}')  # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')  # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}')  # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')  # Всё должно работать