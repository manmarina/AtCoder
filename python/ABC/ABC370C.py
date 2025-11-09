S = list(input())
T = list(input())

ans = []
ln = len(S)

# 左から変更
for i in range(ln):
    num_S = ord(S[i])
    num_T = ord(T[i])
    if num_S > num_T:  # 変更後文字コードが小さくなるなら変更する
        S[i] = T[i]
        ans.append(''.join(S))

# 右から変更
for i in reversed(range(ln)):
    if S[i] != T[i]:  # 変更後文字コードが大きくなる組み合わせを変更する
        S[i] = T[i]
        ans.append(''.join(S))

print(len(ans))
print(*ans, sep="\n")

"""
文字列操作
辞書順で最小になるように文字列を変更してゆく。
まず先頭から、文字コードが小さくなるなら変更してゆく。
その後、末尾から文字が大きくなる組み合わせを変更をしてゆく。

けんちょんの解説
https://drken1215.hatenablog.com/entry/2024/09/13/002646

https://atcoder.jp/contests/abc370/tasks/abc370_c
"""
