X = int(input())


def max_exponential(target):
    max = 1
    for i in range(2, target + 1):
        pow = i * i
        while pow <= target:
            if pow > max:
                max = pow
            pow *= i
    return max


print(max_exponential(X))
