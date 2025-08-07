A, B, C, D, E, F, X = map(int, input().split())


def distance(A, B, C):
    rest = X
    dist = 0
    while rest > 0:
        if rest >= A:
            dist += A * B
            rest -= A + C
        else:
            dist += B * rest
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
