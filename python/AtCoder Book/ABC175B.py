N = int(input())
L = list(map(int, input().split()))


def count_triangle(num, bar):
    pool = set()
    for i in range(num - 2):
        for j in range(i + 1, num - 1):
            for k in range(j + 1, num):
                tri = sorted([bar[i], bar[j], bar[k]])
                if tri[0] == tri[1] or tri[1] == tri[2]:
                    continue
                if tri[0] + tri[1] > tri[2]:
                    pool.add((i + 1, j + 1, k + 1))
    return len(pool)


print(count_triangle(N, L))
