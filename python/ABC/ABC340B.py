Q = int(input())
q = [list(map(int, input().split())) for _ in range(Q)]

ans = []
for q1, q2 in q:
    if q1 == 1:
        ans.append(q2)
    else:  # q1 == 2
        print(ans[-q2])
