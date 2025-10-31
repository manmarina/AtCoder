N = int(input())
A = list(map(int, input().split()))

# 0-index にする
A = [x - 1 for x in A]  # 生徒番号 -> 投稿した順
print(A)

B = [0] * N  # 空の配列を作成しておくのがポイント
for i in range(N):
    # B[インデックスを値に] = 値をインデックスに
    B[A[i]] = i  # 逆順列に変換 登校した順 -> 生徒番号
print(B)

# 出力時は 1-index に戻す
print(*[x + 1 for x in B])

"""
逆順列
いわゆる逆順列を求める問題。

けんちょんの解説
https://drken1215.hatenablog.com/entry/2019/10/03/003600

https://atcoder.jp/contests/abc142/tasks/abc142_c/editorial
https://chatgpt.com/g/g-p-688d3155796881919ed997146b54eec1-atcoder/c/69041a9a-107c-8324-ae63-931b7f29e2fd
"""
