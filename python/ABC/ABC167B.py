A, B, C, K = map(int, input().split())

# 1を取れる枚数 - -1を取らされる枚数
print(min(A, K) - max(0, K - A - B))
