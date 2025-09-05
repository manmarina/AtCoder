N, Q = map(int, input().split())
T = list(map(int, input().split()))

odd = set()
for t in T:
    if t in odd:
        odd.remove(t)
    else:
        odd.add(t)

# print(odd)
print(N - len(odd))
