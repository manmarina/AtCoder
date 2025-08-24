O = input()
E = input()

# print(list(zip(O, E)))

ans = []
for o, e in zip(O, E):
    ans.append(o + e)
if len(O) > len(E):
    ans.append(O[-1])
print(*ans, sep='')
