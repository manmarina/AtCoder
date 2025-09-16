N = int(input())


def count_divisors(n: int) -> int:  # 約数の個数をカウント
    cnt = 0
    d = 1
    while d * d <= n:
        if n % d == 0:
            cnt += 1                # d
            if d * d != n:
                cnt += 1            # n//d（平方でないならペアをもう1つ）
        d += 1
    return cnt


ans = 0
for x in range(1, N + 1, 2):        # 奇数だけ
    if count_divisors(x) == 8:
        ans += 1
print(ans)

"""
奇数に限定して全探索
    偶数はそもそも数えない（ループを 1,3,5,… にするだけで半分カット）。
約数個数の数え方（√n まで）
    d を 1..√n で走らせ、d | n なら約数を 1 個（n/d が d と異なるならもう 1 個）足す。
"""
