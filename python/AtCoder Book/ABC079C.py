ABCD = input()

# 4桁の文字列を1桁の数値*4に変換
A, B, C, D = map(int, ABCD)

# 解を全探索
sign = ['+', '-']
for op1 in sign:
    for op2 in sign:
        for op3 in sign:
            result = A + (B if op1 == '+' else -B)
            result += (C if op2 == '+' else -C)
            result += (D if op3 == '+' else -D)
            if result == 7:
                print(f"{A}{op1}{B}{op2}{C}{op3}{D}=7")
                exit()
