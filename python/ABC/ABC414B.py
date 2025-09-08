N = int(input())
cl = [list(input().split()) for _ in range(N)]

# 1) 合計長チェック（101を超えたら即終了）
total = 0
for _, l in cl:
    total += int(l)
    if total > 100:
        print("Too Long")
        raise SystemExit  # 以降は不要

# 2) 実際の復元（remain なし）
print("".join(c * int(l) for c, l in cl))
