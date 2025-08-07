from datetime import time

A, B, C, D = map(int, input().split())

takahasshi = time(A, B)
aoki = time(C, D)
if takahasshi <= aoki:
    print("Takahashi")
else:
    print("Aoki")
