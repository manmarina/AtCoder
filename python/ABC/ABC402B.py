Q = int(input())
query = [list(map(int, input().split()))for _ in range(Q)]

que = []
for q in query:
    if q[0] == 1:
        que.append(q[1])
    else:  # q[0] == 2
        print(que.pop(0))
