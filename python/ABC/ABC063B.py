from collections import Counter

S = input()

if all(counter == 1 for counter in Counter(S).values()):
    print("yes")
else:
    print("no")
