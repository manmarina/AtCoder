N, K = map(int, input().split())
l = list(map(int, input().split()))

l.sort(reverse=True)
length = 0
for i in range(K):
    length += l[i]
print(length)
