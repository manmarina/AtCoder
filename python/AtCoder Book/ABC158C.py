A, B = map(int, input().split())

for i in range(1001):
    eight = i * 8 // 100
    ten = i * 10 // 100
    if eight == A and ten == B:
        print(i)
        break
else:
    print(-1)
