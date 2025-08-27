S = input()

odd = set("RUD")
even = set("LUD")

for i in range(0, len(S), 2):
    if S[i] not in odd:
        print("No")
        exit()
    # print(S[i])

for i in range(1, len(S), 2):
    if S[i] not in even:
        print("No")
        exit()
    # print(S[i])

print("Yes")
