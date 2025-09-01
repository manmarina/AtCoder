N = int(input())
X = list(map(int, input().split()))

trimed = sorted(X)[N:-N]
print(sum(trimed) / len(trimed))
