A, B, C = map(int, input().split())

seen = [False] * B
x = 0  # 0 から A を足し込んでいくと (A*i) % B を順に辿れる
while not seen[x]:
    if x == C:
        print("YES")
        break
    seen[x] = True
    x = (x + A) % B
else:
    print("NO")
