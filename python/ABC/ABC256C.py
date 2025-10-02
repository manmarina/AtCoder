H1, H2, H3, W1, W2, W3 = map(int, input().split())

ans = 0
for a11 in range(1, H1 - 1):  # 1行1列
    for a12 in range(1, H1 - a11):  # 1行2列
        a13 = H1 - a11 - a12  # 1行3列
        if a13 <= 0:
            continue

        for a21 in range(1, H2 - 1):  # 2行1列
            for a22 in range(1, H2 - a21):  # 2行2列
                a23 = H2 - a21 - a22  # 2行3列
                if a23 <= 0:
                    continue

                a31 = W1 - a11 - a21  # 3行1列
                a32 = W2 - a12 - a22  # 3行2列
                if a31 <= 0 or a32 <= 0:
                    continue

                left = H3 - a31 - a32  # 3行3列 横方向から
                right = W3 - a13 - a23  # 3行3列 縦方向から
                if left == right and left > 0:
                    ans += 1

print(ans)

"""
全探索
チャッピー

数独・ナンプレ風問題
3x3 の正の整数マスに行和 H1,H2,H3 と列和 W1,W2,W3 を合わせる「個数を数える」課題です。

https://atcoder.jp/contests/abc256/tasks/abc256_c
https://chatgpt.com/g/g-p-688d3155796881919ed997146b54eec1-atcoder/c/68de164a-353c-832c-bb68-09af6cf6dbd7
"""
