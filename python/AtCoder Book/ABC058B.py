O = input()
E = input()


def decode(odd, even):
    string = []
    for i in range(len(odd)):
        string.append(odd[i])
        if i < len(even):
            string.append(even[i])
    return ''.join(string)


print(decode(O, E))
