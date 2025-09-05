N = int(input())
SC = [input().split() for _ in range(N)]
# print(SC)

users = [(s, int(c)) for s, c in SC]
users.sort(key=lambda x: x[0])
# print(users)

total = sum(v for _, v in users)
# print(total)
print(users[total % N][0])
