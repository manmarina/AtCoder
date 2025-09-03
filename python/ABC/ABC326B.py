N = int(input())

for n in range(N, 920):  # 919 を含める
    a = n // 100
    b = (n // 10) % 10
    c = n % 10
    if a * b == c:
        print(n)
        break
