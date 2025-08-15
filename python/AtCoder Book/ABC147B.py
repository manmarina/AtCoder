S = input()


def count_to_palindrome(string):
    count = 0
    n = len(string) // 2
    for i in range(n):
        if string[i] != string[len(string) - 1 - i]:
            count += 1
    return count


print(count_to_palindrome(S))
