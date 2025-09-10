ABCD = input()

ln = len(ABCD)
formulas = []
ans = 0
for mask in range(1 << (ln - 1)):  # ビットマスクを生成
    temp = int(ABCD[0])
    formula = [ABCD[0]]
    for i in range(1, ln):
        if mask >> (i - 1) & 1:  # ビットマスクが1なら+、0なら-
            temp += int(ABCD[i])
            formula.append('+' + ABCD[i])
        else:
            temp -= int(ABCD[i])
            formula.append('-' + ABCD[i])

    # 答えを追記して配列に格納
    formula.append('=' + str(temp))
    formulas.append(''.join(formula))

    # 答えが7のときのインデックスを格納
    if temp == 7:
        ans = len(formulas) - 1

# print(*formulas)
print(formulas[ans])
