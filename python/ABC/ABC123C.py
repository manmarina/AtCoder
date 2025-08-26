from math import ceil

N = int(input())
A = int(input())
B = int(input())
C = int(input())
D = int(input())
E = int(input())

mn = min(A, B, C, D, E)
time = 4 + ceil(N / mn)
print(time)
