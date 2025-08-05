N ,M, P = map(int, input().split())

if M > N:
    count = 0
else:
    count = (N - M) // P + 1

print(count)
