N = int(input())
A = list(map(int, input().split()))

A.sort()
S = sum(A)

q, r = divmod(S, N)        # q = S // N, r = S % N

# 最終形 B を作る
B = [q + (i < r) for i in range(N)]
B.sort()

# 差の総和
res = 0
for a, b in zip(A, B):
    res += abs(a - b)

print(res // 2)

"""
法則を見つける系
配列の平均化（balancing array）に必要な最小の操作回数を求める。
操作の前後で配列の合計は変化しないことを利用する。

「考えたこと：最終形」
→ 合計 S は不変なので、最終形は「q が N-r 個、q+1 が r 個」しかない。

「小さいものに小さいものを割り当てる」
→ A と B をソートして、同じ位置同士を対応させるのが最適。

「A も B もソートして、その差の和を求めて、2 で割れば OK」
→ 差の和 = move_sum、1 回の操作で 2 減るから、回数 = move_sum / 2。

けんちょん
https://drken1215.hatenablog.com/entry/2023/08/06/003228

https://atcoder.jp/contests/abc313/tasks/abc313_c
https://chatgpt.com/g/g-p-688d3155796881919ed997146b54eec1-atcoder/c/692163bf-7cbc-8324-97ff-b0d65d453782
"""
