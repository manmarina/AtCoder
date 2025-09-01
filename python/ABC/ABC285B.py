N = int(input())
S = input()

for i in range(1, N):
    count = 0
    for j in range(5 - i + 1):
        if S[j] == S[j + i]:
            print(count)
            break
        count += 1
    else:
        print(count)
