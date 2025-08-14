N, M = map(int, input().split())
AB = []
for i in range(N):
    AB.append(list(map(int, input().split())))

AB.sort(key=lambda x: x[0])

rest = M
total = 0
for i in range(N):
    if rest <= AB[i][1]:
        total += rest * AB[i][0]
        break
    else:
        total += AB[i][1] * AB[i][0]
        rest -= AB[i][1]

print(total)
