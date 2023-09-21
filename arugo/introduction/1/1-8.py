# 標準入力から値を受け取る
# S: str 型
S = input()

# 重複を消すset関数
string_set = set()
# 受け取った値を利用してコードを書いてください
for s in S:
    string_set.add(s)

print(len(string_set))

# 別解
T = ""

# S の各文字 c について場合分けを行い、 T を生成する
for c in S:
    if c == "o":
        T += "x"
    else:
        T += "o"

# 答えを出力する
print(T)