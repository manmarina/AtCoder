N = int(input())
A = list(map(int, input().split()))

s = sum(1 / a for a in A)
print(1 / s)
