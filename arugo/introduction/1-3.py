# 標準入力から値を受け取る
# S: str 型
S = input()

# 十二支の動物名を平仮名で格納したリスト
ZODIAC = [
    "ねずみ", "うし", "とら", "うさぎ", "たつ", "へび",
    "うま", "ひつじ", "さる", "にわとり", "いぬ", "いのしし" 
]

cnt = 0
for i in ZODIAC:
    if i == S:
        print('Yes')
        cnt += 1


if cnt == 0:
    print("No")
