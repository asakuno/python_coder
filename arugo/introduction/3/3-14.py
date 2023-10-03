import math

class MyFraction:
    def __init__(self, num, den):
        self.num = num
        self.den = den
        self.normalize()

    def normalize(self):
        if self.den < 0:
            self.num *= -1
            self.den *= -1
        g = math.gcd(self.num, self.den)
        self.num //= g
        self.den //= g

    def __str__(self):
        return f"{self.num}/{self.den}"

    def __add__(self, other):
        return MyFraction(self.num * other.den + self.den * other.num, self.den * other.den)

    def __sub__(self, other):
        return MyFraction(self.num * other.den - self.den * other.num, self.den * other.den)

    def __mul__(self, other):
        return MyFraction(self.num * other.num, self.den * other.den)

    def __truediv__(self, other):
        return MyFraction(self.num * other.den, self.den * other.num)

a = MyFraction(2, 3)
b = MyFraction(1, 6)

# ここで MyFraction インスタンスを文字列に変換して表示
print(f"{a} + {b} = {a + b}")  # 出力: 2/3 + 1/6 = 5/6
print(f"{a} - {b} = {a - b}")  # 出力: 2/3 - 1/6 = 1/2
print(f"{a} × {b} = {a * b}")  # 出力: 2/3 × 1/6 = 1/9
print(f"{a} ÷ {b} = {a / b}")  # 出力: 2/3 ÷ 1/6 = 4/1
