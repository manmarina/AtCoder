N, M, X = map(int, input().split())
A = list(map(int, input().split()))

# print(A)

count_left = sum(1 for a in A if a < X)
count_right = sum(1 for a in A if X < a < N)
print(min(count_left, count_right))
