N = int(input())

# 10進数の確認
ok = set()  # 7を含む数を格納するset
for i in range(1, N + 1):  # 1~Nまで
    for s in str(i):
        if s == '7':
            ok.add(i)


# 8進数に変換したときに7を含むか判定する関数
def has_seven(n):
    while n > 0:
        if str(n % 8) == '7':
            return True
        n //= 8
    return False


# 8進数の確認
for i in range(1, N + 1):  # 1~Nまで
    if has_seven(i):
        ok.add(i)

print(N - len(ok))  # Nから7を含む数の個数を引いたものが答え

"""
数学的な気づき系
8進数に変換する。
7が含まれる数をsetに追加してゆく。

けんちょんの解説
https://drken1215.hatenablog.com/entry/2020/12/19/224100

https://atcoder.jp/contests/abc186/tasks/abc186_c
https://chatgpt.com/g/g-p-688d3155796881919ed997146b54eec1-atcoder/c/69104278-ae84-8321-b4c6-b1ae94a9715e
"""
