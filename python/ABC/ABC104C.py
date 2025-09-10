D, G = map(int, input().split())
p = []
c = []
for i in range(D):
    pi, ci = map(int, input().split())
    p.append(pi)
    c.append(ci)

INF = 10**18
ans = INF

for mask in range(1 << D):
    score = 0
    used = 0
    # まず「全問解く」と決めた種類を加算
    for i in range(D):
        if (mask >> i) & 1:
            score += 100 * (i + 1) * p[i] + c[i]
            used += p[i]

    if score >= G:
        ans = min(ans, used)
        continue

    # 届かない分を高い種類から貪欲に埋める（ボーナスは狙わない → p[i]-1 まで）
    need = G - score
    for i in reversed(range(D)):  # i = D-1, D-2, ..., 0
        if (mask >> i) & 1:
            continue
        v = 100 * (i + 1)
        max_take = p[i] - 1
        if max_take <= 0:
            continue
        k = (need + v - 1) // v  # ceil_div
        take = min(max_take, k)
        score += take * v
        used += take
        need = G - score
        if need <= 0:
            ans = min(ans, used)
            break

print(ans)

"""
ざっくり言うと「bit 全探索 + 貪欲での穴埋め」です。
ポイントは「ボーナスは“全部解いたとき”しか入らない」ので、
“全部解く集合”をまず決め打ちし、足りない分を高得点問題から貪欲に埋める、
という二段構えにします。

1.「全問解く種類の集合」を bitmask で全探索
2.マスクで得た得点を score とし、まだ G に届かないなら“残りの種類”から貪欲に追加
3.こうして達成できたら、そのときの 解答数の最小値を更新。
4.すべてのマスクに対して試し、最小解答数が答え。
"""
