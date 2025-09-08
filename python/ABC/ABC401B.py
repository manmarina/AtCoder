N = int(input())
S = [input() for _ in range(N)]

count = 0
islogin = False
for s in S:
    if s == "private" and not islogin:
        count += 1
    elif s == "login":
        islogin = True
    elif s == "logout":
        islogin = False
print(count)
