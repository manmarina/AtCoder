N = int(input().strip())
S = [input().strip() for _ in range(N)]

wins = [row.count('o') for row in S]                  # 勝ち数を集計
# print(wins)

order = sorted(range(N), key=lambda i: (-wins[i], i))  # 勝ち降順→番号昇順
# print(order)

ans = [i + 1 for i in order]                          # 1-index化
print(*ans)
