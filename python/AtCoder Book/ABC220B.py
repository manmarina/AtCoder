K = int(input())
A, B = input().split()


def convert_to_decimal(num, base):
    dec = 0
    digit = 1
    length = len(num)
    for i in range(1, length + 1):
        dec += int(num[length - i]) * digit
        digit *= base
    return dec


dec_A = convert_to_decimal(A, K)
dec_B = convert_to_decimal(B, K)

# print(dec_A, dec_B)
print(dec_A * dec_B)
