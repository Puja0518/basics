
class Processor:
    def __init__(self, target):
        self.target = target

    def convert_square(self):
        return self.target*self.target

    def subtract_by_five(self):
        return self.target-5

    def multiply_by_hundred(self):
        return self.target * 100

t = Processor(4)
print(t.convert_square())

tar = Processor(6)
print(tar.convert_square())

targ = Processor(8)
print(targ.subtract_by_five())
print(targ.convert_square())
print(targ.multiply_by_hundred())


class Tools:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def addition(self):
        return self.x + self.y

    def multiplication(self):
        return self.x * self.y

    def subtraction(self):
        return self.x - self.y

value = Tools(8,5)
print(value.addition())
print(value.multiplication())
print(value.subtraction())
        