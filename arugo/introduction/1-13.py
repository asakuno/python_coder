poll_info = [90, 60, 240, 30, 180]

# ここに poll_info を加工するコードを書いてください
ans = []
# poll_info を出力
n = sum(poll_info)
def print_num(list, number: int, count: int) -> int:
    for num in list:
        ans.append(int(num/number * 100))

print_num(poll_info, n, len(poll_info))
print(ans)