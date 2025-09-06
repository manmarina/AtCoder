S = input()

# 第一条件
if len(S) % 2:
    print("No")
    exit()

# 第二条件
for i in range(1, len(S) // 2 + 1):  # ややこしい問題文のとおりに条件を記述
    if S[2 * i - 1 - 1] != S[2 * i - 1]:
        print("No")
        exit()

# 第三条件
ss = set(S)
if len(S) != len(ss) * 2:
    print("No")
    exit()

print("Yes")
