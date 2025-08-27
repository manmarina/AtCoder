N = int(input())
A = list(map(int, input().split()))

L = 10**18

if 0 in A:
    print(0)
    exit()

prod = 1
for a in A:
    if prod > L // a:
        print(-1)
        exit()
    prod *= a

print(prod)
