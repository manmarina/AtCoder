N = int(input())
D = list(map(int, input().split()))

ans = 0
for i in range(1, N + 1):
    s = str(i)
    if len(set(s)) == 1:          # i がゾロ目月か？
        d = int(s[0])             # 使われている数字 d（1〜9）
        if d <= D[i - 1]:
            ans += 1              # j = d
        if 11 * d <= D[i - 1]:
            ans += 1              # j = 11d
print(ans)
