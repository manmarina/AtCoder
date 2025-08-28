N = int(input())
ST = [input() for _ in range(N)]

# print(ST)
# print(set(ST))
print("Yes" if len(ST) != len(set(ST)) else "No")
