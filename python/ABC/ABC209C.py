N = int(input())
C = list(map(int, input().split()))
C.sort()  # 昇順ソート

ans = 1
for i in range(N):
    # ある項の数は、前の項の数から-1したもので、すべての項の積が答えとなる
    # ある項の数は、前の項の数よりも大きくなくてはならない 大きくなれないときは0
    ans = ans * max(0, C[i] - i) % 1000000007  # ある項が0なら答えも0
print(ans)

"""
数学的な気づき系
制約（＝重複禁止） を加えた直積（順番あり・重複あり）
昇順に並べて、前まで使った数を引いて掛け算する問題。
チャッピーの解説を読むとすぐ理解できる。

解説
https://atcoder.jp/contests/abc209/editorial/2228

https://atcoder.jp/contests/abc209/tasks/abc209_c
https://chatgpt.com/g/g-p-688d3155796881919ed997146b54eec1-atcoder/c/690ab1fe-4354-8323-aa89-1b439319b150
"""
