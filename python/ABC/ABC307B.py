N = int(input())
S = [input() for _ in range(N)]
# print(S)

for i in range(N):
    for j in range(N):
        if i == j:
            continue
        word = S[i] + S[j]
        if word == word[::-1]:
            print("Yes")
            exit()
print("No")
