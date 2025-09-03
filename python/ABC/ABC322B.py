N, M = map(int, input().split())
S = input()
T = input()

# print(T[:len(S)])
# print(T[-len(S):])

pre = T[:len(S)]
suf = T[-len(S):]

if S == pre:
    if S == suf:
        print(0)
    else:
        print(1)
elif S == suf:
    print(2)
else:
    print(3)
