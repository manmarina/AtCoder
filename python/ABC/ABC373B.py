S = input().strip()           # 長さ26、A..Zが一度ずつ

pos = [0] * 26
for i, ch in enumerate(S):
    pos[ord(ch) - 65] = i     # 'A' のASCIIは 65

ans = 0
for x in range(25):           # A→B, ..., Y→Z の25回
    ans += abs(pos[x + 1] - pos[x])
print(ans)
