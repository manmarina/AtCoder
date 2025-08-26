N = int(input())
T, A = map(int, input().split())
H = list(map(int, input().split()))

# print(H)

temp = []
for hight in H:
    t = T - hight * 0.006
    temp.append(abs(t - A))

# print(temp)
print(temp.index(min(temp)) + 1)
