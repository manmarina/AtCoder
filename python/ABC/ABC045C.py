from itertools import product

S = input()

# +の位置を決定
bit = [0, 1]
bits = []
for b in product(bit, repeat=len(S) - 1):
    bits.append(b)
# print(bits)

# +を組み込んだ数式を配列に格納
formulas = []
for bs in bits:
    formula = [S[0]]
    for i in range(1, len(S)):
        if bs[i - 1] == 1:
            formula.append('+')
        formula.append(S[i])
    formulas.append(''.join(formula))
# print(formulas)

# 配列内の数式の計算結果を合計
ans = []
for f in formulas:
    ans.append(eval(f, {"__builtins__": None}, {}))
# print(ans)

# 結果出力
print(sum(ans))
