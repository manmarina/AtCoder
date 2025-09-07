N = int(input())
A = list(map(int, input().split()))

if N <= 2:
    print("Yes")
else:
    ok = all(A[i] * A[i + 2] == A[i + 1] * A[i + 1] for i in range(N - 2))
    print("Yes" if ok else "No")
