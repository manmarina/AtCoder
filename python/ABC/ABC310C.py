N = int(input())

seen = set()
for _ in range(N):
    s = input().strip()
    seen.add(min(s, s[::-1]))  # 文字列の向きを正規化！！
print(len(seen))

"""
文字列操作
各文字列をmin(s, s[::-1]) に正規化して集合に入れるのが一番シンプルで安全です。

けんちょん
https://drken1215.hatenablog.com/entry/2025/02/09/023754

https://atcoder.jp/contests/abc310/tasks/abc310_c
https://chatgpt.com/g/g-p-688d3155796881919ed997146b54eec1-atcoder/c/690c560e-0b80-8321-b5d5-46855a13b20b
"""
