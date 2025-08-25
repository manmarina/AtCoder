N = int(input())
lr = [list(map(int, input().split())) for i in range(N)]

print(sum([r - l + 1 for l, r in lr]))
