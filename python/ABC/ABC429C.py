from collections import Counter

N = int(input())
A = list(map(int, input().split()))

cnt1 = Counter(A)
cnt2 = [v for v in cnt1.values()]  # 同じ要素の数をカウントしたリスト
print(cnt1)
print(cnt2)


def nC2(n):
    return n * (n - 1) // 2


ans = 0
for c in cnt2:
    if c != 1:
        combi = nC2(c)  # 2つの等しい数の選び方
        count = N - c  # 残りの1つの選び方
        ans += combi * count

print(ans)

"""
工夫して探索の通り数を減らす全探索
同じ要素の数をカウントしたリストを作成する。
このリストを探索して、2以上のある値について探索してゆく。
2以上のものはnC2で選び方を探索し、その値と、残りの1つの選び方の積が、ある値に関する選び方の数となる。

https://atcoder.jp/contests/abc429/tasks/abc429_c
"""
