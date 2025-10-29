N = int(input())
A = list(map(int, input().split()))

counter = {}
ans = 0

for i in range(N):
    a = A[i]
    # j - A[j] = i + A[i] を満たす個数を加算
    ans += counter.get(i - a, 0)  # 一つのj - A[j]が複数のi + A[i]とペア成立
    # i + A[i] のカウンタを進める
    counter[i + a] = counter.get(i + a, 0) + 1

# print(counter)
# print(ans)

"""
計算量を削減したシミュレーション
yuulis
https://yuulis.hatenablog.com/entry/ABC-417-C
難しい。。

どう数えるのか（考え方）
左側（過去の i）について、
各 i の値 A[i] + i を辞書 counter に記録しておく。
→ 「この値を持つ i が何個あるか」を保存。

現在の j に対して、
j - A[j] を計算し、それと同じ値の A[i] + i が過去にあればペア成立。

チャッピーの「例で確認」をみるとなんとか理解できる。

https://atcoder.jp/contests/abc417/tasks/abc417_c
https://chatgpt.com/g/g-p-688d3155796881919ed997146b54eec1-atcoder/c/69008615-d0bc-8323-bcdf-e5cba57c16ad
"""
