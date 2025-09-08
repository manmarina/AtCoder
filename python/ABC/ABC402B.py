from collections import deque
import sys

it = iter(sys.stdin.read().strip().split())
Q = int(next(it))
q = deque()
out = []

for _ in range(Q):
    t = next(it)
    if t == '1':
        x = int(next(it))
        q.append(x)
    else:  # t == '2'
        out.append(str(q.popleft()))

print("\n".join(out))
