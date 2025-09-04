B = int(input())

# range(16)とするとWA pythonで0**0=1なので、B=1のケースでWAになる
for A in range(1, 16):  # A=15の時にA**Aは10**18を超えるので
    if A**A == B:
        print(A)
        break
else:
    print(-1)
