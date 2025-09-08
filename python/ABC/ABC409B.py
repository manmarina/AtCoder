N = int(input())
A = list(map(int, input().split()))

A.sort(reverse=True)
# print(A)

ans = 0
for i, v in enumerate(A, start=1):  # iは“候補x”
    if v >= i:
        ans = i
    else:
        break
print(ans)

"""
3
100 100 1
の答えは
2
"""
