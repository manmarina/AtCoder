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

"""
ビット全探索
bit全探索（bitmask）

4桁 a,b,c,d の間には演算子を3箇所入れるので、各箇所を「+ or -」の2択 → 2³=8通りを総当りすればOK。

アルゴリズムのポイント
    4桁の文字列 S を数値に分解：A = int(S[0]), B = int(S[1]), C = int(S[2]), D = int(S[3])
    3つの隙間（A|B, B|C, C|D）に入れる演算子をビットで表現
        例：mask の 0bit= A|B, 1bit= B|C, 2bit= C|D
        0 → -, 1 → +（逆でも可）
    mask を 0..7 で回し、式を左から順に評価
    ちょうど 7 になった式を "=7" を付けて出力して終了（必ず存在します）
"""
