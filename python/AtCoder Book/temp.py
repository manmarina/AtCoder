def split_monotone_segments(A):
    n = len(A)
    if n == 0:
        return []
    ans = []
    start = 0
    dir = 0  # 0: 未確定, +1: 非減少, -1: 非増加

    for i in range(1, n):
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

    ans.append(A[start:n])  # 最後の区間
    return ans


# 動作確認
N = 6
A = [1, 2, 3, 2, 2, 1]
print(split_monotone_segments(A))  # -> [[1, 2, 3], [2, 2, 1]]
