N, Q = map(int, input().split())
S = list(input())
ans = 0

# 初期状態のABCの数をカウント
for i in range(N - 2):
    if S[i] == "A" and S[i + 1] == "B" and S[i + 2] == "C":
        ans += 1
# クエリ処理
for _ in range(Q):
    x, c = input().split()
    x = int(x) - 1

    # 変更前にABCがあれば、その数をマイナスする
    for k in range(3):  # idxを左にずらしながら計3回検討
        idx = x - k
        if 0 <= idx and idx + 2 < N:
            if S[idx] == "A" and S[idx + 1] == "B" and S[idx + 2] == "C":
                ans -= 1

    # 変更後にABCがあれば、その数をプラスする
    S[x] = c
    for k in range(3):  # idxをずらしながら3回検討
        idx = x - k
        if 0 <= idx and idx + 2 < N:
            if S[idx] == "A" and S[idx + 1] == "B" and S[idx + 2] == "C":
                ans += 1
    print(ans)

"""
計算量を削減したクエリ
解説
https://atcoder.jp/contests/abc372/editorial/10972
けんちょん
https://drken1215.hatenablog.com/entry/2024/09/22/002009
文字の変更により、変更される部分文字列は3つしかない。
変更前の部分文字列3つと、変更後の部分文字列3つの変化だけもとめて増減すれば良い。

https://atcoder.jp/contests/abc372/tasks/abc372_c
"""
