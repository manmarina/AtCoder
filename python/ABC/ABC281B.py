S = input()

pre = S[0]
num = S[1:-1]
suf = S[-1]

ok = (
    pre.isupper() and
    len(num) == 6 and
    num.isdigit() and  # numが数字でないとint(num)でエラーになるので
    100000 <= int(num) <= 999999 and
    suf.isupper()
)

print("Yes" if ok else "No")
