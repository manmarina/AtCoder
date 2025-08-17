ABCD = input()

# 4桁の文字列を1桁の数値*4に変換
A, B, C, D = map(int, ABCD)

# 解を全探索
sign = ['+', '-']
for op1 in sign:
    for op2 in sign:
        for op3 in sign:
            expr = f"{A}{op1}{B}{op2}{C}{op3}{D}"
            if eval(expr) == 7:
                print(expr + "=7")
                exit()
