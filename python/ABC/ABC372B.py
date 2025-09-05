from math import log

M = int(input())

m = M
ans = []
while m > 0:
    p = int(log(m, 3))
    ans.append(p)
    m = m - 3**p
print(len(ans))
print(*ans)
