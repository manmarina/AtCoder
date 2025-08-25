A, B, C = map(int, input().split())
K = int(input())

mx = max(A, B, C)
print(mx * 2**K + (A + B + C - mx))
