# 標準入力から値を受け取る
# S: str 型
S = input()
strings = []
# 受け取った値を利用してコードを書いてください
for i in S:
    if i == "o":
        strings.append("x")
    else:
        strings.append("o")

print(''.join(strings))
