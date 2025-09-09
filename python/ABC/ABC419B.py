Q = int(input())
query = [list(map(int, input().split())) for _ in range(Q)]

bag = []
for q in query:
    if q[0] == 1:
        bag.append(q[1])
    else:  # q == 2
        print(bag.pop(bag.index(min(bag))))
