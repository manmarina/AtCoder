N, M = map(int, input().split())
A = list(map(int, input().split()))

play = N - sum(A)
print(play if play >= 0 else -1)
