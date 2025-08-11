S = input()

prefix = S[0]
suffix = S[-1]
number = S[1:7]

if len(S) != 8:
    print("No")
elif not prefix.isupper():
    print("No")
elif not suffix.isupper():
    print("No")
elif not number.isdigit():
    print("No")
elif int(number) < 100000:
    print("No")
else:
    print("Yes")
