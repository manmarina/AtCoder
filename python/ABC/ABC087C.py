N = int(input())
A = [list(map(int, input().split())) for _ in range(2)]
# print(A)

ans = []
for i in range(N):  # 下へ降りる位置を決める
    score = 0
    for j in range(i + 1):  # 上の行のアメの個数を加算
        score += A[0][j]
    for k in range(i, N):  # 下の行のアメの個数を加算
        score += A[1][k]
    ans.append(score)
# print(ans)
print(max(ans))

"""
全探索
単純な全探索で解ける！累積和で高速化したり DP したりしても OK

https://atcoder.jp/contests/abc087/tasks/arc090_a
https://drken1215.hatenablog.com/entry/2022/12/08/165015
"""
