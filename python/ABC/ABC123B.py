from itertools import permutations

A = int(input())
B = int(input())
C = int(input())
D = int(input())
E = int(input())


def ceil_to_tens(n):
    return ((n + 9) // 10) * 10


menu = [A, B, C, D, E]
ans = []
for p in permutations(menu):
    temp = 0
    for i, v in enumerate(p):
        if i == 4:
            temp += v
        else:
            temp += ceil_to_tens(v)
    else:
        ans.append(temp)

print(min(ans))
