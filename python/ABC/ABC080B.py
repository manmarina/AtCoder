N = input()

num = sum(map(int, N))
if int(N) % num == 0:
    print("Yes")
else:
    print("No")
