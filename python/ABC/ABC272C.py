N = int(input())
A = list(map(int, input().split()))

# 配列を偶数,奇数を分けて作成
evens = [x for x in A if x % 2 == 0]
odds = [x for x in A if x % 2 == 1]

ans = -1
# 偶数 + 偶数の場合
if len(evens) >= 2:
    evens.sort(reverse=True)
    ans = max(ans, evens[0] + evens[1])

# 奇数 + 奇数の場合
if len(odds) >= 2:
    odds.sort(reverse=True)
    ans = max(ans, odds[0] + odds[1])

print(ans)

"""
数学的な気づき系
チャッピー
偶奇を考える
和が偶数になる時は偶数 + 偶数、もしくは、奇数 + 奇数であることを見抜く。

偶数の和は：
偶数 + 偶数
奇数 + 奇数
で作れます。
したがって、
偶数の中で大きい2つ
奇数の中で大きい2つ
をそれぞれ求めて、それらの和のうち最大を答えればOKです。

https://atcoder.jp/contests/abc272/tasks/abc272_c
https://chatgpt.com/g/g-p-688d3155796881919ed997146b54eec1-atcoder/c/69084f3c-9eb0-8321-aa28-f9d84893c5e5
"""
