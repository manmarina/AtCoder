N = int(input())
H = list(map(int, input().split()))

mx = 0
count = 0
for v in H:
    if v >= mx:
        mx = v
        count += 1
print(count)
