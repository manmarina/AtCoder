M = int(input())
D = list(map(int, input().split()))

S = sum(D)
target = (S + 1) // 2  # ⌈S/2⌉

acc = 0
for i, di in enumerate(D, start=1):  # i: 月(1-indexed)
    if acc + di >= target:
        day = target - acc
        print(i, day)
        break
    acc += di
