N, Q = map(int, input().split())
A = [(i + 1, 0) for i in range(N)][::-1]

for _ in range(Q):
    T, C = input().split()
    if T == "1":
        x, y = A[-1]
        if C == "U":
            y += 1
        if C == "D":
            y -= 1
        if C == "R":
            x += 1
        if C == "L":
            x -= 1
        A.append((x, y))
    else:
        print(*A[-int(C)])

"""
発想の転換系
一見dequeを使わないといけないと見せかけているが、pythonはdequeの添字アクセスが遅いので使えない。
通常の配列を逆順に考えて利用する。deque[i] は O(n)、list[i]はO(1)。
公式解説

https://atcoder.jp/contests/abc335/tasks/abc335_c
https://chatgpt.com/g/g-p-688d3155796881919ed997146b54eec1-atcoder/c/692ad576-1344-832c-9174-910efca6956f
"""
