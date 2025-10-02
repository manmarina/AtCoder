def rle(s):
    # （文字,文字数)を格納するリストを作成
    res = []
    i, n = 0, len(s)
    while i < n:
        j = i
        while j < n and s[j] == s[i]:
            j += 1
        res.append((s[i], j - i))
        i = j
    return res


S = input().strip()
T = input().strip()

RS = rle(S)  # Sの（文字,文字数)を格納するリスト
RT = rle(T)  # Tの（文字,文字数)を格納するリスト
print("RS =", RS)
print("RT =", RT)

ok = True
if len(RS) != len(RT):  # セクション数が異なったらアウト
    ok = False
else:
    for (cs, ls), (ct, lt) in zip(RS, RT):
        if cs != ct:  # 文字が違ったらアウト
            ok = False
            break
        if lt < ls:  # ltのほうが長かったらアウト
            ok = False
            break
        if ls == lt:  # 同じ文字数なら次の判定へ
            continue
        # ここから ls < lt
        if ls == 1:   # 長さ1の区間は伸ばせないのでアウト
            ok = False
            break

print("Yes" if ok else "No")

"""
文字列処理 / ランレングス圧縮(RLE)
チャッピー

操作は「同じ文字が連続2個以上ある箇所だけを、さらに同じ文字で伸ばせる（増やせる）」というもの。
→ つまり 文字の並び順は変えられない、かつ 各連続区間（run）の長さは“そのまま”か“増加”しか起きない。ただし長さ1の区間は増やせない。
これを文字列S, Tの**RLE（文字と長さの列）**に分解して、各区間で判定します。

https://atcoder.jp/contests/abc259/tasks/abc259_c
https://chatgpt.com/g/g-p-688d3155796881919ed997146b54eec1-atcoder/c/68de28fd-d204-8327-85a6-4d40c0bb8216
"""
