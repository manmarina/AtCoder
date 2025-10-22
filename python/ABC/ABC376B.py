def num_move(n, from_, to, ng):
    if from_ > to:  # l > tのときは
        from_, to = to, from_  # l < tとしてやっても問題ない（距離がわかればよいので）
    if from_ < ng < to:  # 反対の手が間にいるとき
        return n - (to - from_)  # n - 近い方
    else:
        return to - from_  # 近い方


n, q = map(int, input().split())
l, r = 1, 2
ans = 0

for _ in range(q):
    h, t = input().split()
    t = int(t)
    if h == 'L':
        ans += num_move(n, l, t, r)
        l = t
    else:
        ans += num_move(n, r, t, l)
        r = t

print(ans)

"""
場合分けを減らす
解説放送

l -> Tの移動を考えるとき
距離がわかればよいだけなので、
l > Tだとしても、入れ替えて考えても問題ない。
すると、
l < T の間に rが入るかどうかだけ考えればよくなる。
つまり、間にrが入らない方向の距離だけ足してやればよい。
"""
