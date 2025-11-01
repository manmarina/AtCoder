A, B, C = map(int, input().split())

if C % 2 == 0:  # Cが偶数のとき
    # 絶対値の大小関係
    if abs(A) < abs(B):
        res = "<"
    elif abs(A) > abs(B):
        res = ">"
    else:
        res = "="
else:  # Cが奇数のとき
    # 普通の大小関係
    if A < B:
        res = "<"
    elif A > B:
        res = ">"
    else:
        res = "="

print(res)

"""
場合分け系
けんちょん
https://drken1215.hatenablog.com/entry/2024/05/19/230920
まともに計算するとものすごい桁数になります。
そこで、問題の条件を分かりやすいものに言い換えるのをやってみましょう。

https://atcoder.jp/contests/abc205/tasks/abc205_c
https://chatgpt.com/g/g-p-688d3155796881919ed997146b54eec1-atcoder/c/6905aa49-7d1c-8322-a927-455e9d76ebbc
"""
