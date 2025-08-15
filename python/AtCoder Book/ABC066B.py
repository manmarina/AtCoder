S = input()


def length_of_evenstring(string):
    cut = string
    while 1:
        cut = cut[:-2]
        if cut[:len(cut) // 2] == cut[len(cut) // 2:]:
            return len(cut)


print(length_of_evenstring(S))
