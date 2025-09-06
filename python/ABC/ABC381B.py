from collections import Counter
S = input().strip()
n = len(S)

# 1) 長さが偶数
if n % 2 == 1:
    print("No")
    exit()

# 2) 各ペアが同じ文字
for i in range(0, n, 2):
    if S[i] != S[i + 1]:
        print("No")
        exit()

# 3) 文字出現回数が0または2（Counter版）
cnt = Counter(S)
if all(v == 2 for v in cnt.values()):
    print("Yes")
else:
    print("No")
