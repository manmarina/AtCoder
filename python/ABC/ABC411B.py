N = int(input())
D = list(map(int, input().split()))

# S[0]=0, S[k]=D1+...+Dk (長さ N) 累積和テーブルを作成
S = [0] * (N)
for k in range(1, N):
    S[k] = S[k - 1] + D[k - 1]
print(S)

for i in range(1, N):               # i: 1..N-1
    row = []
    for j in range(i + 1, N + 1):       # j: i+1..N
        dist = S[j - 1] - S[i - 1]
        row.append(str(dist))
    print(" ".join(row))
