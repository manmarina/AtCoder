N = int(input())
# print(ord('{'))

hoge = []
while N > 0:
    N -= 1  # 毎回1を引くのがポイント
    hoge.append(N % 26)
    N //= 26

hoge = hoge[::-1]
# print(hoge)

fuga = []
for h in hoge:
    fuga.append(chr(h + 97))

# print(fuga)
print(*fuga, sep='')

"""
数学的な気づき系
けんちょん
https://drken1215.hatenablog.com/entry/2020/06/21/225500
26進数もどき（0が使えない）に変換する問題。
毎回「N を 1 減らしてから N % 26」を使う処理が重要。
自分の実装をけんちょんの解説により改良。

https://atcoder.jp/contests/abc171/submissions/me
https://chatgpt.com/g/g-p-688d3155796881919ed997146b54eec1-atcoder/c/6916c3b7-4884-8320-8fe6-f18d64dfb0bf
"""
