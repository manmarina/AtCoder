S = input().strip()
a = [int(x) for x in S]  # [A,B,C,D]

for mask in range(1 << 3):  # 0..7
    val = a[0]
    ops = []  # 文字列復元用
    for i in range(3):
        if (mask >> i) & 1:  # 1: '+', 0: '-'
            val += a[i + 1]
            ops.append('+')
        else:
            val -= a[i + 1]
            ops.append('-')
    if val == 7:
        expr = f"{a[0]}{ops[0]}{a[1]}{ops[1]}{a[2]}{ops[2]}{a[3]}=7"
        print(expr)
        break
