N, K = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(N)]
AB.sort()
# print(AB)

pre = 0  # 前の友達の街（もしくはスタート）
for i in range(N):
    # 次の友達の街にたどり着けないとき
    if K < AB[i][0] - pre:
        print(pre + K)  # たどり着ける街を表示
        exit()

    # 次の友達の街にたどり着けた時
    K = K - (AB[i][0] - pre) + AB[i][1]  # Kの残高を求める
    pre = AB[i][0]  # 前の友達の街を更新

    # 最後の友達の街の時
    if i == N - 1:
        print(K + AB[i][0])  # たどり着ける街を表示
        exit()

"""
場合分け系
次の友達の街にたどり着けないとき、次の友達の街にたどり着けた時、最後の友達の街の時にわけて考える

https://atcoder.jp/contests/abc203/tasks/abc203_c
"""
