# 投票先を表す文字列
S = input()

# 1 番目から 5 番目の立候補者への投票数
vote_count = [0, 0, 0, 0, 0]

def check_vote(x, vote_count):
    for i in range(5):
        if i == x-1:
            vote_count[i] += 1

for vote in S:
    # i 番目の投票した立候補者
    x = int(vote)

    # 立候補者が誰かで場合分け
    check_vote(x, vote_count)

# 最終的な投票数を答える
for count in vote_count:
    print(count)
