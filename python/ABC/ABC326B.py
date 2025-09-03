N = int(input())

for i in range(N, 919 + 1):
    t = str(i)
    a, b, c = int(t[0]), int(t[1]), int(t[2])
    if c == a * b:
        print(i)
        break
