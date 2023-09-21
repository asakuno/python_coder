# 円周率を表す変数
PI = 3.14

def get_area(r: int) -> float:
    print(r * r * PI)

round = [4, 7, 10, 15, 24]

for r in round:
    get_area(r)