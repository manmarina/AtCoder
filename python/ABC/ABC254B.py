N = int(input())

prev = []
for i in range(1, N + 1):  # 1行目からN行目
    row = [1] * i          # 端は1で初期化
    for j in range(1, i - 1):
        row[j] = prev[j - 1] + prev[j]
    print(*row)
    prev = row
