N, M = map(int, input().split())
S = input()
T = input()

is_pre = T.startswith(S)
is_suf = T.endswith(S)

if is_pre:
    if is_suf:
        print(0)
    else:
        print(1)
elif is_suf:
    print(2)
else:
    print(3)
