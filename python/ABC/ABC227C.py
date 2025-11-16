import sys
N = int(sys.stdin.readline())

ans = 0
a = 1
while a * a * a <= N:
    b = a
    while a * b * b <= N:
        cmax = N // (a * b)
        ans += (cmax - b + 1)  # c は b ~ cmax個ある
        b += 1
    a += 1
print(ans)

"""
工夫して探索の通り数を減らす全探索
けんちょん
https://drken1215.hatenablog.com/entry/2023/05/19/152200
「三重ループをしないで、上手に上限を切って二重ループに落とす」問題です。

https://atcoder.jp/contests/abc227/tasks/abc227_c
https://chatgpt.com/c/68d2873e-d528-8324-93ff-5db041ca4896
"""
