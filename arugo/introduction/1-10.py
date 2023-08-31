# 標準入力から値を受け取る
# S: str 型
S = input()

string = ""
# 受け取った値を利用してコードを書いてください
for s in S:
    if s == "a":
        string += "b"
    elif s == "b":
        string += "c"
    else:
        string += "a"

print(string)