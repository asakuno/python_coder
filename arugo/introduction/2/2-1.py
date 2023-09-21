# 標準入力から値を受け取る
# month: int 型
month = int(input())

# 受け取った値を利用してコードを書いてください

if month == 2:
    print(28)
elif month == 4 or month == 6 or month == 9 or month == 11:
    print(30)
else:
    print(31)