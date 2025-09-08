N = int(input())
A = list(map(int, input().split()))

A.sort(reverse=True)
print(A)

for i, a in enumerate(A, 1):
    if a <= i:
        print(i)
        break
else:
    print(0)

"""
3
100 100 1
の答えは
2
"""
