A = tuple(map(int, input().split()))
B = tuple(map(int, input().split()))
C = tuple(map(int, input().split()))


def dot(ax, ay, bx, by):  # 内積を計算
    return ax * bx + ay * by


def is_right(A, B, C):
    # Aを頂点
    if dot(B[0] - A[0], B[1] - A[1], C[0] - A[0],
           C[1] - A[1]) == 0:  # ベクトルAB * ベクトルAC
        return True
    # Bを頂点
    if dot(A[0] - B[0], A[1] - B[1], C[0] - B[0],
           C[1] - B[1]) == 0:  # ベクトルBA * ベクトルBC
        return True
    # Cを頂点
    if dot(A[0] - C[0], A[1] - C[1], B[0] - C[0],
           B[1] - C[1]) == 0:  # ベクトルCA * ベクトルCB
        return True
    return False


print("Yes" if is_right(A, B, C) else "No")
