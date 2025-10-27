from collections import defaultdict

N, K = map(int, input().split())
C = list(map(int, input().split()))
# print(C)

mp = defaultdict(int)

# 最初の K 個をカウント
for i in range(K):
    mp[C[i]] += 1
# print(mp)

ans = len(mp)  # この区間の種類の数

for i in range(1, N - K + 1):  # 先頭の次から最後まで
    mp[C[i + K - 1]] += 1  # 今回区間の最後の文字のカウントを増やす
    mp[C[i - 1]] -= 1  # 前回区間の最初の文字のカウントを減らす
    if mp[C[i - 1]] == 0:  # 減らした結果0になったらキーを削除する（種類を減らすため）
        del mp[C[i - 1]]

    ans = max(ans, len(mp))  # この区間の種類の数のほうが多ければ更新

print(ans)

"""
計算量を削減したシミュレーション
解説
けんちょんも同じ解法
数列の幅 Kの区間をすべて調べるには、このようにやるのが定石。

https://atcoder.jp/contests/abc210/tasks/abc210_c
https://drken1215.hatenablog.com/entry/2024/11/09/144755
"""
