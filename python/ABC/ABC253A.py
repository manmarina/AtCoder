import statistics

abc = list(map(int, input().split()))
med = statistics.median(abc)

if abc[1] == med:
    print("Yes")
else:
    print("No")
