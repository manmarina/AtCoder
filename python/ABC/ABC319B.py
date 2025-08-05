N = int(input())

j = []
for i in range(1, N+1):
    if N % i == 0 and i <= 9:
        j.append(i)

for i in range(N + 1):
    for k in j:
        if i % (N/k) == 0:
            print(k, end='')
            break
    else:
        print('-', end='')
print()
