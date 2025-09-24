s = input().strip()

# 先頭と末尾の a の個数を数える
h = 0
while h < len(s) and s[h] == 'a':
    h += 1

t = 0
while t < len(s) and s[-1 - t] == 'a':
    t += 1

"""
これでもよい
h = len(s) - len(s.lstrip('a'))
t = len(s) - len(s.rstrip('a'))
"""

if h > t:
    print("No")
else:
    core = s[h:len(s) - t]  # 本体
    print("Yes" if core == core[::-1] else "No")

"""
文字列操作系
チャッピー
“先頭に好きなだけ a を足して回文にできるか？”を判定する問題

https://atcoder.jp/contests/abc237/tasks/abc237_c
https://chatgpt.com/c/68d36dd5-b3e4-832a-a440-768629fe6707
"""
