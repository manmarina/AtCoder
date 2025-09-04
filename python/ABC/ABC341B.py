N = int(input())
A = list(map(int, input().split()))
ST = [tuple(map(int, input().split())) for _ in range(N - 1)]

for i, (S, T) in enumerate(ST):
    k = A[i] // S
    A[i] -= k * S          # 省略可（以後使わない）
    A[i + 1] += k * T

print(A[-1])
