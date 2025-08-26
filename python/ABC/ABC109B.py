N = int(input())
W = [input() for i in range(N)]

past = {W[0]}
for i in range(1, N):
    if W[i] in past:
        print("No")
        break
    if W[i][0] != W[i - 1][-1]:
        print("No")
        break
    past.add(W[i])
    # print(past)

else:
    print("Yes")
