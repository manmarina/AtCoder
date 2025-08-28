A, B, W = map(int, input().split())

Wg = 1000 * W


def ceil_div(x, y):  # x>0, y>0 で使用
    return (x + y - 1) // y


n_min = ceil_div(Wg, B)
n_max = Wg // A

if n_min <= n_max:
    print(n_min, n_max)
else:
    print("UNSATISFIABLE")
