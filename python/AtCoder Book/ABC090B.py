A, B = map(int, input().split())

palindrome = []
for i in range(A, B + 1):
    string = str(i)
    k = len(string)
    for j in range(k // 2 + 1):
        if string[j] != string[k - 1 - j]:
            break
    else:
        palindrome.append(i)

print(len(palindrome))
