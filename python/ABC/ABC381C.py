N = int(input())
T = input()

ans = []
for i in range(N):
    # '/'でなければ次の文字へ
    if T[i] != '/':
        continue

    # '/'だったとき
    cnt = 1
    for j in range(1, N):
        if i - j < 0 or i + j > N - 1:  # 文字列の範囲外のときは次の文字へ
            break
        if T[i - j] != '1' or T[i + j] != '2':  # '/'の左が'1'、右が'2'でないときは次の文字へ
            break
        cnt += 2

    # cntをansに追加
    ans.append(cnt)

# print(ans)
print(max(ans) if ans else 0)  # ansが空の時の処理を書かないとRE

"""
文字列操作
解説
11/22文字列の最長の長さを探索する。

この操作では 1 回の繰り返しにつき最悪 O(N) の計算量が掛かるので
O(N^2) になってしまうと考える方もいるかもしれませんが、
実は計算量は O(N)で済みます

https://atcoder.jp/contests/abc381/tasks/abc381_c
https://chatgpt.com/g/g-p-688d3155796881919ed997146b54eec1-atcoder/c/68f9a79b-d150-8321-ae45-60f624ce5cd4
"""
