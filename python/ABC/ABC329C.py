from collections import defaultdict


N = int(input())
S = input()


# 各文字ごとの最長連続長を記録
len_list = defaultdict(int)

# ランレングス圧縮
i = 0
while i < N:
    c = S[i]
    j = i
    while j < N and S[j] == c:
        j += 1
    # 区間 [i, j) が文字 c の連続部分
    len_list[c] = max(len_list[c], j - i)
    i = j

# 各文字の最長長さを合計
res = sum(v for v in len_list.values())
print(res)

"""
ランレングス圧縮
けんちょん
https://drken1215.hatenablog.com/entry/2023/11/21/032500
ランレングス圧縮の典型題！

https://atcoder.jp/contests/abc329/tasks/abc329_c
"""
