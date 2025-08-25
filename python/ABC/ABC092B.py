N = int(input())
D, X = map(int, input().split())
A = [int(input()) for i in range(N)]

choco = [X]
for a in A:
    choco.append((D - 1) // a + 1)

print(sum(choco))
