P = list(map(int, input().split()))


def convert_to_string(list):
    string = []
    for num in list:
        string.append(chr(num + ord('a') - 1))
    return ''.join(string)


print(convert_to_string(P))
