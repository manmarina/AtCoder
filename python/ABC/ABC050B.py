N = int(input())
T = list(map(int, input().split()))
M = int(input())
PX = [list(map(int, input().split())) for i in range(M)]

# print(T)
# print(PX)

total = sum(T)
for px in PX:
    print(total - T[px[0] - 1] + px[1])
