# module_6_1.py
# Зачем нужно наследование

class Animal:
    alive = True
    fed = False
    name = None

    def eat(self, food):
        if food.edible is True:
            print(f'{self.name} съел {food.name}')
            self.alive = True
            self.fed = True
        else:
            print(f'{self.name} не стал есть {food.name}')
            self.alive = False
            self.fed = False


class Plant:
    edible = False
    name = None

    def eat(self, food):
        self.food = food
        pass


class Mammal(Animal):
    def __init__(self, name):
        self.name = name


class Predator(Animal, Plant):
    def __init__(self, name):
        self.name = name


class Flower(Plant):
    def __init__(self, name):
        self.name = name


class Fruit(Plant):
    edible = True

    def __init__(self, name):
        self.name = name


a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)

# Что произошло: Хищник попытался съесть цветок и погиб, млекопитающее съело фрукт и насытилось.
