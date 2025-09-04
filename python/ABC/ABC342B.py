N = int(input())
P = list(map(int, input().split()))
Q = int(input())
AB = [list(map(int, input().split())) for _ in range(Q)]

for a, b in AB:
    ai = P.index(a)
    bi = P.index(b)
    print(a if ai < bi else b)
