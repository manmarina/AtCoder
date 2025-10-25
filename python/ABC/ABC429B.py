import logging
logging.basicConfig(level=logging.INFO, format='[%(levelname)s] %(message)s')


N, M = map(int, input().split())
A = list(map(int, input().split()))
logging.debug(f"{A = }")

diff = sum(A) - M
logging.debug(f"{diff = }")

if diff in set(A):
    print("Yes")
else:
    print("No")
