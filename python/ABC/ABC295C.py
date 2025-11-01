from collections import Counter

N = int(input())
A = list(map(int, input().split()))

cnt = Counter(A)
# print(cnt)

ans = 0
for v in cnt.values():
    ans += v // 2
print(ans)

"""
バケットと連想配列
連想配列で集計するといい感じに解ける！

けんちょんの解説
https://drken1215.hatenablog.com/entry/2024/11/08/002436

https://atcoder.jp/contests/abc295/tasks/abc295_c
"""
