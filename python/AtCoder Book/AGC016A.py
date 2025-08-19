S = input().strip()

ans = float('inf')

for code in range(26):
    c = chr(ord('a') + code)
    if c not in S:
        continue  # この文字を目標にしても不可能

    # 「c ではない」連続区間の最大長を求める
    max_run = 0
    cur = 0
    for ch in S:
        if ch == c:
            max_run = max(max_run, cur)
            cur = 0
        else:
            cur += 1
    max_run = max(max_run, cur)  # 末尾が非cで終わる場合を反映

    ans = min(ans, max_run)

print(ans)
