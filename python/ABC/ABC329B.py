N = int(input())
A = list(map(int, input().split()))

del_max = [a for a in A if a != max(A)]
print(max(del_max))
