S = input()
T = input()


def is_match_when_swap(swap, answer):
    swap = list(swap)
    answer = list(answer)

    if swap == answer:
        return True

    for i in range(len(swap) - 1):
        swaped = swap.copy()
        swaped[i], swaped[i + 1] = swaped[i + 1], swaped[i]

        # print(swaped)

        if swaped == answer:
            return True

    return False


print("Yes" if is_match_when_swap(S, T) else "No")
