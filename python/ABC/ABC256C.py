h1, h2, h3, w1, w2, w3 = map(int, input().split())

ans = 0
# 1行目
for a11 in range(1, h1 - 1):
    for a12 in range(1, h1 - a11):
        a13 = h1 - a11 - a12  # 1行3列目
        if a13 <= 0:
            continue

        # 2行目
        for a21 in range(1, h2 - 1):
            for a22 in range(1, h2 - a21):
                a23 = h2 - a21 - a22  # 2行3列目
                if a23 <= 0:
                    continue

                # 3行目
                a31 = w1 - a11 - a21
                a32 = w2 - a12 - a22
                if a31 <= 0 or a32 <= 0:
                    continue

                # 3行3列目
                hol = h3 - a31 - a32
                ver = w3 - a13 - a23
                if hol == ver and hol > 0:
                    a33 = hol
                    ans += 1

                    # print("1:", a11, a12, a13)
                    # print("2:", a21, a22, a23)
                    # print("3:", a31, a32, a33)
                    # print()

print(ans)

"""
工夫して探索の通り数を減らす全探索
写経

数独・ナンプレ風問題
3x3 の正の整数マスに行和 H1,H2,H3 と列和 W1,W2,W3 を合わせる「個数を数える」課題です。

https://atcoder.jp/contests/abc256/tasks/abc256_c
https://chatgpt.com/g/g-p-688d3155796881919ed997146b54eec1-atcoder/c/68de164a-353c-832c-bb68-09af6cf6dbd7
"""
