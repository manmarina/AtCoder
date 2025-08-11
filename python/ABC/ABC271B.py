N, Q = map(int, input().split())

a = []
for i in range(N):
    a.append(list(map(int, input().split())))

s = []
for i in range(Q):
    s.append(list(map(int, input().split())))

for i in range(len(s)):
    print(a[s[i][0] - 1][s[i][1]])
