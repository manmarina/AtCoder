N, K = map(int, input().split())
D = set(input().split())
x = N
while True:
    if all(ch not in D for ch in str(x)):
        print(x)
        break
    x += 1
