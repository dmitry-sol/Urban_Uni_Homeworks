# module_6_3
# "Множественное наследование"

class Horse:

    x_distance = 0
    sound = 'Frrr'

    def run(self, dx):
        self.dx = dx
        return self.x_distance + self.dx

class Eagle:

    y_distance = 0
    sound = 'I train, eat, sleep, and repeat'

    def fly(self, dy):
        self.dy = dy
        return self.y_distance + self.dy

class Pegasus(Horse, Eagle):
    # def __init__(self, *arg):


    def move(self, dx, dy):
        self.run(dx)
        self.fly(dy)

    def get_pos(self):
        return (self.x_distance, self.y_distance)

    def voice(self):
        return self.sound


p1 = Pegasus()

print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())

p1.voice()