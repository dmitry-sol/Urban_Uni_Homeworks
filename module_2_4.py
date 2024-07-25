# module_2_4

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
if 1 in numbers:
    numbers.remove(1)
primes = []
not_primes = []
is_prime = False

for i in numbers:
    for j in numbers:
        if i != j and i % j == 0:
            not_primes.append(i)
            is_prime = False
            break
        else:
            is_prime = True
    if is_prime is True:
        primes.append(i)
print('Primes:', primes)
print('Not Primes:', not_primes)
