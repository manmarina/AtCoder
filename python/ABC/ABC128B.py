N = int(input())
book = []
for i in range(1, N + 1):
    k, v = input().split()
    book.append((k, int(v), i))
# print(book)

book.sort(key=lambda x: (x[0], -x[1]))
for _, _, idx in book:
    print(idx)
