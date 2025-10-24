from collections import defaultdict


Q = int(input())

bag = defaultdict(int)
for _ in range(Q):
    q = list(map(int, input().split()))
    if q[0] == 1:
        bag[q[1]] += 1
    elif q[0] == 2:
        bag[q[1]] -= 1
    else:  # q[0] == 3:
        print(sum(1 for v in bag.values() if v != 0))
# print(bag)

"""
TLE
"""
