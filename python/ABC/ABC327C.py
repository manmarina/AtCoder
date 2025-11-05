A = [list(map(int, input().split())) for _ in range(9)]
# print(A)

N = 9

# 行のチェック
for i in range(N):
    if len(set(A[i])) != N:
        print("No")
        exit()

# 列のチェック
for j in range(N):
    temp = set()
    for i in range(N):
        temp.add(A[i][j])
    if len(set(temp)) != N:
        print("No")
        exit()

# 3x3のチェック
for j in range(0, N, 3):
    for i in range(0, N, 3):
        temp = set()
        for k in range(3):
            for l in range(3):
                temp.add(A[i + k][j + l])
        if len(set(temp)) != N:
            print("No")
            exit()

print(("Yes"))

"""
基本実装問題
9 x 9 に並んだ数字が「数独」の解になっているかを判定する問題

けんちょんの解説
https://drken1215.hatenablog.com/entry/2023/11/05/104000

https://atcoder.jp/contests/abc327/tasks/abc327_c
"""
