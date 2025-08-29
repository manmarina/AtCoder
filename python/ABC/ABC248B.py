A, B, K = map(int, input().split())

count = 0
slime = A
while slime < B:
    slime *= K
    count += 1

# print(slime)

print(count)
