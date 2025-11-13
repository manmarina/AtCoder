S = input()
K = int(input())

# 先頭に1が続く場合
i = 0
if K == 1:  # 1文字しかない時
    s = S[0]

elif S[0] == '1':  # 先頭が1の時
    while i < K and S[i] == '1':  # 1がならぶ間iを伸ばす
        i += 1
    if i != K:  # iがK以外の時
        s = S[i]  # sは1以外の数字
    else:  # iがkの時（Siがすべて1だった時）
        s = '1'  # sは1

    if K <= i:  # Kが1がならぶ数以下の時
        print(1)
        exit()

else:  # 先頭が1以外の時
    s = S[0]

print(s)

"""
場合分け系
1 だけはそのまま残るが、それ以外は途方もなく多い個数になる。よって、
先頭の 1 が K 個以上だったら 1
そうでなかったら、「先頭から見て最初の 1 以外の数」
が答え

けんちょんの解説
https://drken1215.hatenablog.com/entry/2018/09/03/224200

https://atcoder.jp/contests/abc106/tasks/abc106_c
"""
