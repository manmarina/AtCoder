N = int(input())
S = input()


def shift_ch(ch, N):
    base = ord('A')
    num = (ord(ch) - base + N) % 26
    return chr(num + base)


ans = []
for ch in S:
    ans.append(shift_ch(ch, N))

print(*ans, sep='')
