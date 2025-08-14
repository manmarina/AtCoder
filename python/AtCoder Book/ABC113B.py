N = int(input())
T, A = map(int, input().split())
H = list(map(int, input().split()))

difference = []
for i in range(N):
    temperature = T - H[i] * 0.006
    if temperature < A:
        diff = A - temperature
    else:
        diff = temperature - A
    difference.append(diff)

print(difference.index(min(difference)) + 1)
