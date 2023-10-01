# 演算	演算子	特殊メソッド
# 足し算	+	__add__
# 引き算	-	__sub__
# 掛け算	*	__mul__
# 通常の割り算	/	__truediv__
# 整数での割り算の商	//	__floordiv__
# 整数での割り算の余り	%	__mod__
# 累乗	**	__pow__

class Pair:
    def __init__(self, first, second):
        self.first = first
        self.second = second
    def __str__(self):
        return f"({self.first}, {self.second})"
    def __add__(self, other):
        return Pair(self.first + other.first, self.second + other.second)
    # ここに __sub__ メソッドを書いてください
    def __sub__(self, other):
        return Pair(self.first - other.first, self.second - other.second)
    
a = Pair(2, 3)
b = Pair(1, 5)
print(a - b)