import sys
N, M, K = map(int, input().split())

A = []
R = []
for _ in range(M):
    temp = list(input().split())
    keys = [int(num) - 1 for num in temp[1:-1]]
    A.append(keys)
    R.append(temp[-1])  # 'o' or 'x'
print(A)
print(R)

res = 0
# 鍵の ON/OFF を bit で全探索（0〜2^N-1）
for bit in range(1 << N):
    ok = True
    for i in range(M):
        num = 0
        for j in A[i]:
            if bit & (1 << j):
                num += 1  # 正しい鍵の本数をカウント
        # C++ の条件と同じ
        if num < K and R[i] == 'o':  # 正しい鍵の本数が足りないのに'o'の時
            ok = False
        if num >= K and R[i] == 'x':  # 正しい鍵の本数が十分なのに'x'の時
            ok = False
    if ok:
        res += 1

print(res)

"""
ビット全探索（bit全探索）
けんちょん
https://drken1215.hatenablog.com/entry/2024/06/08/085219
各鍵が本物かダミーかの組合せは全部で 2N通りある。ここで、N≤15という制約を見よう。
これはもう、「組合せを全部試してみよ」と言っているようなものだ。
計算量は O(2^N M)となる。

https://atcoder.jp/contests/abc356/tasks/abc356_c
https://chatgpt.com/g/g-p-688d3155796881919ed997146b54eec1-atcoder/c/69314710-3d54-8320-a0ce-783375f7b2d8
"""
