N, M, H, K = map(int, input().split())
S = input()
I = set()
for _ in range(M):
    x, y = map(int, input().split())
    I.add((x, y))
# print(I)

x, y = 0, 0
for s in S:
    if s == 'R':
        dx = 1
        dy = 0
    elif s == 'L':
        dx = -1
        dy = 0
    elif s == 'U':
        dx = 0
        dy = 1
    else:  # s == 'D':
        dx = 0
        dy = -1
    x, y = x + dx, y + dy

    H -= 1
    if H < 0:
        print("No")
        exit()

    if (x, y) in I and H < K:  # アイテムが有り、かつ、HがK未満の時
        H = K
        I.remove((x, y))  # アイテム消費

print("Yes")

"""
シミュレーション系
一度使ったアイテムは消費して無くなってしまうことを忘れないように。

けんちょんの解説
https://drken1215.hatenablog.com/entry/2023/05/29/020800

https://atcoder.jp/contests/abc303/tasks/abc303_c
https://chatgpt.com/c/692031ae-0698-8323-95af-fccdb651efb0
"""
