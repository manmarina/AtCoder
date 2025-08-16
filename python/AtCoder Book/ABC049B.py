H, W = map(int, input().split())
C = []
for i in range(H):
    C.append(input())


def print_2times_long(original):
    for row in original:
        print(row)
        print(row)


print_2times_long(C)
