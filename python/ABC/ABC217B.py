S = set(input() for _ in range(3))

ok = {'ABC', 'ARC', 'AGC', 'AHC'}

# print(ok)
# print(S)

print(*(ok - S))
