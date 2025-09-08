T = input()
U = input()

lt = len(T)
lu = len(U)

for i in range(lt - lu + 1):
    for j in range(lu):
        t = T[i + j]
        u = U[j]
        if t != '?' and t != u:
            break
    else:
        print("Yes")
        exit()
else:
    print("No")
