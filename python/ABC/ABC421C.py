N = int(input())
S = [*input()]

# print(S)
# print(ok)

count = 0
for i in range(N * 2 - 2):
    if S[i] == 'A':
        dist = 0
        for j in range(i + 1, N * 2):
            if S[j] == 'B':
                break
            dist += 1

        # print(dist)

        count += dist
        S[i + 1] = 'B'
        if dist != 0:
            S[i + dist + 1] = 'A'

    else:  # S[i] == 'B'
        dist = 0
        for j in range(i + 1, N * 2):
            if S[j] == 'A':
                break
            dist += 1

        # print(dist)

        count += dist
        S[i + 1] = 'A'
        if dist != 0:
            S[i + dist + 1] = 'B'

# print(S)
print(count)
