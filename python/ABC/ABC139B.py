A, B = map(int, input().split())

add = A - 1
if (B - 1) % add == 0:
    print((B - 1) // add)
else:
    print((B - 1) // add + 1)
