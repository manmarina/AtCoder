N, M = map(int, input().split())
A = list(map(int, input().split()))

ok = set(i for i in range(1, M + 1))
# print(ok)

count = 0
for i in range(N):
    sa = set(A)
    if not (ok <= sa):  # 部分集合の判定 ok not in saでは駄目
        # print(count)
        break
    A.pop()
    count += 1

print(count)
