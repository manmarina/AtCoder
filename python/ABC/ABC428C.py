Q = int(input())

stack = []
for _ in range(Q):
    q = input().split()
    num = int(q[0])
    if num == 1:
        if q[1] == ')' and stack[-1] == '(':
            stack.pop()
        else:
            stack.append(q[1])
    else:  # num == 2
        if stack:
            stack.pop()
        else:
            stack.append('(')

    if stack:
        print("No")
    else:
        print("Yes")
