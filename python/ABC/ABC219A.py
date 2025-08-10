X = int(input())

answer = "expert"
if X < 40:
    answer = 40 - X
elif X < 70:
    answer = 70 - X
elif X < 90:
    answer = 90 - X

print(answer)
