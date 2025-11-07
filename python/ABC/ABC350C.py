N = int(input())
A = list(map(int, input().split()))
A = [x - 1 for x in A]  # 0-indexed にする 位置 -> 値
print("A:", A)

# where[i] = 値 i が現在どの位置にあるか
where = [0] * N  # 値 -> 位置
for i in range(N):
    where[A[i]] = i
print("where:", where)

res = []

# 左から順に、位置 i に値 i を持ってくる
for i in range(N - 1):  # N-1回でソート完了するため
    if A[i] == i:
        continue  # すでに正しい位置ならスキップ

    j = where[i]  # 値 i のある位置を探す

    # A[i] と A[j] を入れ替える
    where[A[i]], where[A[j]] = where[A[j]], where[A[i]]
    A[i], A[j] = A[j], A[i]

    res.append((i + 1, j + 1))  # 出力は1-indexed

# 出力
print(len(res))
for i, j in res:
    print(i, j)

"""
計算量を削減したシミュレーション + 逆順列
逆順列で、どこにその要素があるのかを管理する。
「どこにその要素があるのかを管理するテク」はより高難易度の問題では頻出する！！

けんちょん
https://drken1215.hatenablog.com/entry/2024/04/22/130300

https://atcoder.jp/contests/abc350/tasks/abc350_c
https://chatgpt.com/g/g-p-688d3155796881919ed997146b54eec1-atcoder/c/690e028e-675c-8323-b532-e903f191720e
"""
