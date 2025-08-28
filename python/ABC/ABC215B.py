N = int(input())

n = 1
k = 0
while n * 2 <= N:
    n *= 2
    k += 1
print(k)
