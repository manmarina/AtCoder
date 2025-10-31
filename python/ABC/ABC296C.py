N, X = map(int, input().split())
A = set(map(int, input().split()))

for a in A:
    if a - X in A:
        print("Yes")
        exit()

print("No")

"""
計算量を削減したシミュレーション

Ai-Aj=Xを、Ai-Xの有無に言い換える。
setを活用して、Ai-Xの有無をO(1)で答える。

けんちょんの解説
https://drken1215.hatenablog.com/entry/2025/02/08/030659


https://atcoder.jp/contests/abc296/tasks/abc296_c
"""
