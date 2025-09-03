N = int(input())
WX = [list(map(int, input().split())) for _ in range(N)]


def ok(t, X):
    x = (t + X) % 24
    if 9 <= x < 18:
        return True
    return False


time = []
for t in range(24):
    count = 0
    for W, X in WX:
        if ok(t, X):
            count += W
    time.append(count)
# print(time)
print(max(time))
