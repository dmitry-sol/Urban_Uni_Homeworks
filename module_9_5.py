# module_9_5
# Итераторы

class StepValueError(ValueError):
    def __init__(self, message='Шаг не может быть равен 0'):
        self.message = message


class Iterator:
    def __init__(self, start, stop, step=1):
        self.start = start
        self.stop = stop
        if step != 0:
            self.step = step
        else:
            raise StepValueError
        self.pointer = 0

    def __iter__(self):
        self.pointer = self.start
        return self

    def __next__(self):
        if (self.step > 0 and self.pointer <= self.stop) or (self.step < 0 and self.pointer >= self.stop):
            self.pointer += self.step
        else:
            raise StopIteration
        return self.pointer - self.step


try:
    iter1 = Iterator(100, 200, 0)
    for i in iter1:
        print(i, end=' ')
except StepValueError as exc:
    print(exc.message)
print()

try:
    iter2 = Iterator(-5, 1)
    for i in iter2:
        print(i, end=' ')
except StepValueError as exc:
    print(exc.message)
print()

try:
    iter3 = Iterator(6, 15, 2)
    for i in iter3:
        print(i, end=' ')
except StepValueError as exc:
    print(exc.message)
print()

try:
    iter4 = Iterator(5, 1, -1)
    for i in iter4:
        print(i, end=' ')
except StepValueError as exc:
    print(exc.message)
print()

try:
    iter5 = Iterator(10, 1)
    for i in iter5:
        print(i, end=' ')
except StepValueError as exc:
    print(exc.message)
