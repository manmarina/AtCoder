from collections import defaultdict

N = int(input())

# インプットしながら連想配列Sにビットを追加
S = defaultdict(int)
for i in range(N):
    S[input()] = 1


# ビットを合計して表示
print(sum(v for v in S.values()))
