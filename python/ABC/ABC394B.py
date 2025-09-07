N = int(input())
S = [input() for _ in range(N)]

# S.sort(key=len) チャッピー
S.sort(key=lambda x: len(x))
print(*S, sep='')
