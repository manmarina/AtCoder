N, M = map(int, input().split())
sc = [tuple(map(int, input().split())) for _ in range(M)]

# print(1, sc)


def is_able_number(N, conditions_list):
    conditions = set(_ for _ in conditions_list)
    # print(2, conditions)

    first_digit = []
    for condition in conditions:
        # 矛盾チェック（N=1以外の時、先頭桁が0はNG
        if condition == (1, 0) and N != 1:
            return None
        first_digit.append(condition[0])

    # print(3, first_digit)

    # 矛盾チェック（同じ桁に違う値が来たらNG）
    if len(first_digit) != len(set(first_digit)):
        return None

    return conditions


def make_integer(digit, conditions):
    integer_list = [0 for i in range(digit)]
    for condition in conditions:
        integer_list[condition[0] - 1] = condition[1]

    # 1桁目が0なら1に更新
    if integer_list[0] == 0 and N != 1:
        integer_list[0] = 1
    # print(5, integer_list)

    integer = 0
    for d in integer_list:
        integer = integer * 10 + d
    return integer


conditions = is_able_number(N, sc)
# print(4, conditions)

if conditions is None:
    print(-1)
else:
    print(make_integer(N, conditions))
