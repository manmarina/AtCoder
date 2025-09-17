N, A, B = map(int, input().split())

# 1行要素を作成
dot_block = ""
hash_block = ""
for i in range(N):
    if i % 2 == 0:
        dot_block += '.' * B
        hash_block += '#' * B
    else:
        dot_block += '#' * B
        hash_block += '.' * B
# print(dot_block)
# print(hash_block)

# N,Aを元にタイルを作成
for i in range(N):
    for j in range(A):
        if i % 2 == 0:
            print(dot_block)
        else:
            print(hash_block)

"""
元は NxN の市松模様（チェッカーボード） を作成します。
1マスを AxB の同一文字ブロック に拡大した図を出力します。
市松模様なので、ブロック（マス）は横・縦に交互に「.」と「#」が切り替わります。
"""
