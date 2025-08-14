N, X = map(int, input().split())

m = []
for i in range(N):
    m.append(int(input()))

count = len(m)
rest = X - sum(m)
minimum = min(m)
count += rest // minimum
print(count)
