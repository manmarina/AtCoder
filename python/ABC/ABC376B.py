N, Q = map(int, input().split())
HT = [list(input().split()) for _ in range(Q)]

L, R = 1, 2  # 初期位置


def cw(a, b):            # 時計回り距離
    return (b - a + N) % N


def in_cw_arc(a, b, x):
    """a→b の時計回り区間に x があるか（a除外, b含む）
       ※a==b のときは空区間（何も含まない）"""
    if a == b:
        return False
    if a < b:
        return a < x <= b
    else:
        return x > a or x <= b


ans = 0
for h, t in HT:
    t = int(t)
    if h == 'L':
        p, s = L, R
        d = cw(p, t)
        # s が CW 区間にいなければ CW、いれば CCW
        ans += d if not in_cw_arc(p, t, s) else (N - d)
        L = t
    else:
        p, s = R, L
        d = cw(p, t)
        ans += d if not in_cw_arc(p, t, s) else (N - d)
        R = t

print(ans)
