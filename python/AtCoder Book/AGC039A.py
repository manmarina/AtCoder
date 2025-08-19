S = input()
K = int(input())

string = S
rear = None

# 最初の文字と最後の文字が一致するときは、最後の文字が連続する分を抜き出す
i = len(S)
if S[0] == S[i - 1]:
    while i > 0 and S[i - 1] == S[0]:
        i -= 1
    string = S[:i]
    rear = S[i:]
    # print(string, rear)

    # 後ろの文字列の書き換え回数をカウント
    if len(rear) % 2 == 0:
        count_rear = len(rear) // 2
    else:
        count_rear = len(rear) // 2 + 1


# 文字の書き換え回数をカウント
i = 1
count = 0
while i < len(string):
    if string[i - 1] == string[i]:
        count += 1
        i += 2
        continue
    i += 1
answer = count * K

# rearが存在するときはcountを合算
if rear:
    count += count_rear
    answer = count * K
    if len(rear) % 2 == 1:
        answer -= 1

print(answer)
