from collections import defaultdict


N = int(input())
A = list(map(int, input().split()))
W = list(map(int, input().split()))

# 箱ごとに重みを格納
dd = defaultdict(list)
for b, w in zip(A, W):
    dd[b].append(w)
print(dd)

# 箱の中のグループで、最大値以外の合計を加算
ans = 0
for w in dd.values():
    if len(w) >= 2:
        w.sort()  # 箱の中のグループを昇順にソート
        ans += sum(w[:-1])  # 最後の（最大の）要素を除いて合計
print(ans)

"""
問題文の理解が難解系
リトライ
どの箱に何個荷物が入っているのかわかりにくい。
最初に考えたときよりは、すんなりと問題文の意味がわかった。
けんちょんのロジックとほぼ同じロジックで完成できた。

けんちょんの解説
https://drken1215.hatenablog.com/entry/2024/07/07/211832

https://atcoder.jp/contests/abc360/tasks/abc360_c
https://chatgpt.com/g/g-p-688d3155796881919ed997146b54eec1-atcoder/c/6909fff4-f16c-8320-93f2-c577a74c9d6b
"""
