N, K = map(int, input().split())
C = list(map(int, input().split()))
# print(C)

max_ = 0
for i in range(N - K + 1):
    set_ = set(C[i:i + K])
    max_ = max(max_, len(set_))
print(max_)

"""
TLE
"""
