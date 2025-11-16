N, X, Y = map(int, input().split())
A = list(map(int, input().split()))

# 飴を配る個数が最も多い子に、すべてXを配っても総重量以上になってしまうときは実現不能。
if min(A) * Y < max(A) * X:
    print(-1)
    exit()

A.sort()
# print(A)

total = A[0] * Y  # 飴を配る個数が最も少ない子に、すべてYを配ることとして総重量を決める。
diff = Y - X
ans = A[0]
# print(total)
for i in range(1, N):  # 配る個数が少ない子から順に考える
    total_cur = A[i] * Y  # すべてYで配った時の重量
    diff_cur = total_cur - total  # すべてYで配った時の重量 - 総重量
    if diff_cur % diff != 0:  # すべてYで配った時の重量と、総重量の差が、Y-Xの倍数になっていないときも実現不能。
        print(-1)
        exit()
    else:
        ans += A[i] - diff_cur // diff  # Yを配った個数を加算する
print(ans)

"""
計算量を削減したシミュレーション + 貪欲法
飴を配る個数が最も少ない子に、すべてYを配ることとして総重量を決める。
飴を配る個数が最も多い子に、すべてXを配っても総重量以上になってしまうときは実現不能。
すべてYで配った時の重量と、総重量の差が、Y-Xの倍数になっていないときも実現不能。

https://atcoder.jp/contests/abc432/tasks/abc432_c
"""
