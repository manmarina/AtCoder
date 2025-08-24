H, W = map(int, input().split())
a = []
for i in range(H):
    a.append(input())
for i in range(H):
    a[i] = '#' + a[i] + '#'

str = '#' * (W + 2)
a.insert(0, str)
a.append(str)
print(*a, sep='\n')
