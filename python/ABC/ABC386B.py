S = input()


def count_zero(run):
    if run % 2:
        run = -(-run // 2)
    else:
        run //= 2
    return run


run = 0
count = 0
for s in S:
    if s == '0':
        run += 1
    else:
        count += count_zero(run)
        run = 0
        count += 1
count += count_zero(run)

print(count)
