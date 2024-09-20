# module_9_7
# Декораторы

def is_prime(func):

    def wrapper(*args):
        result_ = func(*args)
        divider = 2
        while result_ % divider != 0:
            divider += 1
        print('Простое' if divider == result_ else 'Составное')
        return result_

    return wrapper


@is_prime
def sum_three_or_more(*args):
    return sum(args)


result = sum_three_or_more(2, 3, 6)
print(result)
