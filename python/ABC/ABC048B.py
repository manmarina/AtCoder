a, b, x = map(int, input().split())

ma = (a - 1) // x
mb = b // x
print(mb - ma)
