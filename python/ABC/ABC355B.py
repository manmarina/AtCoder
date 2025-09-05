N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

tagged = [(a, 'A') for a in A] + [(b, 'B') for b in B]
tagged.sort(key=lambda x: x[0])
# print(tagged)

for i in range(1, len(tagged)):
    if tagged[i - 1][1] == 'A' and tagged[i][1] == 'A':
        print("Yes")
        break
else:
    print("No")
