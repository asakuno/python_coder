import random # random モジュールを読み込む

random.seed(42) # シードに 42 を指定する

num = [] # サイコロの出目 (1 から 6 までの値をとる)
for i in range(1000):
    num.append(random.randint(1, 6))

# 正しい結果になっているか確認するために最初の 10 個を出力する
print(num[0:10]) # "[6, 1, 1, 6, 3, 2, 2, 2, 6, 1]" が出力されるはず

# 出目の出た回数を数えるリスト
# cnt[i]: i の出た回数
# こっちの方が書き方的に良い
# for i in range(1000):
#     cnt[num[i]] += 1

cnt = [0] * 7
for i in range(len(num)):
    for j in num:
        if i == j:
            cnt[i] += 1


# ここに出目の出た回数を数えるコードを書いてください

# 出目の出た回数を出力する
for i in range(1, 7):
    print(f"{i} が出た回数: {cnt[i]}")