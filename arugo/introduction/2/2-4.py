# 円周率を表す変数
PI = 3.14

# ここに答えとなるコードを書いてください
def computed_round(r: int) -> int:
    return print(f"半径 {r} cm の円の面積は {r * r * PI} cm^2")

def computed_cylinder(r: int, h: int) -> int:
    return print(f"底面の半径が {r} cm、高さが {h} cm の円柱の体積は {r * r * PI * h} cm^3")

computed_round(3)
computed_round(5)
computed_round(10)
computed_cylinder(2,4)
computed_cylinder(6,10)
computed_cylinder(10,3) 