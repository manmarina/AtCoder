A, B, C, D, E, F, X = map(int, input().split())


def distance(run, speed, rest):
    total_time = X
    dist = 0
    while total_time > 0:
        if total_time >= run:
            dist += run * speed
            total_time -= run + rest
        else:
            dist += speed * total_time
            break
    return dist


takahashi = distance(A, B, C)
aoki = distance(D, E, F)

if takahashi > aoki:
    print("Takahashi")
elif takahashi < aoki:
    print("Aoki")
else:
    print("Draw")
