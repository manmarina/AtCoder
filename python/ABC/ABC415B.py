S = input()

pending = None
for i, s in enumerate(S, 1):
    if s == '#':
        if pending is None:
            pending = i
        else:
            print(f"{pending},{i}")
            pending = None
