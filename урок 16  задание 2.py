 
class Turtle:

    def __init__(self, x, y, s):

        self.x = x

        self.y = y

        self.s = s

    def go_up(self):

        self.y += self.s

        return self.y

    def go_down(self):

        self.y -= self.s

        return self.y

    def go_left(self):

        self.x -= self.s

        return self.x

    def go_right(self):

        self.x += self.s

        return self.y

    def evolve(self):

        self.s += 1

        return self.s

    def degrade(self):

        if self.s <= 0:

            print('s = 0')

            return

            self.s -= 1

            return self.s

    def count_moves(self, x2, y2):

        return self.x-x2, self.y- y2

        res = Turtle(5, 15, 26)

print(res.go_up())

print(res.go_down())

print(res.go_left())

print(res.go_right())

print(res.evolve())

print(res.degrade())

print(res.count_moves(12,10))
