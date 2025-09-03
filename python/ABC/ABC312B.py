N, M = map(int, input().split())
S = [input() for _ in range(N)]
# print(S)


def get_code(i, j):
    code = [[]for _ in range(9)]
    for r in range(9):
        for c in range(9):
            code[r].append(S[i + r][j + c])
    return code


def is_Tak(code):
    # 左上の#チェック
    for i in range(3):
        for j in range(3):
            if code[i][j] != '#':
                return False

    # 右下の#チェック
    for i in range(6, 9):
        for j in range(6, 9):
            if code[i][j] != '#':
                return False

    # 左上の.チェック
    j = [0, 1, 2, 3, 3, 3, 3]
    i = [3, 3, 3, 3, 2, 1, 0]
    for r, c in zip(i, j):
        if code[r][c] != '.':
            return False

    # 右下の.チェック
    j = [5, 5, 5, 5, 6, 7, 8]
    i = [8, 7, 6, 5, 5, 5, 5]
    for r, c in zip(i, j):
        if code[r][c] != '.':
            return False
    return True


for i in range(N - 8):
    for j in range(M - 8):
        code = get_code(i, j)

        if is_Tak(code):
            # for row in code:
            #     print(*row, sep='')
            print(i + 1, j + 1)
