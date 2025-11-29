import math

D = int(input())

ans = 10**30
Y = int(math.isqrt(D))  # 最大スタート

for X in range(int(math.isqrt(D)) + 1):
    # Y を可能な範囲で減らす
    while Y >= 0 and X * X + Y * Y > D:
        Y -= 1

    # Y が有効ならチェック
    if Y >= 0:
        ans = min(ans, abs(X * X + Y * Y - D))

    # その一個上の Y (Y+1) もチェックしておく（ちょうど超えた点）
    if Y + 1 <= int(math.isqrt(D)):
        ans = min(ans, abs(X * X + (Y + 1) * (Y + 1) - D))

print(ans)

"""
工夫して探索の通り数を減らす全探索
けんちょん
https://drken1215.hatenablog.com/entry/2023/11/26/203211
X,Yとも最大値はDの平方根未満
Xを固定してYをDの平方根から探索する

https://atcoder.jp/contests/abc330/tasks/abc330_c
https://chatgpt.com/g/g-p-688d3155796881919ed997146b54eec1-atcoder/c/692ac9ea-2efc-8320-9b79-b5afda91c10c
"""
