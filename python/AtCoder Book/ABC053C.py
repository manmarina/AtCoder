x = int(input())

mod = x % 11
count = x // 11 * 2

if 1 <= mod <= 5:
    count += 1
elif mod >= 6:
    count += 2

# print(mod)
print(count)
