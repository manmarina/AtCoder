T = int(input())
A = []
for _ in range(T):
    _ = input()
    A.append(list(map(int, input().split())))

# print(A)

for a in A:
    print(sum(1 for i in a if i % 2 == 1))
