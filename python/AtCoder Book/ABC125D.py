N = int(input())
A = list(map(int, input().split()))

num_minus = sum(v < 0 for v in A)

sum_abs = sum(map(abs, A))
min_abs = min(map(abs, A))

print(sum_abs if num_minus % 2 == 0 else sum_abs - min_abs * 2)
