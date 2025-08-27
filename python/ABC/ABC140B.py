N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = [0] + list(map(int, input().split()))

sat = sum(B)
for i in range(1, len(A)):
    if A[i] == A[i - 1] + 1:
        sat += C[A[i - 1]]

print(sat)
