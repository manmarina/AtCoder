S = input()

if len(S) % 2:
    S = S[:-1]
else:
    S = S[:-2]

while 1:
    front = S[:len(S) // 2]
    back = S[len(S) // 2:]
    if front == back:
        print(len(S))
        break
    S = S[:-2]
