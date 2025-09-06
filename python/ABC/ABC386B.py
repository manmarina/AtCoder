S = input().strip()
n = len(S)

i = 0
press = 0
while i < n:
    # i + 1 < n を先に書くことで、S[i + 1]のインデクスオーバーフローを防ぐ
    if S[i] == '0' and i + 1 < n and S[i + 1] == '0':
        press += 1  # use "00"
        i += 2
    else:
        press += 1  # use single digit
        i += 1
print(press)
