from collections import Counter


N = int(input())
A = list(map(int, input().split()))


cnt = Counter(A)  # 辺の長さ -> 本数
# print(cnt)

bars = []
for key in sorted(cnt.keys(), reverse=True):
    bars.append((key, cnt[key]))  # (辺の長さ,本数)のソートされたリストを作成
# print(bars)

box = []  # 選んだ辺を格納する
for l, v in bars:  # 辺の長さ、本数　を取り出す
    if v >= 4:  # 本数が4本以上のとき
        box.append(l)  # 長辺、短辺を格納する（同じ長さ）
        box.append(l)
    elif v >= 2:
        box.append(l)  # まず長辺分から格納する

    if len(box) >= 2:  # 長辺、短辺そろったら
        print(box[0] * box[1])  # 面積を計算して出力する
        exit()

print(0)  # 長辺、短辺が揃わなかった時

"""
貪欲法
長い辺から選択してゆく。

けんちょんの解説
https://drken1215.hatenablog.com/entry/2025/01/07/020940

https://atcoder.jp/contests/abc071/tasks/arc081_a
"""
