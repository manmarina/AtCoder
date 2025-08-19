N = int(input())
A = list(map(int, input().split()))

ans = []
start = 0
dir = 0  # 0: 未確定, +1: 非減少, -1: 非増加

for i in range(1, N):
    if dir == 0:
        if A[i] > A[i - 1]:
            dir = +1
        elif A[i] < A[i - 1]:
            dir = -1
    elif dir == +1:
        if A[i] < A[i - 1]:
            ans.append(A[start:i])  # [start .. i-1]
            start = i
            dir = 0
    else:  # dir == -1
        if A[i] > A[i - 1]:
            ans.append(A[start:i])  # [start .. i-1]
            start = i
            dir = 0

ans.append(A[start:N])  # 最後の区間
print(len(ans))
