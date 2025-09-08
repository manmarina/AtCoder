N = int(input())

logged = False
ans = 0
for _ in range(N):
    s = input().strip()
    if s == "login":
        logged = True
    elif s == "logout":
        logged = False
    elif s == "private":
        if not logged:
            ans += 1
print(ans)
