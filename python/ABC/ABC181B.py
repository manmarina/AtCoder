N = int(input())
AB = [list(map(int, input().split())) for _ in range(N)]

ans = 0
for a, b in AB:
    sum = (a + b) * (b - a + 1) // 2  # 等差数列の和の公式
    ans += sum
print(ans)
