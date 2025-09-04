N = int(input())

lowbit = N & -N          # 2^k N&-Nは最下位ビットのみが立つ性質がある
print(lowbit.bit_length() - 1)  # 最下位ビットの長さ−1が末尾の0の長さ
