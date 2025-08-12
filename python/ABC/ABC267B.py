import sys

S = '?' + input()

check = ["oxo", 'oxxo', 'oxxxo', 'oxxxxo', 'oxxxxxo']
line = ""

if S[1] == '1':
    print("No")
    sys.exit()

if S[7] == '1':
    line += 'o'
else:
    line += 'x'

if S[4] == '1':
    line += 'o'
else:
    line += 'x'

if S[2] == '1' or S[8] == '1':
    line += 'o'
else:
    line += 'x'

if S[5] == '1':
    line += 'o'
else:
    line += 'x'

if S[9] == '1' or S[3] == '1':
    line += 'o'
else:
    line += 'x'

if S[6] == '1':
    line += 'o'
else:
    line += 'x'

if S[10] == '1':
    line += 'o'
else:
    line += 'x'

for i in range(5):
    if check[i] in line:
        print("Yes")
        break
else:
    print("No")
