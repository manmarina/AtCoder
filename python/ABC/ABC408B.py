N = int(input())
A = list(map(int, input().split()))

vals = sorted(set(A))        # 重複除去 → 昇順
print(len(vals))
print(*vals)
