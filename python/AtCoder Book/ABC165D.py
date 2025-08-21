A, B, N = map(int, input().split())


def fx(A, B, x):
    return A * x // B - A * (x // B)


# # 周期性を発見
# for i in range(1, N + 1):
#     print(f"fx({i}) = {fx(A, B, i)}",)


if B <= N:
    print(fx(A, B, B - 1))
else:
    print(fx(A, B, N))
