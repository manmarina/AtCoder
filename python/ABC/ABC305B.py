p, q = input().split()

# 英文字を数字に変換
p = ord(p) - ord('A')
q = ord(q) - ord('A')
if p > q:
    p, q = q, p
# print(p, q)

# スライス和を求めて表示
line = [3, 1, 4, 1, 5, 9]
print(sum(line[p:q]))

"""
スライス和を使った解法
累積和を使っても解ける
（別解を参照）
"""
