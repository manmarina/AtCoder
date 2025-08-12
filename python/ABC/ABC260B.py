N, X, Y, Z = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# 合格者リスト
passed = []

# 数学の点数と受験番号のリスト
math = []
for i in range(N):
    math.append([A[i], -(i + 1)])
math.sort(reverse=True)

for i in range(X):
    passed.append(-math[i][1])
# print(passed)

# 英語の点数と受験番号のリスト
english = []
for i in range(N):
    if i + 1 not in passed:
        english.append([B[i], -(i + 1)])
english.sort(reverse=True)

for i in range(Y):
    passed.append(-english[i][1])
# print(passed)

# 数学と英語の合計点数と受験番号のリスト
both = []
for i in range(N):
    if i + 1 not in passed:
        both.append([A[i] + B[i], -(i + 1)])
both.sort(reverse=True)

for i in range(Z):
    passed.append(-both[i][1])
# print(passed)

# 合格者の出力
passed.sort()
for i in passed:
    print(i)
