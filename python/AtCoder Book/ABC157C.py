N, M = map(int, input().split())
sc = []
for i in range(M):
    sc.append(list(map(int, input().split())))


def is_able_number(conditions_list):
    conditions = set()
    for condition in conditions_list:
        conditions.add(tuple(condition))
    first_digit = []
    for condition in conditions:
        if condition == (1, 0) and len(conditions) != 1:
            return None
        first_digit.append(condition[0])
    if len(first_digit) != len(set(first_digit)):
        return None
    return conditions


def make_integer(digit, conditions):
    integer_list = [0 for i in range(digit)]
    for condition in conditions:
        integer_list[condition[0] - 1] = condition[1]
    integer = 0
    for d in integer_list:
        integer = integer * 10 + d
    return integer


conditions = is_able_number(sc)
if conditions is None:
    print(-1)
else:
    print(make_integer(N, conditions))
