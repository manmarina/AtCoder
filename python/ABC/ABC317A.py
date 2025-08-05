N, H, X = map(int, input().split())
P = list(map(int, input().split()))

diff = X - H
for index, value in enumerate(P):
    if value >= diff:
        print(index + 1)
        break
