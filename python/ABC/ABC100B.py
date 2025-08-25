D, N = map(int, input().split())

# 「100で割り切れるけど 10000では割り切れない数」だけが好きな数。
need = 100 ** D  # 少なくともこれで割り切れる必要がある。
need_more = 100 ** (D + 1)  # これは割り切れてはいけない。

cnt = 0
x = 1
while True:
    if x % need == 0 and x % need_more != 0:  # 条件を満たすか？
        cnt += 1
        if cnt == N:
            print(x)
            break
    x += 1
