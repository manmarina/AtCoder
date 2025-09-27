import sys

input = sys.stdin.readline
N, Q = map(int, input().split())
A = list(map(int, input().split()))

# 二重配列と累積和
# 区間の長さは 最大でも N（配列の全体）です。
# 配列を 2 回並べておけば、必ず 1 本の連続区間として取れる。
B = A + A
pref = [0] * (2 * N + 1)
for i, x in enumerate(B, 1):
    pref[i] = pref[i - 1] + x
# print(pref)

off = 0  # 先頭（0-index）が元配列のどこか
out = []
for _ in range(Q):
    t, *rest = map(int, input().split())
    if t == 1:
        c = rest[0]
        off = (off + c) % N  # Nで回転
    else:
        l, r = rest
        length = r - l + 1
        start = (off + (l - 1)) % N  # Nで回転
        s = pref[start + length] - pref[start]
        out.append(str(s))
print("\n".join(out))

"""
二重配列の累積和
チャッピー

回転は“配列を動かさずに”先頭位置のオフセットだけ持つ
累積和は “二重配列” に乗せる

https://atcoder.jp/contests/abc425/tasks/abc425_c
https://chatgpt.com/g/g-p-688d3155796881919ed997146b54eec1-atcoder/c/68d7e92f-bc70-8333-90e3-a9d04186068d
"""
