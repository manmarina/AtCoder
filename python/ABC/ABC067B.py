N, K = map(int, input().split())
l = list(map(int, input().split()))

l.sort(reverse=True)
print(sum(l[i] for i in range(K)))
