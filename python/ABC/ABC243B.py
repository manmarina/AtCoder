N = int(input())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

count1 = 0
for a, b in zip(A, B):
    if a == b:
        count1 += 1

count2 = len(set(A) & set(B)) - count1

print(count1, count2)
