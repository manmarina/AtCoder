S = input()

ls = len(S)
ans = set()
for i in range(1, ls + 1):
    # print(i, end=':')
    for j in range(ls + 1 - i):
        # print(j, end='')
        ans.add(S[j:j + i])
    # print()

# print(ans)
print(len(ans))

"""
やることはシンプルです。「全部の部分文字列を列挙して set で重複排除 → 個数を数える」だけです。
"""
