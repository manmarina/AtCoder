N, M = map(int, input().split())
PS = [list(input().split()) for _ in range(M)]

flag_AC = [False] * (N + 1)  # ACしたかどうかのフラグ
pool_WA = [0] * (N + 1)  # ACするまでのWA数をプールしておく
AC = 0  # AC数
WA = 0  # ペナルティ数
for p, s in PS:
    p = int(p)
    if not flag_AC[p]:  # ACしていなければ
        if s == "WA":
            pool_WA[p] += 1  # WA数をプール
        else:  # s == "AC"
            flag_AC[p] = True  # ACしたフラグを立てる
            AC += 1  # ACをカウントする
            WA += pool_WA[p]  # プールしておいたWAをカウントする

print(AC, WA)

"""
シミュレーション + バケット
高橋君のペナルティ数は、高橋君が AC を 1 回以上出した各問題において、初めて AC を出すまでに出した WA の数の総和です。
という条件を見逃さないこと！！

けんちょんの解説
https://drken1215.hatenablog.com/entry/2020/01/12/230200

https://atcoder.jp/contests/abc151/tasks/abc151_c
https://chatgpt.com/g/g-p-688d3155796881919ed997146b54eec1-atcoder/c/6910db69-6798-8322-8edd-325c925bb4e9
"""
