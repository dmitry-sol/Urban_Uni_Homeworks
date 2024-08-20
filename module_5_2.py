# module_5_2
# Специальные методы классов

class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __len__ (self):
        return self.number_of_floors

    def __str__(self):
        return f'Название: {self.name}, количество этажей: {self.number_of_floors}'




h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)
h3 = House('Горный воздух', 5)
h4 = House('Сосновый бор', 12)

print(h1)
print(h2)
print(h3)
print(str(h4))

print()
print(len(h1))
print(len(h2))
print(len(h3))
print(len(h4))
