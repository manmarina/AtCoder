H, A = map(int, input().split())

attack = H // A
if H % A:
    attack += 1
print(attack)
