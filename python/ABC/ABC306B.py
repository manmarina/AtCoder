A = list(map(int, input().split()))
ans = 0
for i, a in enumerate(A):   # A[0] が 2^0、A[63] が 2^63
    if a:
        ans += 1 << i
print(ans)
