S = input()

SS = S + S
rotation = [SS[i:i + len(S)] for i in range(len(S))]

print(min(rotation))
print(max(rotation))
