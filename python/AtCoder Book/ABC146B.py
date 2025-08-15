N = int(input())
S = input()


def shift_char(string, shift):
    shifted = []
    for s in string:
        shifted.append(chr((ord(s) - ord('A') + shift) % 26 + ord('A')))
    return (''.join(shifted))


print(shift_char(S, N))
