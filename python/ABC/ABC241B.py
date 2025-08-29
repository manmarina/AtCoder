from collections import Counter

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

cnt = Counter(A)

# print(cnt)

for b in B:
    if cnt[b] == 0:
        print("No")
        break
    cnt[b] -= 1
else:
    print(("Yes"))
