N = int(input())


def divide_times(n):
    times = 0
    while n % 2 == 0:
        n //= 2
        times += 1
    return times


max = 0
max_index = 1
for i in range(1, N + 1):
    dt = divide_times(i)
    # print(i, dt)
    if max < dt:
        max = dt
        max_index = i
print(max_index)
