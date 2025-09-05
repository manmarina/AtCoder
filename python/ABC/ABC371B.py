N, M = map(int, input().split())
AB = [list(input().split()) for _ in range(M)]

has_taro = [False] * (N + 1)
for a, b in AB:
    a = int(a)
    if has_taro[a] == False and b == 'M':
        print("Yes")
        has_taro[a] = True
    else:
        print("No")
