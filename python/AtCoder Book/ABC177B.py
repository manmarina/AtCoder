S = input()
T = input()


def rewrite_times(whole, part):
    lw = len(whole)
    lp = len(part)
    min = 10 ** 9
    for i in range(lw - lp + 1):
        temp_whole = whole[i:lp + i]
        if temp_whole == part:
            return 0
        count = 0
        for j in range(lp):
            temp_whole = whole[i + j]
            temp_part = part[j]
            if temp_whole != temp_part:
                count += 1
        if count < min:
            min = count
    return min


print(rewrite_times(S, T))
