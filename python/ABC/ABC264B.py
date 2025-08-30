R, C = map(int, input().split())

dst = max(abs(R - 8), abs(C - 8))

# print(dst)

if dst % 2 == 1:
    print("black")
else:
    print("white")
