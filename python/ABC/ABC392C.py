N = int(input())
P = list(map(int, input().split()))
Q = list(map(int, input().split()))

QP = [(q, p) for q, p in zip(Q, P)]  # (ゼッケン, 見つめられる人のインデックス)を格納
QP.sort()  # ゼッケンでソート
# print(QP)

ans = []
for _, p in QP:
    ans.append(Q[p - 1])  # 見つめられる人のインデックス -> 見つめられる人のゼッケンを出力
print(*ans)

"""
問題文の理解が難解系
誰が誰を見つめているのかわかりにくい。
出力例1の図でようやくわかった。

Pi = Qiのインデックス(人iを表す)
Qi = ゼッケンの数
QiはPiを見つめている（同じインデックス = 正面）
1が書かれたゼッケンの人からゼッケン順に出力する

https://atcoder.jp/contests/abc392/tasks/abc392_c
"""
