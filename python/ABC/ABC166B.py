N, K = map(int, input().split())

A = []
for _ in range(K):
    d = int(input())
    A.append(list(map(int, input().split())))

treat = {v for sub in A for v in sub}

# print(A)
# print(treat)

print(N - len(treat))
