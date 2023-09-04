# 標準入力から値を受け取る
# S: str 型
S = input()

# 受け取った値を利用してコードを書いてください
def change_string(S: str):
    result = ""
    for s in S:
        if s == "a":
            result += "b"
        elif s == "b":
            result += "c"
        else:
            result += "a"
    return result

for i in range(3):
    S = change_string(S)
    print(S)