N, X = map(int, input().split())
S = input()

point = X
for s in S:
    if s == 'x':
        point = max(0, point - 1)
    else:  # s == 'o'
        point += 1
print(point)
