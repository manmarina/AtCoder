N = int(input())
A = list(map(int, input().split()))

pairs = [(i, v) for i, v in enumerate(A, 1)]
pairs.sort(key=lambda x: x[1])

# print(pairs)

print(pairs[-2][0])
