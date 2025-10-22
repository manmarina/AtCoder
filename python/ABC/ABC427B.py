N = int(input())


def f(n):
    if n == 0:
        return 1
    n = str(n)
    temp = 0
    for s in n:
        temp += int(s)
    return temp


ans = [1]
for i in range(N - 1):
    ans.append(ans[-1] + f(ans[-1]))
print(ans[-1])

"""
基本実装問題

Ai = Ai-1 + f(Ai-1)となることを見抜いて実装
"""
