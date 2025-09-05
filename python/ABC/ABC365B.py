N = int(input())
A = list(map(int, input().split()))

tagged = [(a, i) for i, a in enumerate(A, 1)]
tagged.sort(key=lambda x: -x[0])
# print(tagged)

tagged.pop(0)
# print(tagged)

print(tagged[0][1])
