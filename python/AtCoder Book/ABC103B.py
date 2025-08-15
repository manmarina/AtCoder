S = input()
T = input()


def is_match_when_rotated(rotate, answer):
    rotated = list(rotate)
    answer = list(answer)
    for i in range(len(rotate)):
        rotated = list(rotated[-1]) + rotated[:-1]
        # print(rotated)
        if rotated == answer:
            return True
    return False


print("Yes" if is_match_when_rotated(S, T) else "No")
