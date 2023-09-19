PI = 3.141 #マジックナンバーを避けるため具体的な数字は変数に入れておく

def get_area(r: int) -> float:
    print(r*r*PI)

round = [3, 5, 8, 12, 20]

for r in round:
    get_area(r)