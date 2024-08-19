# module_5_1
# Атрибуты и методы объекта

class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        if new_floor > self.number_of_floors or new_floor < 1:
            print('Такого этажа не существует\n')
        else:
            floor = 1
            while floor <= new_floor:
                print(floor)
                floor +=1
            print()




h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h3 = House('Горный воздух', 12)
h4 = House('Сосновый бор', 6)
h1.go_to(5)
h2.go_to(10)
h3.go_to(12)
h4.go_to(-2)