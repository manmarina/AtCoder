N = int(input())
S = list(map(int, input().split()))

LIMIT_S = 1000
LIMIT_AB = 997 // 7 + 1

ok = set()

for a in range(1, LIMIT_AB):
    for b in range(1, LIMIT_AB):
        temp = 4 * a * b + 3 * a + 3 * b
        if temp > LIMIT_S:
            break
        ok.add(temp)

print(sum(1 for i in S if i not in ok))
