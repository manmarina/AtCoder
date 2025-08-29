S = input()

has_lower = False
has_upper = False
seen = set()

for ch in S:
    if ch in seen:
        print("No")
        break
    seen.add(ch)
    if ch.islower():
        has_lower = True
    if ch.isupper():
        has_upper = True
else:
    print("Yes" if has_lower and has_upper else "No")
