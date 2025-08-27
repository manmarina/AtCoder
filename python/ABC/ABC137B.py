K, X = map(int, input().split())

start = X - K + 1
end = X + K - 1
print(*range(start, end + 1))
