N, A = map(int, input().split())
T = list(map(int, input().split()))

cur = 0
for t in T:
    start = max(cur, t)
    finish = start + A
    print(finish)
    cur = finish
