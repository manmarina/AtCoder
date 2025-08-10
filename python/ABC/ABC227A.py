N, K, A = map(int, input().split())

box1 = [i for i in range(A, N+1)]
box2 = [i for i in range(1, N+1)]

for i in range(1000//N + 1):
    box1 += box2

print(box1[K-1])
