
class Calculator:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b
    
    def substract(self):
        return self.a - self.b

    def multiply(self):
        return self.a * self.b

    def divide(self):
        try:
            return self.a / self.b
        except ZeroDivisionError:
            return '0으로 나눌 수 없습니다.'

print(Calculator(1, 2).add())
print(Calculator(2, 1).substract())
print(Calculator(3, 4).multiply())
print(Calculator(4, 0).divide())