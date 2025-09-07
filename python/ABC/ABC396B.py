Q = int(input())
q = [list(map(int, input().split())) for _ in range(Q)]
# print(q)

pile = [0] * 100
# print(pile)

for que in q:
    if que[0] == 1:
        pile.append(que[1])
    else:
        print(pile.pop())
