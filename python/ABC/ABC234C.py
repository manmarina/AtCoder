K = int(input())
out = []
while K > 0:
    # 余り0のときは0、余り1のときは2、を繰り返す
    out.append('0' if K % 2 == 0 else '2')
    K //= 2
# 逆順に表示
print(''.join(reversed(out)))

"""
数学的な気づき系
チャッピー
2進表記の「1」を「2」に置き換えて出力するだけの問題です。

汎用性のある解

https://atcoder.jp/contests/abc234/tasks/abc234_c
https://chatgpt.com/c/68d35662-8f00-8325-841b-546c537dd42a
"""
