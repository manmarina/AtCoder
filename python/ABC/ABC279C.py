h, w = map(int, input().split())
s = [input() for _ in range(h)]
t = [input() for _ in range(h)]

# A. 縦列を取り出して文字列化
Ts = [''.join(s[i][j] for i in range(h)) for j in range(w)]
Tt = [''.join(t[i][j] for i in range(h)) for j in range(w)]

# B. ソートして比較
Ts.sort()
Tt.sort()
# print(Ts)
# print(Tt)

if Ts == Tt:
    print("Yes")
else:
    print("No")

"""
計算量を削減したシミュレーション
行列を転覆してソートを容易にする。

https://atcoder.jp/contests/abc279/tasks/abc279_c
https://chatgpt.com/g/g-p-688d3155796881919ed997146b54eec1-atcoder/c/690c2f91-a5d0-8323-9803-735606e22a78
"""
