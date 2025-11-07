ABC = list(map(int, input().split()))

ABC.sort()
if (ABC[1] - ABC[0]) % 2 == 0:  # 最大以外の数の差が偶数の時
    print(((ABC[2] - ABC[0]) + (ABC[2] - ABC[1])) // 2)
else:  # 最大以外の数の差が奇数の時
    print(((ABC[2] - ABC[0]) + (ABC[2] - ABC[1])) // 2 + 2)

"""
数学的気づき系
偶奇を考える。

https://atcoder.jp/contests/abc093/tasks/arc094_a
"""
