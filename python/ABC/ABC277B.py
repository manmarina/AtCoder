N = int(input())
S = [input() for _ in range(N)]
# print(S)

ok1 = set("HDCS")
ok2 = set("A23456789TJQK")


def is_trump(S):
    if len(S) != len(set(S)):
        return False
    for s in S:
        if s[0] not in ok1:
            return False
        if s[1] not in ok2:
            return False
    return True


print("Yes" if is_trump(S) else "No")
