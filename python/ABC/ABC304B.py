N = int(input())

base = 10**(len(str(N)) - 3)
print(N // base * base if N >= 1000 else N)
