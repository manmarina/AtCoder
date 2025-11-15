N = int(input())
S = list(input())
Q = int(input())
TAB = [list(map(int, input().split())) for _ in range(Q)]
# print(TAB)

flip = 0
for t, a, b in TAB:
    if t == 1:
        a -= 1
        b -= 1
        if not flip:  # flip == 1の時 そのまま入れ替える
            S[a], S[b] = S[b], S[a]
        else:  # flip == 0の時 インデックスをflipしてから入れ替える
            if a < N:
                a += N
            else:
                a -= N
            if b < N:
                b += N
            else:
                b -= N
            S[a], S[b] = S[b], S[a]
    else:  # t == 2:
        flip = flip ^ 1  # flagを反転する

if flip:  # flip == 1の時
    Sr = S[N:] + S[:N]
    print(*Sr, sep='')
else:  # flip == 0の時
    print(*S, sep='')

"""
計算量を削減したクエリ処理
実際にFLIPするとO(N)かかってしまうので、配列は変更せずインデックスをFLIPする。

hamayanhamayanの解説
https://blog.hamayanhamayan.com/entry/2021/04/25/002202

https://atcoder.jp/contests/abc199/tasks/abc199_c
"""
