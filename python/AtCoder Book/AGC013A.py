N = int(input())
A = list(map(int, input().split()))

i = 0
answer = []
while i < N:
    flag = 0
    j = i + 1
    while j < N:
        if flag == 0:  # 初期値なら
            if A[j - 1] < A[j]:  # 増加なら
                flag = 1
            elif A[j - 1] > A[j]:  # 減少なら
                flag = 2
            j += 1
        elif flag == 1:  # 増加なら
            if A[j - 1] > A[j]:  # 逆行したら
                flag = 0
                answer.append(A[i:j])
                i = j
                break
            j += 1
        elif flag == 2:  # 減少なら
            if A[j - 1] < A[j]:  # 逆行したら
                flag = 0
                answer.append(A[i:j])
                i = j
                break
            j += 1
    else:
        temp = i
        i = j
answer.append(A[temp:j])

print(len(answer))
