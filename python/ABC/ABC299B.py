N, T = map(int, input().split())
C = list(map(int, input().split()))
R = list(map(int, input().split()))

# まず切り札 T があるか確認
has_trump = any(ci == T for ci in C)

# 探すべき色
target = T if has_trump else C[0]

best_rank = -1
best_idx = -1  # 0-basedで持って最後に+1

for i in range(N):
    if C[i] == target and R[i] > best_rank:
        best_rank = R[i]
        best_idx = i

print(best_idx + 1)
