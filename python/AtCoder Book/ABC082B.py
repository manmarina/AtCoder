s = input()
t = input()


def is_able_younger(s, t):
    list_s = sorted(list(s))
    list_t = sorted(list(t), reverse=True)

    # print(list_s)
    # print(list_t)

    if list_s < list_t:
        return True
    else:
        return False


print("Yes" if is_able_younger(s, t) else "No")
