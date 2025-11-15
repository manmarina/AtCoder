N, X, Y = map(int, input().split())
CAB = [list(input().split()) for _ in range(N)]
print(CAB)

grid = []
for i in range(X):
    for j in range(Y):
        grid.append([i, j])
print(sorted(grid))

for c, a, b in CAB:
    a = int(a)
    b = int(b)
    if c == 'X':
        for i in range(len(grid)):
            if grid[i][0] < a:
                grid[i][1] -= b
            else:
                grid[i][1] += b

    else:  # c == 'Y'
        for i in range(len(grid)):
            if grid[i][1] < a:
                grid[i][0] -= b
            else:
                grid[i][0] += b
print(sorted(grid))

"""
未完
いいところまでいったかと思ったけど、チャッピーによると計算量が全然だめらしい。

https://chatgpt.com/g/g-p-688d3155796881919ed997146b54eec1-atcoder/c/69188305-8080-8322-aab0-cf4db7b9455b
"""
