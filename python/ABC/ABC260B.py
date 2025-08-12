N, X, Y, Z = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# (優先度) 得点降順・同点は受験番号昇順で並べたいので (-score, id) でソート
math = [(-A[i], i + 1) for i in range(N)]
eng = [(-B[i], i + 1) for i in range(N)]
both = [(-(A[i] + B[i]), i + 1) for i in range(N)]

math.sort()
eng.sort()
both.sort()

picked = set()

# 数学から X 人
cnt = 0
for _, idx in math:
    if cnt == X:
        break
    if idx not in picked:
        picked.add(idx)
        cnt += 1

# 英語から Y 人
cnt = 0
for _, idx in eng:
    if cnt == Y:
        break
    if idx not in picked:
        picked.add(idx)
        cnt += 1

# 合計から Z 人
cnt = 0
for _, idx in both:
    if cnt == Z:
        break
    if idx not in picked:
        picked.add(idx)
        cnt += 1

# 受験番号の昇順で出力
picked = list(picked)
picked.sort()
print(*picked, sep="\n")
