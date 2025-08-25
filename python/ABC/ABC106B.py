N = int(input())

count = 0
for i in range(1, N + 1, 2):
    div = set()
    for j in range(1, int(i**0.5) + 1):
        if i % j == 0:
            div.add(j)
            div.add(i // j)
    # print(i, div, len(div))
    if len(div) == 8:
        count += 1
print(count)
