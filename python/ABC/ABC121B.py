N, M, C = map(int, input().split())
B = list(map(int, input().split()))
A = [list(map(int, input().split())) for i in range(N)]

# print(B)
# print(A)

judge = []
for row in A:
    temp = 0
    for x, y in zip(row, B):
        temp += x * y
    judge.append(temp + C)

# print(judge)
print(sum(1 for i in judge if i > 0))
