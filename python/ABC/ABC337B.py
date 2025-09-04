S = input().strip()


def ok(s: str) -> bool:
    phase = 1  # 1:A, 2:B, 3:C
    for ch in s:
        if ch == 'A':
            if phase > 1:  # BやCの後にAが出た
                return False
        elif ch == 'B':
            if phase == 3:  # Cの後にBが出た
                return False
            phase = 2
        elif ch == 'C':
            phase = 3
        else:
            return False  # A/B/C以外が混ざっている
    return True


print("Yes" if ok(S) else "No")
