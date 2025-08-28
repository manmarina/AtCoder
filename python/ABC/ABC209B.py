N, X = map(int, input().split())
A = list(map(int, input().split()))

total = sum(A) - (N // 2)   # 偶数番目の個数だけ1円引き
print("Yes" if total <= X else "No")
