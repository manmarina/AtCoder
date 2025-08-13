P = int(input())


def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


coins = [0]
for i in range(1, 10 + 1):
    coins.append(factorial(i))

# print(coins)

rest = P
count_total = 0
for coin in reversed(coins):
    count = 0
    while 0 < rest:
        if rest < coin:
            break
        rest -= coin
        count += 1
        count_total += 1
        # print(count_total, coin, rest)
        if count == 100:
            break
    else:
        break

print(count_total)
