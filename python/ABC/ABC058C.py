import sys

N = int(sys.stdin.readline())
S = [sys.stdin.readline().strip() for _ in range(N)]

# S[i] に含まれる各文字（a..z）の個数を数える
nums = [[0] * 26 for _ in range(N)]
for i in range(N):
    for ch in S[i]:
        nums[i][ord(ch) - ord('a')] += 1
print(nums)

# 各文字について、全文字列での最小出現回数をとって連結
res_parts = []
for i in range(26):
    mi = nums[0][i]
    for j in range(1, N):
        mi = min(mi, nums[j][i])
    res_parts.append(chr(ord('a') + i) * mi)

print(''.join(res_parts))

"""
バケット
けんちょん

文字列ごとの26文字のバケットをnumsに格納
numsの26文字を走査して、最小文字数個res_partsに格納する
"""
