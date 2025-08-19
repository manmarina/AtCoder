N = int(input())
S = input()

# jが変わったらiをslimeに格納
slime = []
i = 0
while i < N:
    j = i + 1
    while j < N and S[j] == S[i]:
        j += 1
    slime.append(S[i])
    i = j

# 答えを表示
print(len(slime))
