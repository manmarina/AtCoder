import sys

input = sys.stdin.buffer.readline
T = int(input())

out = []
for _ in range(T):
    a, b, c = map(int, input().split())
    total = a + b + c
    out.append(str(min(a, c, total // 3)))
print("\n".join(out))


"""
bが最小で、a==cの時
101 -> 0
202 -> 1
303 -> 2
404 -> 2
505 -> 3
606 -> 4
707 -> 4
808 -> 5
909 -> 6
以上正しく動作している。
自分のコードではこの通りの回答が得られなかった。
"""
