N = int(input())
S = input()

visited = set()
visited.add((0, 0))
x, y = (0, 0)


def visit(t):
    if t in visited:
        print("Yes")
        exit()
    visited.add(t)
    # print(visited)


for s in S:
    if s == 'R':
        x += 1
        visit((x, y))
    elif s == 'L':
        x -= 1
        visit((x, y))
    elif s == 'U':
        y += 1
        visit((x, y))
    else:  # s == 'D':
        y -= 1
        visit((x, y))
else:
    print("No")

"""
基本実装問題

けんちょん
https://drken1215.hatenablog.com/entry/2024/11/08/015741
高橋君が同じ座標にいたことがあるかどうかを判定する問題。

https://atcoder.jp/contests/abc291/tasks/abc291_c
"""
