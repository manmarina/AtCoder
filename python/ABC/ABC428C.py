Q = int(input())

out = set()

stack = []
score = 0
for _ in range(Q):
    q = input().split()
    num = int(q[0])
    if num == 1:
        stack.append(q[1])
        if q[1] == '(':
            score += 1
        else:
            score -= 1

        if score == 0 and q[1] == ')':
            out.add(len(stack))
    else:  # num == 2
        if len(stack) in out:
            out.remove(len(stack))
        if stack.pop() == '(':
            score -= 1
        else:
            score += 1

    if not stack and not out:
        print("Yes")
    elif stack[0] != ')' and score == 0:
        print("Yes")
    else:
        print("No")

    # print(stack, score)
