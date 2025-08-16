N = int(input())
S = input()


def cut_string(cutter, string):
    X = string[:cutter]
    Y = string[cutter:]
    return X, Y


def count_and(X, Y):
    return len(set(X) & set(Y))


def cut_and_count(num, string):
    max = 0
    for i in range(1, num):
        X, Y = cut_string(i, string)
        # print(X, Y)
        count = count_and(X, Y)
        # print(count)
        if count > max:
            max = count
    return max


print(cut_and_count(N, S))
