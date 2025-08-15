A, B = map(int, input().split())
S = input()


def is_postalcode(string):
    if len(string) != A + 1 + B:
        return False
    if not string[:A].isdigit():
        return False
    if not string[-B:].isdigit():
        return False
    if string[A] != '-':
        return False
    return True


print("Yes" if is_postalcode(S) else "No")
