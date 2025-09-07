import sys

it = iter(sys.stdin.read().rstrip().split())
Q = int(next(it))

stack = [0] * 100
out = []

for _ in range(Q):
    c = next(it)
    if c == '1':
        x = int(next(it))
        stack.append(x)
    else:  # c == '2'
        out.append(str(stack.pop()))

print("\n".join(out))
