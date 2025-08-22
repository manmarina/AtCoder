N = int(input())
S = input()

cs = [0] * (N + 1)
for i, v in enumerate(S, 1):
    if v == 'I':
        temp = 1
    else:  # v == 'D'
        temp = -1
    cs[i] = cs[i - 1] + temp

# print(cs)
print(max(cs))
