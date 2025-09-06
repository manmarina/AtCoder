N, D = map(int, input().split())
S = input()

sl = [*S]
# print(sl)

i = len(sl) - 1
while D:
    if sl[i] == '@':
        sl[i] = '.'
        D -= 1
    i -= 1
print(*sl, sep='')
