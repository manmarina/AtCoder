A, B, W = map(int, input().split())


def calc_min(B, W):
    if W * 1000 % B == 0:
        return W * 1000 // B
    else:
        return W * 1000 // B + 1


def calc_max(A, W):
    return W * 1000 // A


# 取りうる個数の最小値と最大値を計算
mn = calc_min(B, W)
mx = calc_max(A, W)

if mn > mx:
    print("UNSATISFIABLE")
else:
    print(mn, mx)
