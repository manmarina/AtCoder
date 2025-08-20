N, K = map(int, input().split())
p = list(map(int, input().split()))


MAX_NUM = 2 * 10**5
cs = [0] * (MAX_NUM + 1)


def calc_ev(n):
    ev = 1 / n * (sum(i for i in range(1, n + 1)))
    return ev


for i, v in enumerate(p, 1):
    ev = calc_ev(v)
    cs[i] = cs[i - 1] + ev

mx = 0
for i in range(len(p) - K + 1):
    l = i
    r = i + K
    temp = cs[r] - cs[l]
    mx = max(mx, temp)


# print(cs)
print(mx)
