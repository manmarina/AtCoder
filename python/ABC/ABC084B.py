A, B = map(int, input().split())
S = input()


def is_postalcode(S):
    if S[A] != '-':
        return False
    if not S[:A].isdigit():
        return False
    if not S[-B:].isdigit():
        return False
    return True


print("Yes" if is_postalcode(S) else "No")
