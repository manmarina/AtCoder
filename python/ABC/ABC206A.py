N = int(input())

price = int(N * 1.08)
regular_price = 206

if price == regular_price:
    print("so-so")
elif price < regular_price:
    print("Yay!")
else:
    print(":(")
