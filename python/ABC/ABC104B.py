S = input()


def is_AC(S):
    if S[0] != 'A':
        return False
    if S[2:-1].count('C') != 1:
        return False

    # for i, s in enumerate(S):
    #     if i != 0 and i != S.index('C'):
    #         if not s.islower():
    #             return False

    for i in range(len(S)):
        if i != 0 and i != S.index('C'):
            if not S[i].islower():
                return False

    return True


print("AC" if is_AC(S) else "WA")
