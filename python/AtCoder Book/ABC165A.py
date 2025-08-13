K = int(input())
A, B = map(int, input().split())

start = A // K
end = B // K + 1
for i in range(start, end):
    if A <= i * K <= B:
        print("OK")
        break
else:
    print("NG")
