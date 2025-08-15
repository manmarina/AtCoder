a, b = input().split()


def younger_string(a, b):
    string_a = a * int(b)
    string_b = b * int(a)

    return string_a if string_a < string_b else string_b


print(younger_string(a, b))
