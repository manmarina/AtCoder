from collections import Counter

S = input()

cnt = Counter(S)
for i in range(1, -(-len(S) // 2)):
    kinds = len([c for c in cnt.values() if c == i])
    if kinds != 2 and kinds != 0:
        print("No")
        break
else:
    print("Yes")
