M = int(input())

ans = []
i = 0
while M > 0:
    cnt = M % 3
    ans.extend([i] * cnt)
    M //= 3
    i += 1

print(len(ans))
print(*ans)

"""
10進数で 123 を「1の位・10の位・100の位」に分けるときも、
123 % 10 = 3 が 1の位
123 // 10 = 12 にして繰り返す
とやっています。
これと同じことを 3進法 でやるだけです。
"""
