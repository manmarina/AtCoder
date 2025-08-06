S = input()

count = 0
for i in S:
    if i == 'v':
        count += 1
    else:
        count += 2

print(count)
