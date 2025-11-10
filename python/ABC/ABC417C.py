from collections import defaultdict


N = int(input())
A = list(map(int, input().split()))
# print(A)

ans = 0
dd = defaultdict(int)  # A[i] + i -> A[i] + iの数
for i in range(N):
    dd[A[i] + i] += 1

for j in range(N):
    ans += dd[j - A[j]]  # A[i] + i と j - A[j] が一致した数を加算

print(ans)

"""
計算量を削減したシミュレーション
リトライ

公式+チャッピーの解説がわかりやすい。
「公式の解説です。 灰コーダーの私にもわかりやすくこの内容を教えて下さい。」以下を参照して下さい。

A[i] + A[j] = j - i を変形して、
A[i] + i = j - A[j] を得る。
つまり、A[i] + i と j - A[j] が一致していれば、その数の累計が答え。

まず、defaultdictを作成して、
A[i] + i の数をカウントする。
その後、defaultdictからj - A[j]の数を取り出してansに加算する。
ansが A[i] + i = j - A[j] を満たすものの数となる。

0-indexedでも、1-indexedでも答えは一致するので、0-indexedで作成しています。

https://atcoder.jp/contests/abc417/tasks/abc417_c
https://chatgpt.com/g/g-p-688d3155796881919ed997146b54eec1-atcoder/c/69008615-d0bc-8323-bcdf-e5cba57c16ad
"""
