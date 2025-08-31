H, M = map(int, input().split())

TOTAL = 24 * 60
start = H * 60 + M

for t in range(TOTAL):
    cur = (start + t) % TOTAL
    h, m = divmod(cur, 60)
    A, B = divmod(h, 10)  # 時の十/一
    C, D = divmod(m, 10)  # 分の十/一
    hh = A * 10 + C       # 右上(C)と左下(B)を入れ替え後の「時」
    mm = B * 10 + D       # と「分」
    if 0 <= hh < 24 and 0 <= mm < 60:
        print(h, m)       # 先頭ゼロなしでも可
        break
