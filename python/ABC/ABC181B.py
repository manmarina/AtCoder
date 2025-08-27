N = int(input())
AB = [list(map(int, input().split())) for _ in range(N)]

print(sum(sum(range(a, b + 1)) for a, b in AB))
