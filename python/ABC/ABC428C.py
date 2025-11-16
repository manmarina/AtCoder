Q = int(input())
Query = [list(input().split()) for _ in range(Q)]
# print(Query)

out = set()
stack = []
score = 0
for q in Query:
    if q[0] == '1':
        _, c = q
        stack.append(c)
        if c == ')' and score == 0:
            out.add(len(stack) - 1)

        if c == ')':
            score -= 1
        else:  # c == '(':
            score += 1

        # print(stack)
        # print(out)
        # print("score:", score)
        # print()

    else:  # q[0] == '2':
        if stack.pop() == ')':
            score += 1
        else:
            score -= 1
        if len(stack) in out:
            out.remove(len(stack))

        # print(stack)
        # print(out)
        # print("score:", score)
        # print()

    if out:
        print("No")
    elif score == 0:
        print("Yes")
    else:
        print("No")

"""
場合分け系
リトライ
不正な')'が出現したら位置をoutに格納。
outが空にならない限り、'('と')'の数が一致してもYesにならない。

https://atcoder.jp/contests/abc428/tasks/abc428_c
"""
