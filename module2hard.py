# module2hard
# Simple Way

numbers = int(input('Введите число от 3 до 20: '))
password = []
psw = ''

for j in range(numbers-1):
    for k in range(numbers-1):
        a = j + 1
        b = a + k + 1
        s = a + b
        if numbers % s == 0:
            psw = psw + str(a) + str(b)
            if s == numbers:
                break

print(numbers, '-', psw)
print()
print()



# Complicated Way

number1 = int(input('Введите число начала промежутка от 3: '))
number2 = int(input('Введите число конца промежутка: '))

numbers = []
while number1 <= number2:
    numbers.append(number1)
    number1 += 1

password = []
length = len(numbers)

for i in range(length):
    psw = ''
    for j in range(numbers[i]):
        for k in range(numbers[i]):
            a = j + 1
            b = a + k + 1
            s = a + b
            if numbers[i] % s == 0:
                psw = psw + str(a) + str(b)
            if s >= numbers[i]:
                break

    password.append(psw)

print()
for i in range(length):
    print(numbers[i], '-', password[i])