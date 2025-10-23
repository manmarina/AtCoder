S = input()

ans = 0
for s in S:
    ans = ans * 26 + (ord(s) - ord('A') + 1)
print(ans)

"""
数学的な気づき系 n進数変換
26進数 -> 10進数変換

https://atcoder.jp/contests/abc285/tasks/abc285_c
"""
