H, W = map(int, input().split())
S = []
for _ in range(H):
    S.append([*input()])
# print(S)

for i in range(H):
    for j in range(W-1):
        if S[i][j] == 'T' and S[i][j+1] == 'T':
            S[i][j] = 'P'
            S[i][j+1] = 'C'
# print(S)
for row in S:
    print(*row, sep='')

"""
文字列操作
TTをPCに置き換える問題。

けんちょんの解説
https://drken1215.hatenablog.com/entry/2023/06/02/031300

https://atcoder.jp/contests/abc297/tasks/abc297_c/editorial
"""
