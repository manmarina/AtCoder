N = int(input())
A = list(map(int, input().split()))

sA = set(A)
for i in range(2000 + 1):
    if i not in sA:
        print(i)
        break
