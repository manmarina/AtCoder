N = int(input())
S = input()

cs_W, cs_E = [0], [0]  # Wの数、Eの数の累積和配列を作成
for i in range(N):
    if S[i] == 'W':
        cs_W.append(cs_W[i] + 1)
        cs_E.append(cs_E[i])
    else:
        cs_W.append(cs_W[i])
        cs_E.append(cs_E[i] + 1)
# print("cs_W:", cs_W)
# print("cs_E:", cs_E)

ans = 10**6
for i in range(N):
    num_W = 0
    if i > 0:  # iが1以上の時
        num_W = cs_W[i - 1]  # iの左側のWの数

    num_E = 0
    if i < N - 1:  # iがN-1未満の時
        num_E = cs_E[-1] - cs_E[i]  # iの右側のEの数

    ans = min(ans, num_W + num_E)  # Wの数、Eの数の合計が最小なら更新

print(ans)

"""
累積和
累積和の典型問題

けんちょん
https://drken1215.hatenablog.com/entry/2018/05/30/233311

https://atcoder.jp/contests/abc098/tasks/arc098_a
"""
