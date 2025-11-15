ABC = list(map(int, input().split()))
ABC.sort(reverse=True)
# print(ABC)
print(*ABC, sep='')
