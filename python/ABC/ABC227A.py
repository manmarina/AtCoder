# 入力の受け取り
N, K, A = map(int, input().split())

# (A+K-1)をNで割った余り
ans = (A+K-1) % N

# ansが「0」ならば
if ans == 0:
    # Nを出力
    print(N)
# そうでないなら(「0」以外なら)
else:
    # ansを出力
    print(ans)
