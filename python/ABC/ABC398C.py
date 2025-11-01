from collections import Counter


N = int(input())
A = list(map(int, input().split()))

cnt = Counter(A)
# print(cnt)

ans = []
for i, v in cnt.items():
    if v == 1:
        ans.append(i)
# print(ans)

if not ans:
    print(-1)
else:
    print(A.index(max(ans))+1)

"""
バケットと連想配列
295Cと似た問題。
連想配列で集計するといい感じに解ける！

https://atcoder.jp/contests/abc398/tasks/abc398_c
"""
