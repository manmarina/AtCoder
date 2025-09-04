N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    # i 行の中で 1 になっている列を探す
    nei = [str(j + 1) for j in range(N) if A[i][j] == 1]
    print(" ".join(nei))  # 空なら空行になる
