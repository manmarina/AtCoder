T = int(input())
N = []
A = []

for i in range(T):
    N.append(int(input()))
    A.append(list(map(int, input().split())))

for i in range(T):
    print(len(list(filter(lambda n: n % 2 != 0, A[i]))))
