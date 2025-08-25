N = int(input())
K = int(input())
X = list(map(int, input().split()))
total = 0
for x in X:
    total += min(x, K - x)
print(total * 2)
