K = int(input())
# 二進数表記にして、1を2に置換するだけ
print(bin(K)[2:].replace('1', '2'))

"""
数学的な気づき系
チャッピー
2進表記の「1」を「2」に置き換えて出力するだけの問題です。

Pythonらしい簡潔解

https://atcoder.jp/contests/abc234/tasks/abc234_c
https://chatgpt.com/c/68d35662-8f00-8325-841b-546c537dd42a
"""
