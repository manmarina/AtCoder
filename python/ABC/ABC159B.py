S = input()


def is_palindrome(S):
    return S == S[::-1]


def is_strong(S):
    if not is_palindrome(S):
        return False

    cen = len(S) // 2
    L = S[:cen]
    # R = S[-cen:]

    # print(L, R)

    if not is_palindrome(L):
        return False

    # if not is_palindrome(R):
    #     return False

    return True


print("Yes" if is_strong(S) else "No")
