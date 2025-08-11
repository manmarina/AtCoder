N = int(input())
S = input()

for i in range(N - 1):
    count = 0
    for j in range(i + 1, N):
        if S[j - i - 1] != S[j]:
            count += 1
        else:
            print(count)
            break
    else:
        print(count)
