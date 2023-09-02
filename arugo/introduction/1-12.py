# 標準入力から値を受け取る
# S: str 型
S = input()
ans = []
# 受け取った値を利用してコードを書いてください
alpha = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

for s in S:
    for num in range(26):
        if alpha[num] == s:
            ans.append(alpha[num-3])

print(''.join(ans))