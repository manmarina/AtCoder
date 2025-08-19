S = input()


def calc_num(cnt):
    ans = 0
    for i in range(1, cnt + 1):
        ans += i
    return ans


i = 0
cut = []
while i < len(S):
    j = i + 1
    while j < len(S) and S[i] == S[j]:
        j += 1
    cut.append(S[i:j])
    i = j

# print(cut)

answer = []
i = 0
while i < len(cut):
    # 最初が＞のとき
    if cut[i][0] == '>':
        cnt = calc_num(len(cut[i]))
        answer.append((cnt,))
        i += 1
    # 最後が＜のとき
    elif i == len(cut) - 1 and cut[i][0] == '<':
        cnt = calc_num(len(cut[i]))
        answer.append((cnt,))
        i += 1
    # 通常の時
    else:
        cnt_1 = len(cut[i])
        cnt_2 = len(cut[i + 1])
        if cnt_1 < cnt_2:
            cnt_1 = calc_num(cnt_1 - 1)
            cnt_2 = calc_num(cnt_2)
        else:
            cnt_1 = calc_num(cnt_1)
            cnt_2 = calc_num(cnt_2 - 1)
        answer.append((cnt_1, cnt_2))
        i += 2

print(sum(map(sum, answer)))
