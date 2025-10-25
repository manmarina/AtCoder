from collections import Counter

N = int(input())
A = list(map(int, input().split()))

cnt1 = Counter(A)
cnt2 = [v for v in cnt1.values()]


def nC2(n):
    return n * (n - 1) // 2


total_count = len(A)
ans = 0
for c in cnt2:
    if c != 1:
        combi = nC2(c)
        count = total_count - c
        ans += combi * count

print(ans)
