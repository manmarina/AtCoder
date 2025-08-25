S = input()

abc = set(chr(i) for i in range(97, 97 + 26))
diff = abc - set(S)
if diff:
    print(min(diff))
else:
    print("None")
