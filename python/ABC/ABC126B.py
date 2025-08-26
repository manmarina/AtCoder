S = input()
L = int(S[:2])
R = int(S[2:])

# print(L, R)

LY = False
RY = False

if L > 12 or L == 0:
    LY = True
if R > 12 or R == 0:
    RY = True

if LY and RY:
    print("NA")
elif LY:
    print("YYMM")
elif RY:
    print(("MMYY"))
else:
    print("AMBIGUOUS")
