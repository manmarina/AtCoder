N = int(input())
a = [0]
for i in range(N):
    a.append(int(input()))

# print(a)
visited = [False] * (N + 1)
cur = 1
count = 1
while 1:
    if visited[cur]:
        print(-1)
        break
    if a[cur] == 2:
        print(count)
        break
    visited[cur] = True
    cur = a[cur]
    count += 1
