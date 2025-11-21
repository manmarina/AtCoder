N = int(input())
AB = [list(map(int, input().split())) for _ in range(N)]
# print(AB)

C = []
for i, ab in enumerate(AB, 1):
    a, b = ab
    C.append((a / (a + b), i))
C.sort(key=lambda x: (-x[0], x[1]))
# print(C)

for _, i in C:
    print(i, end=' ')
print()

"""
WA
誤差でWAしてしまう

けんちょんの解説
https://drken1215.hatenablog.com/entry/2023/10/22/124200

https://atcoder.jp/contests/abc308/tasks/abc308_c
"""
