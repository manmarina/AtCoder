N, M = map(int, input().split())
A = list(map(int, input().split()))
S = [input() for _ in range(N)]
# print(S)

point = [i for i in range(N + 1)]  # プレイヤー -> 獲得点数
answered = [set() for _ in range(N + 1)]  # プレイヤー -> 答えた問題番号のset
for i in range(N):  # 全プレイヤー
    for j in range(M):  # 全問題
        if S[i][j] == 'o':
            point[i + 1] += A[j]  # ポイントを加算
            answered[i + 1].add(j)  # 答えた問題番号をsetに格納
# print(point)
# print(answered)

# 追加で答える問題の得点リストを作成
B = []
for i in range(M):
    B.append((A[i], i))  # (配点, 問題番号)を追加
B = sorted(B, reverse=True)  # 配点を降順でソート
# print(B)

mx = max(point)  # 最高得点
for i in range(1, N + 1):  # 全プレイヤー
    j = 0  # 問題を走査するidx
    cnt = 0  # 追加で解く問題数をカウント
    p = point[i]  # プレイヤーiの得点
    while p < mx:  # プレイヤーiの得点が最高得点を超えるまで
        if B[j][1] not in answered[i]:  # 問題jをプレイヤーiが答えていなければ
            p += B[j][0]  # 問題jの得点を追加
            cnt += 1  # 追加で解いた問題数を加算
        j += 1
    print(cnt)  # 追加で解いた問題数を出力

"""
シミュレーション + 貪欲法
貪欲に高い点数の問題から解きたいけど、すでに解いた問題はもう回答できない点に注意する。
複数の配列やsetを駆使する。

けんちょんの解説
https://drken1215.hatenablog.com/entry/2023/10/12/013732

https://atcoder.jp/contests/abc323/tasks/abc323_c
https://chatgpt.com/g/g-p-688d3155796881919ed997146b54eec1-atcoder/c/6910f37d-3d54-8323-9ada-41cf26d9afeb
"""
