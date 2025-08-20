def is_prime(n):
    if n % 2 == 0:
        return False
    if n < 2:
        return False
    if n == 2:
        return True
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


def is_like_2017(n):
    if not is_prime(n):
        return 0
    if not is_prime((n + 1) // 2):
        return 0
    return 1


MAX_NUM = 10**5

cs = [0] * (MAX_NUM + 1)

for i in range(1, MAX_NUM + 1):
    cs[i] = cs[i - 1] + is_like_2017(i)

Q = int(input())
for i in range(Q):
    l, r = map(int, input().split())
    print(cs[r] - cs[l - 1])
