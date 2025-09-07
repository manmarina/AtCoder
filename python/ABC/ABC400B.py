N, M = map(int, input().split())
LIM = 10**9

if N == 1:
    ans = M + 1
    print(ans if ans <= LIM else "inf")
    exit()

s = 0  # s=すべての項の合計
t = 1  # N^0　t=今の項の値(N^i)
for i in range(M + 1):
    s += t
    if s > LIM:
        print("inf")
        break
    # 次の項 t *= N を作る前に安全判定
    if i < M:
        if t > LIM // N:  # t * N > LIM なら危険なので事前に判定
            print("inf")
            break
        t *= N
else:
    print(s)
