from itertools import permutations

N, M = map(int, input().split())
S = [input() for _ in range(N)]

# 順列全探索
for per in permutations(S, N):
    for i in range(N - 1):
        count = 0
        # 隣の文字列と比較して、文字が違う箇所をカウント
        for j in range(M):
            if per[i][j] != per[i + 1][j]:
                count += 1
        # カウントが2以上ならその順列はパスして次の順列へ
        if count > 1:
            break
    else:
        print("Yes")
        exit()
else:
    print("No")

"""
順列全探索
自力で実装
"""
