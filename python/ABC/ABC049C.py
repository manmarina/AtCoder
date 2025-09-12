S = input()
T = ["dreamer", "dream", "eraser", "erase"]

while S:
    for word in T:
        if S.endswith(word):
            S = S[:-len(word)]
            break
    else:
        print("NO")
        exit()

print("YES")
