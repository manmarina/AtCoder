T = int(input())
H = []
test = []

for _ in range(T):
    n, h = map(int, input().split())
    H.append(h)
    temp = []
    for i in range(n):
        temp.append(list(map(int, input().split())))
    test.append(temp)
# print(H)
# print(test)

for i in range(T):
    mx, mn = H[i], H[i]
    # print(mx)
    t_pre = 0
    for j in range(len(test[i])):
        # print(test[i][j])

        t, l, u = test[i][j]
        dt = t - t_pre
        t_pre = t
        # print("dt:", dt)
        mx = mx + dt
        mn = max(mn - dt, 1)
        # print(max(l, mn) <= min(u, mx))
        # print("mx:", mx, "mn:", mn)

        if not (max(l, mn) <= min(u, mx)):
            print("No")
            break

        mx = min(u, mx)
        mn = max(l, mn)

        # print("mx:", mx, "mn:", mn)
        # print("--------")
    else:
        print("Yes")

    # print()

"""
クエリ処理
計算量は考えなくても解けるが、実装がややこしい。
入念にデバッグ出力してなんとかAC。

https://atcoder.jp/contests/abc434/tasks/abc434_c
"""
