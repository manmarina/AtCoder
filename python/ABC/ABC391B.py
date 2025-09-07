N, M = map(int, input().split())
S = [input().rstrip() for _ in range(N)]
T = [input().rstrip() for _ in range(M)]

for a in range(N - M + 1):        # 0-indexの a は実際の a-1
    for b in range(N - M + 1):    # 0-indexの b は実際の b-1
        ok = True
        for i in range(M):
            # 行ごとにまとめて比較すると速く・簡潔
            if S[a + i][b:b + M] != T[i]:
                ok = False
                break
        if ok:
            print(a + 1, b + 1)   # 1-index に戻して出力
            raise SystemExit
