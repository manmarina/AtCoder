S, T = input().split()

ans = []
for w in range(1, len(S)):
    for c in range(w):  # 0-index
        temp = ""
        for k in range(c, len(S), w):
            temp += S[k]
        ans.append(temp)
# print(ans)
print("Yes" if T in ans else "No")

"""
問題文がややこしいが、次のように解釈できる。

0-indexed で考える。

整数 0≤c<w≤|S|
 であって、文字列 S
 の添字 (0 始まり) が w
 で割って c
 余る部分の文字を連結したときに、T
 になるものが存在するかを判定せよ。
"""
