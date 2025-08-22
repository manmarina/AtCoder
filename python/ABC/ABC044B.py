w = input()

sw = set(w)
for i in sw:
    if w.count(i) % 2 == 1:
        print("No")
        break
else:
    print("Yes")
