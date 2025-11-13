S = input().strip()
K = int(input())

ichinum = 0
for i in range(len(S)):
    if S[i] == '1':
        ichinum += 1
    else:
        break

if ichinum >= K:
    print(1)
else:
    print(S[ichinum])

"""
場合分け系
けんちょん
https://drken1215.hatenablog.com/entry/2018/09/03/224200
1 だけはそのまま残るが、それ以外は途方もなく多い個数になる。よって、
先頭の 1 が K 個以上だったら 1
そうでなかったら、「先頭から見て最初の 1 以外の数」
が答え

自分の実装よりifが少なくて美しい。

https://atcoder.jp/contests/abc106/tasks/abc106_c
https://chatgpt.com/g/g-p-688d3155796881919ed997146b54eec1-atcoder/c/6915bf02-8f30-8324-a14b-fb86ce2e63f9
"""
