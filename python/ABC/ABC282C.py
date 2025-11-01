N = int(input())
S = [*input()]

flag = False
for i in range(N):
    if S[i] == '"':  # "がでたらフラグを反転
        if flag:
            flag = False
        else:
            flag = True

    if S[i] == ',' and flag == False:  # フラグが経っていないときのカンマは
        S[i] = '.'  # ピリオドに変換する
print(*S, sep='')

"""
文字列操作
""で括られていないカンマをピリオドに変換する。

けんちょんの解説
https://drken1215.hatenablog.com/entry/2022/12/21/161217

https://atcoder.jp/contests/abc282/tasks/abc282_c
"""
