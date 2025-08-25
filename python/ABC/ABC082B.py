s = input()
t = input()

s = sorted(s)
t = sorted(t, reverse=True)

# print(s, t)
if s < t:
    print("Yes")
else:
    print("No")
