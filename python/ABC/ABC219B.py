S1 = input()
S2 = input()
S3 = input()
T = input()

arr = [None, S1, S2, S3]
print(*[arr[int(t)] for t in T], sep='')
