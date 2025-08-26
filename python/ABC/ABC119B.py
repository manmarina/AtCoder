N = int(input())
xu = [list(input().split()) for i in range(N)]

# print(xu)

yen = []
for num, unit in xu:
    if unit == "BTC":
        yen.append(float(num) * 380000)
    else:
        yen.append(int(num))

print(sum(yen))
