N = input()

SN = sum(map(int, N))
N = int(N)
print("Yes" if N % SN == 0 else "No")
