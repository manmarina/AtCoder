N = int(input())
S = input()

answer = 0
for i in range(1, N):
    front = set(S[:i])
    back = set(S[i:])

    # print(front, back)

    answer = max(len(front & back), answer)
print(answer)
