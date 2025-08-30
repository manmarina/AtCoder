A, B, C, D, E, F = map(int, input().split())

mod = 998244353
ABC = (A % mod) * (B % mod) * (C % mod)
DEF = (D % mod) * (E % mod) * (F % mod)
ans = (ABC - DEF) % mod
print(ans)
