N, X = map(int, input().split())
m = [int(input()) for i in range(N)]

# print(m)
rest = X - sum(m)
count = len(m)
# print(rest)

count += rest // min(m)
print(count)
