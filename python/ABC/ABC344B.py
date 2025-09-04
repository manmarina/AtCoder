ans = []
while 1:
    A = int(input())
    ans.append(A)
    if A == 0:
        break
print(*ans[::-1], sep='\n')
