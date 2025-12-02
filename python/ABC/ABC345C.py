from collections import Counter


S = input()

cnt = Counter(S)
# print(cnt)


def nC2(num):
    return num * (num - 1) // 2


ans = nC2(len(S))
# print(ans)

for v in cnt.values():
    if v > 1:
        ans -= (nC2(v) - 1)
print(ans)

"""
WA
"""
