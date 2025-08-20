perm = []
count = 0
for i in range(8):
    for j in range(8):
        for k in range(8):
            for l in range(8):
                for m in range(8):
                    for n in range(8):
                        for o in range(8):
                            for p in range(8):
                                count += 1
                                temp = [i, j, k, l, m, n, o, p]
                                if len(temp) == len(set(temp)):
                                    perm.append(temp)

print(count)
print(len(perm))
