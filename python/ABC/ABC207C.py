N = int(input())

t = [0] * N
l = [0] * N
r = [0] * N

for i in range(N):
    t[i], l[i], r[i] = map(int, input().split())
    l[i] *= 2  # 0.5 -> 1　整数で　扱えるように。
    r[i] *= 2  # 0.5 -> 1　整数で　扱えるように。

    # すべてのパターンで「左閉区間・右開区間」となるように揃える
    if t[i] == 1:
        r[i] += 1  # 0.5加算を整数で 右を開区間に
    elif t[i] == 3:
        l[i] += 1  # 0.5加算を整数で 左を閉区間に
        r[i] += 1  # 0.5加算を整数で 右を開区間に
    elif t[i] == 4:
        l[i] += 1  # 0.5加算を整数で 左を閉区間に

# 全探索
res = 0
for i in range(N):
    for j in range(i + 1, N):
        # 261Aと同じロジック
        L = max(l[i], l[j])
        R = min(r[i], r[j])
        if L < R:  # 大きい方の左が、小さい方の右よりも小さい時
            res += 1  # 共通部分ありとしてカウント

print(res)

"""
閉区間・半開区間・開区間

けんちょん
https://drken1215.hatenablog.com/entry/2024/05/20/024952
261Aの判定法と同じ方法で判定する。
「左閉区間・右開区間」となるように揃えたい。そこで、0.5 を導入する。
浮動小数点型はあまり扱いたくないため、全体を 2 倍して整数値のみで解いた。

https://atcoder.jp/contests/abc207/tasks/abc207_c
https://chatgpt.com/g/g-p-688d3155796881919ed997146b54eec1-atcoder/c/6908405d-8b1c-8322-80ef-77bf57793091
"""
