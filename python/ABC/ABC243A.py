ABC = [0, 0, 0]
V, ABC[0], ABC[1], ABC[2] = map(int, input().split())

while 1:
    for i in range(3):
        V -= ABC[i]
        if V < 0:
            if i == 0:
                print("F")
            elif i == 1:
                print("M")
            else:
                print("T")
            exit()
