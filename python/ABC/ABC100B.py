D, N = map(int, input().split())

k = N if N % 100 != 0 else N + 1   # N==100 のときだけ 101 にずらす
print(k * (100 ** D))
