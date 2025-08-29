A, B = input().split()

# print(A)
# print(B)

for a, b in zip(reversed(A), reversed(B)):
    if int(a) + int(b) > 9:
        print("Hard")
        break
else:
    print("Easy")
