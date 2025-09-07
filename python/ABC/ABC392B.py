N, M = map(int, input().split())
A = list(map(int, input().split()))

seen = [False] * (N + 1)
for x in A:
    seen[x] = True

miss = [i for i in range(1, N + 1) if not seen[i]]
print(len(miss))
print(*miss)  # len==0 のときは空行になる
