from collections import Counter

N = int(input())
S = [input() for _ in range(N)]

# print(S)
print(Counter(S).most_common(1)[0][0])
