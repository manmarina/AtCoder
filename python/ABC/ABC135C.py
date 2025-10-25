import logging
logging.basicConfig(level=logging.INFO, format='[%(levelname)s] %(message)s')


N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

cnt = 0
for i in range(N):
    mn = min(A[i], B[i])  # 左のモンスターを全力で攻撃する
    A[i] -= mn
    B[i] -= mn
    cnt += mn
    logging.debug(f"{A[i] = },{B[i] = },{mn = },{cnt = }")

    mn = min(A[i + 1], B[i])  # 余った力で右のモンスターを攻撃する
    A[i + 1] -= mn
    B[i] -= mn
    cnt += mn
    logging.debug(f"{A[i+1] = },{B[i] = },{mn = },{cnt = }")

print(cnt)

"""
貪欲法

左のモンスターを全力で攻撃、余りの力で右のモンスターを攻撃する

https://atcoder.jp/contests/abc135/tasks/abc135_c
"""
