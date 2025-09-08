N = int(input())
cl = [list(input().split())for _ in range(N)]


def check_len(l):
    if l > INF:
        print("Too Long")
        exit()


INF = 100
S = ''
for c, l in cl:
    l = int(l)
    check_len(l)

    S += c * l
    check_len(len(S))

print(S)
