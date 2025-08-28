N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

L = max(A)
R = min(B)
print(max(0, R - L + 1))
