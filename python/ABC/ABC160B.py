X = int(input())

happy = X // 500 * 1000
happy += (X % 500) // 5 * 5
print(happy)
