teams = {
    "arurus": ["aruru", "erara", "ukuku", "usisi", "totoro"],
    "algos": ["dijkstra", "prim", "kruskal"],
    "ramdoms": ["fadj", "vuiawqpv", "qpcuvauavhjzcrb"],
    "keybords": ["qwerty", "yuiop", "asdf", "ghjkl"],
    "bocchi": ["hitori"]
}
# このコードには「for 文の中身が複雑で理解しにくい」という欠点があります。
# この欠点を解決するために、次の 2 つの判定ロジックを関数で切り出してください。

# ・あるチームのメンバーリスト list_members について、文字 c を含むメンバーがいるか
# ・teams のそれぞれのメンバーリストについて、文字 c を含むメンバーがどのチームにもいるか
# その上で、このコードを「条件を満たす英文字」を改行区切りで出力するものに書き換えてください。

# team に文字 c を含む人が一人でもいるなら True, 一人もいないなら False
def team_has_c(team_members, c):
    for name in team_members:
        if c in name:
            return True
    return False

# teams に文字 c を含む人がいないチームがなければ True, あれば False
def all_teams_have_c(teams, c: str):
    for team_members in teams.values():
        if not team_has_c(team_members, c):
            return False
    return True

for c_num in range(ord("a"), ord("z") + 1):
    c = chr(c_num)
    # 条件を満たす文字を出力する
    if all_teams_have_c(teams, c):
        print(c)