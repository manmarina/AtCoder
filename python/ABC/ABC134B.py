N, D = map(int, input().split())

area = D * 2 + 1
person = N // area if N % area == 0 else N // area + 1
print(person)
