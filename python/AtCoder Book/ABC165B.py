X = int(input())

year = 0
balance = 100
while balance < X:
    year += 1
    balance = balance * 101 // 100  # 整数のまま1%増やす（切り捨て）

print(year)
