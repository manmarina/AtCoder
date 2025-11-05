N, M = map(int, input().split())
A = list(map(int, input().split()))
print(A)

B = [0] * (max(A) + 1)
for a in A:
    B[a] += 1
print(B)

cs = [0] * (max(A) + 1)
for i in range(1, len(cs)):
    cs[i] = cs[i - 1] + B[i]
print(cs)

ans = 0
for i in range(1, len(cs) - M + 1):
    # print('i:', i, "i+M-1:", i + M - 1)
    ans = max(ans, cs[i + M - 1] - cs[i - 1])

print(ans)


"""
TLE
配列のサイズが大きすぎる!（最大10^9）

けんちょん
https://drken1215.hatenablog.com/entry/2023/11/11/204912

https://atcoder.jp/contests/abc326/tasks/abc326_c
"""
