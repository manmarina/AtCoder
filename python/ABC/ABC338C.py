N = int(input())
Q = list(map(int, input().split()))
A = list(map(int, input().split()))
B = list(map(int, input().split()))
INF = 10**18

ans = 0
for x in range(max(Q) + 1):
    y = INF  # 「B で何人分作れるか」の上限の最小値を求めたいので、最初は超大きい値から開始
    ok = True
    for i in range(N):
        if Q[i] < A[i] * x:  # 材料 i が、A を x 人分作るだけで足りない → この x は不可能
            ok = False
            break
        if B[i] > 0:
            # 材料 i は B も使う。B を何人分まで作れるかを計算
            y = min(y, (Q[i] - A[i] * x) // B[i])
            # ↑ 各材料 i が許す y の上限のうち、最小のものを維持している
    if ok:
        ans = max(ans, x + y)

print(ans)

"""
工夫して探索の通り数を減らす全探索
公式解説
Biの個数yは計算で求めることで探索の通り数を減らす。

x の候補：0 ～ max(Qi)（≦ 10^6）
各 x について、材料 i を全部見る：O(N)（N ≦ 10）
O(N x max(Qi)) ≤ 10 x 10^6 = 10^7
なので計算可能。

https://atcoder.jp/contests/abc338/tasks/abc338_c
https://chatgpt.com/g/g-p-688d3155796881919ed997146b54eec1-atcoder/c/692d542d-5e18-8322-a759-843bedccc296
"""
