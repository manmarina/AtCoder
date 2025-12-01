H, W, N = map(int, input().split())
T = input()
S = []
for _ in range(H):
    S.append(input())

# print(S)

ans = 0
for i in range(H):
    for j in range(W):
        if S[i][j] == '.':
            y, x = i, j
            for t in T:
                if t == 'L':
                    x -= 1
                elif t == 'R':
                    x += 1
                elif t == 'U':
                    y -= 1
                else:  # t== 'D':
                    y += 1

                ok = (0 <= y <= H and 0 <= x <= W)
                if not ok or S[y][x] == '#':
                    break
            else:
                ans += 1
print(ans)

"""
カーソル系
基本に忠実でひねりのないカーソル系
全マスを走査して、スタート地点が'.'ならTの指示通り移動して'#'が1度でも出ればアウト
でなければカウントを増やす。

https://atcoder.jp/contests/abc341/tasks/abc341_c
"""
